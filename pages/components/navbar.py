from playwright.sync_api import Page, Locator


class NavbarComponent:
    """Header and navigation bar component present on all pages."""

    def __init__(self, page: Page):
        self.page = page
        self.header: Locator = page.locator("header")
        self.navbar: Locator = page.locator("nav.navbar")
        self.logo: Locator = page.locator("a.logo")
        self.nav_links_container: Locator = page.locator("ul.nav-links")
        self.all_nav_links: Locator = page.locator("ul.nav-links li a")
        self.home_link: Locator = page.locator("ul.nav-links li a[href='index.html']")
        self.about_link: Locator = page.locator("ul.nav-links li a[href='about.html']")
        self.projects_link: Locator = page.locator("ul.nav-links li a[href$='#projects']")
        self.contact_link: Locator = page.locator("ul.nav-links li a[href$='#contact']")

    def click_logo(self):
        self.logo.click()

    def click_home(self):
        self.home_link.first.click()

    def click_about(self):
        self.about_link.click()

    def click_projects(self):
        self.projects_link.click()

    def click_contact(self):
        self.contact_link.click()

