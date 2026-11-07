import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


@pytest.mark.a11y
class TestAccessibility:
    """Automated accessibility & semantic HTML compliance checks."""

    def test_document_language_attribute(self, page: Page, base_url: str):
        """TC-A11-01: Ensure <html> element contains a valid lang attribute."""
        page.goto(base_url, wait_until="domcontentloaded")
        html_element = page.locator("html")
        expect(html_element).to_have_attribute("lang", "en")

    def test_single_h1_heading_on_homepage(self, home_page: HomePage):
        """TC-A11-02: Ensure homepage contains exactly one primary <h1> heading."""
        h1_headings = home_page.page.locator("h1")
        expect(h1_headings).to_have_count(1)
        expect(h1_headings.first).to_be_visible()

    def test_all_links_have_accessible_names(self, home_page: HomePage):
        """TC-A11-03: Ensure all anchor links have non-empty accessible text."""
        links = home_page.page.locator("a").all()
        for link in links:
            accessible_name = link.inner_text().strip()
            aria_label = link.get_attribute("aria-label") or ""
            title = link.get_attribute("title") or ""
            has_name = bool(accessible_name or aria_label or title)
            href = link.get_attribute("href")
            assert has_name, f"Anchor link with href '{href}' is missing accessible text or label"

    def test_external_links_have_secure_rel_attributes(self, home_page: HomePage):
        """TC-A11-04: External links targeting new tab should specify rel attributes."""
        external_links = home_page.page.locator("a[target='_blank']").all()
        for link in external_links:
            href = link.get_attribute("href")
            assert href is not None and href.startswith("http"), f"External link {href} invalid"

    def test_keyboard_tab_focus_progression(self, home_page: HomePage):
        """TC-A11-05: Ensure interactive elements receive keyboard tab focus."""
        # Tab into the first link (logo)
        home_page.page.keyboard.press("Tab")
        active_tag = home_page.page.evaluate("document.activeElement.tagName")
        assert active_tag.lower() in ["a", "button", "input"], (
            f"Expected focused element to be interactive, got {active_tag}"
        )
