from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.components.navbar import NavbarComponent
from pages.components.hero import HeroComponent
from pages.components.projects import ProjectsComponent
from pages.components.contact import ContactComponent
from pages.components.footer import FooterComponent


class HomePage(BasePage):
    """Page object for the main portfolio landing page (index.html)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.hero = HeroComponent(page)
        self.projects = ProjectsComponent(page)
        self.contact = ContactComponent(page)
        self.footer = FooterComponent(page)

    def load(self):
        """Navigate to the home page."""
        return self.navigate_to("/")

