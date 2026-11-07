from playwright.sync_api import Page, Locator
from typing import List, Dict


class ProjectsComponent:
    """Featured Projects section."""

    def __init__(self, page: Page):
        self.page = page
        self.section: Locator = page.locator("section#projects")
        self.heading: Locator = page.locator("section#projects h2")
        self.project_grid: Locator = page.locator("section#projects .project-grid")
        self.cards: Locator = page.locator("section#projects .project-card")

    def count(self) -> int:
        return self.cards.count()

    def get_project_titles(self) -> List[str]:
        return [self.cards.nth(i).locator("h3").inner_text().strip() for i in range(self.count())]

    def get_project_data(self, index: int) -> Dict[str, object]:
        card = self.cards.nth(index)
        title = card.locator("h3").inner_text().strip()
        description = card.locator("p").inner_text().strip()
        tags = [tag.inner_text().strip() for tag in card.locator(".tech-stack span").all()]
        return {
            "title": title,
            "description": description,
            "tech_stack": tags
        }

