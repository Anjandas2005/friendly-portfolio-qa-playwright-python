from playwright.sync_api import Page, Locator


class FooterComponent:
    """Page footer with copyright information."""

    def __init__(self, page: Page):
        self.page = page
        self.footer: Locator = page.locator("footer")
        self.copyright_text: Locator = page.locator("footer p")

