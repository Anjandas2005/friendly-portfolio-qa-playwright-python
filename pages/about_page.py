from playwright.sync_api import Page, Locator
from typing import List
from pages.base_page import BasePage
from pages.components.navbar import NavbarComponent
from pages.components.footer import FooterComponent


class AboutPage(BasePage):
    """Page object for the dedicated About Me / CV page (about.html)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.footer = FooterComponent(page)
        self.container: Locator = page.locator(".about-container")
        self.main_heading: Locator = page.locator(".about-container h2")
        self.profile_summary: Locator = page.locator(".profile-card-summary")
        self.resume_sections: Locator = page.locator(".resume-section")
        self.education_items: Locator = page.locator(".resume-section:has-text('Education') .resume-item")
        self.skills_categories: Locator = page.locator(".skills-grid .skill-category")
        self.achievements_items: Locator = page.locator(".achievements-list li")

    def load(self):
        """Navigate directly to the about page."""
        return self.navigate_to("/about.html")

    def get_education_count(self) -> int:
        return self.education_items.count()

    def get_skill_category_titles(self) -> List[str]:
        return [
            self.skills_categories.nth(i).locator("h4").inner_text().strip()
            for i in range(self.skills_categories.count())
        ]

