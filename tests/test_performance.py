import pytest
from playwright.sync_api import Page
from typing import List, Dict


@pytest.mark.smoke
class TestPerformanceAndAssets:
    """Validates page load timing metrics and ensures zero broken network assets."""

    def test_zero_failed_network_requests(self, page: Page, base_url: str):
        """TC-PRF-01: Ensure all static resources (CSS, Fonts, Scripts) return HTTP 200/304."""
        failed_requests: List[Dict[str, object]] = []

        def on_response(response):
            # Only monitor assets loaded by the page, ignore non-http protocols
            if response.url.startswith("http") and response.status >= 400:
                failed_requests.append({
                    "url": response.url,
                    "status": response.status,
                    "status_text": response.status_text
                })

        page.on("response", on_response)
        response = page.goto(base_url, wait_until="networkidle")

        assert response is not None
        assert len(failed_requests) == 0, (
            f"Detected {len(failed_requests)} broken asset request(s):\n"
            + "\n".join([f"[{r['status']}] {r['url']}" for r in failed_requests])
        )

    def test_page_load_timing_thresholds(self, page: Page, base_url: str):
        """TC-PRF-02: Verify Navigation Timing API metrics remain within performant limits."""
        page.goto(base_url, wait_until="load")

        # Extract browser performance timing metrics
        timing = page.evaluate("""() => {
            const [navigation] = performance.getEntriesByType('navigation');
            return {
                dnsTime: navigation.domainLookupEnd - navigation.domainLookupStart,
                tcpTime: navigation.connectEnd - navigation.connectStart,
                domContentLoaded: navigation.domContentLoadedEventEnd - navigation.startTime,
                pageLoad: navigation.loadEventEnd - navigation.startTime
            };
        }""")

        # Performance assertions (thresholds in milliseconds)
        assert timing["domContentLoaded"] < 5000, (
            f"DOMContentLoaded took too long: {timing['domContentLoaded']:.2f}ms"
        )
        assert timing["pageLoad"] < 8000, (
            f"Page Load took too long: {timing['pageLoad']:.2f}ms"
        )

    def test_about_page_zero_failed_network_requests(self, page: Page, base_url: str):
        """TC-PRF-03: Ensure about.html loads without any 404 or broken assets."""
        failed_requests: List[str] = []

        def on_response(response):
            if response.url.startswith("http") and response.status >= 400:
                failed_requests.append(f"[{response.status}] {response.url}")

        page.on("response", on_response)
        page.goto(f"{base_url}/about.html", wait_until="networkidle")

        assert len(failed_requests) == 0, (
            f"Detected broken requests on about.html:\n" + "\n".join(failed_requests)
        )

