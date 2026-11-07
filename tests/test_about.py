import pytest
from playwright.sync_api import expect
from pages.about_page import AboutPage


@pytest.mark.about
class TestAbout:
    """Dedicated About Me (about.html) verification suite."""

    def test_about_page_headings_and_structure(self, about_page: AboutPage):
        """TC-ABT-01: Verify main title, summary card, and resume sections."""
        expect(about_page.main_heading).to_have_text("About Me")
        expect(about_page.profile_summary).to_be_visible()
        expect(about_page.profile_summary.locator("h3")).to_have_text("Professional Profile")

    def test_education_entries(self, about_page: AboutPage):
        """TC-ABT-02: Verify education timeline items and credentials."""
        assert about_page.get_education_count() == 3, "Expected 3 education timeline items"
        btech_item = about_page.education_items.first
        expect(btech_item.locator("h4")).to_contain_text("B.Tech in Computer Science Engineering")
        expect(btech_item.locator(".institution")).to_have_text(
            "Gargi Memorial Institute of Technology, Kolkata"
        )
        expect(btech_item.locator(".meta")).to_contain_text("2023 – 2027")

    def test_technical_skills_categories(self, about_page: AboutPage):
        """TC-ABT-03: Verify technical skills categories."""
        expected_categories = [
            "Programming Languages",
            "Web & Frontend",
            "Core CS Concepts",
        ]
        actual_categories = about_page.get_skill_category_titles()
        assert actual_categories == expected_categories

    def test_certifications_and_achievements(self, about_page: AboutPage):
        """TC-ABT-04: Verify certifications and pitch competition accomplishments."""
        expect(about_page.achievements_items).to_have_count(2)
        first_achievement = about_page.achievements_items.nth(0)
        expect(first_achievement).to_contain_text("Ardent Computech Pvt. Ltd.")

        second_achievement = about_page.achievements_items.nth(1)
        expect(second_achievement).to_contain_text("TiE Kolkata")

