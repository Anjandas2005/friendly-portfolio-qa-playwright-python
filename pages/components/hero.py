from playwright.sync_api import Page, Locator


class HeroComponent:
    """Hero landing section of index.html."""

    def __init__(self, page: Page):
        self.page = page
        self.section: Locator = page.locator("section.hero")
        self.heading: Locator = page.locator(".hero-content h1")
        self.highlight_name: Locator = page.locator(".hero-content .highlight")
        self.subheading: Locator = page.locator(".hero-content p")
        self.view_work_btn: Locator = page.locator(".hero-btns a[href='#projects']")
        self.know_more_btn: Locator = page.locator(".hero-btns a[href='about.html']")

    def click_view_work(self):
        self.view_work_btn.click()

    def click_know_more(self):
        self.know_more_btn.click()

