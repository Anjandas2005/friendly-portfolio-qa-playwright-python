from playwright.sync_api import Page, Locator, Response
from typing import Optional


class BasePage:
    """Base class for all Page Objects providing shared helpers and assertions."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url_or_path: str = "/") -> Optional[Response]:
        """Navigate to a specified URL or relative path and wait until DOM is ready."""
        return self.page.goto(url_or_path, wait_until="domcontentloaded")

    def get_title(self) -> str:
        """Get the current document title."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Get the current browser URL."""
        return self.page.url

    def scroll_to(self, locator: Locator):
        """Scroll an element into the viewport."""
        locator.scroll_into_view_if_needed()

    def is_in_viewport(self, locator: Locator) -> bool:
        """Check if an element is currently within the visible viewport."""
        return locator.is_visible()

