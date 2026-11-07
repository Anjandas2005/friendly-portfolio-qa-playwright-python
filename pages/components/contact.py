from playwright.sync_api import Page, Locator


class ContactComponent:
    """Get In Touch contact section."""

    def __init__(self, page: Page):
        self.page = page
        self.section: Locator = page.locator("section#contact")
        self.heading: Locator = page.locator("section#contact h2")
        self.description: Locator = page.locator("section#contact p")
        self.contact_links_container: Locator = page.locator("section#contact .contact-links")
        self.email_btn: Locator = page.locator(".contact-links a[href*='mail.google.com']")
        self.linkedin_btn: Locator = page.locator(".contact-links a[href*='linkedin.com']")
        self.github_btn: Locator = page.locator(".contact-links a[href*='github.com']")
        self.all_buttons: Locator = page.locator(".contact-links a")

