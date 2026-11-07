import re
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.about_page import AboutPage


@pytest.mark.navigation
class TestNavigation:
    """Navigation test suite for header, links, and cross-page routing."""

    def test_navbar_structure_and_logo(self, home_page: HomePage):
        """TC-NAV-01: Verify navigation header, branding logo, and links presence."""
        expect(home_page.navbar.header).to_be_visible()
        expect(home_page.navbar.logo).to_have_text("Oyendri Sana")
        expect(home_page.navbar.all_nav_links).to_have_count(4)

        labels = [link.inner_text().strip() for link in home_page.navbar.all_nav_links.all()]
        assert labels == ["Home", "About", "Projects", "Contact"]

    def test_navigate_to_about_page_via_navbar(self, home_page: HomePage):
        """TC-NAV-02: Clicking About link in header navigates to about.html."""
        home_page.navbar.click_about()
        expect(home_page.page).to_have_url(re.compile(r"about\.html$"))
        expect(home_page.page).to_have_title("About Me | Oyendri Sana")

        # Verify active link styling on about page
        active_link = home_page.page.locator("ul.nav-links li a.active")
        expect(active_link).to_have_text("About")

    def test_navigate_from_about_to_home(self, about_page: AboutPage):
        """TC-NAV-03: Clicking Home link on about page returns to index.html."""
        about_page.navbar.click_home()
        expect(about_page.page).to_have_url(re.compile(r"(index\.html|\.app/?)$"))
        expect(about_page.page).to_have_title("Oyendri Sana | Curriculum Vitae")

    def test_anchor_links_navigate_to_sections(self, home_page: HomePage):
        """TC-NAV-04: Clicking Projects & Contact anchors navigates to sections."""
        home_page.navbar.click_projects()
        expect(home_page.projects.section).to_be_in_viewport()

        home_page.navbar.click_contact()
        expect(home_page.contact.section).to_be_in_viewport()

