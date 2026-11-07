import re
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.hero
class TestHero:
    """Hero section and call-to-action button tests."""

    def test_hero_text_content(self, home_page: HomePage):
        """TC-HER-01: Verify hero heading, highlighted name, and bio paragraph."""
        expect(home_page.hero.section).to_be_visible()
        expect(home_page.hero.heading).to_contain_text("Hi, I'm")
        expect(home_page.hero.highlight_name).to_have_text("Oyendri Sana")
        expect(home_page.hero.subheading).to_contain_text(
            "B.Tech CSE Student & Web Developer passionate about building efficient, user-friendly software."
        )

    def test_hero_cta_view_work_scrolls_to_projects(self, home_page: HomePage):
        """TC-HER-02: Clicking 'View My Work' brings projects section into view."""
        expect(home_page.hero.view_work_btn).to_be_visible()
        expect(home_page.hero.view_work_btn).to_have_text("View My Work")
        home_page.hero.click_view_work()

        expect(home_page.projects.section).to_be_in_viewport()

    def test_hero_cta_know_more_navigates_to_about(self, home_page: HomePage):
        """TC-HER-03: Clicking 'Know More About Me' navigates to about.html."""
        expect(home_page.hero.know_more_btn).to_be_visible()
        expect(home_page.hero.know_more_btn).to_have_text("Know More About Me")
        home_page.hero.click_know_more()

        expect(home_page.page).to_have_url(re.compile(r"about\.html$"))
        expect(home_page.page).to_have_title("About Me | Oyendri Sana")

