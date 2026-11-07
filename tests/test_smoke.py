import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
class TestSmoke:
    """Smoke test suite to verify basic application health, deployment, and assets."""

    def test_homepage_deployment_and_title(self, page: Page, base_url: str):
        """TC-SMK-01: Verify homepage returns HTTP 200 and expected title."""
        response = page.goto(base_url, wait_until="domcontentloaded")
        assert response is not None, "Did not receive an HTTP response"
        assert response.status == 200, f"Expected HTTP 200, but received {response.status}"

        # Assert no Vercel error page
        content = page.content()
        assert "DEPLOYMENT_NOT_FOUND" not in content, "Vercel returned DEPLOYMENT_NOT_FOUND"

        # Assert page title
        expect(page).to_have_title("Oyendri Sana | Curriculum Vitae")

    def test_about_page_deployment_and_title(self, page: Page, base_url: str):
        """TC-SMK-02: Verify about page returns HTTP 200 and expected title."""
        response = page.goto(f"{base_url}/about.html", wait_until="domcontentloaded")
        assert response is not None, "Did not receive an HTTP response"
        assert response.status == 200, f"Expected HTTP 200, but received {response.status}"
        expect(page).to_have_title("About Me | Oyendri Sana")

    def test_critical_meta_and_css_loaded(self, page: Page, base_url: str):
        """TC-SMK-03: Verify critical responsive meta tag and style.css link."""
        page.goto(base_url, wait_until="domcontentloaded")
        viewport_meta = page.locator("meta[name='viewport']")
        expect(viewport_meta).to_have_attribute("content", "width=device-width, initial-scale=1.0")

        stylesheet = page.locator("link[rel='stylesheet'][href='style.css']")
        expect(stylesheet).to_have_count(1)
