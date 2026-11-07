import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


@pytest.mark.responsive
class TestResponsive:
    """Responsive design verification across desktop, tablet, and mobile viewports."""

    @pytest.mark.parametrize(
        "viewport_size,device_name",
        [
            ({"width": 1920, "height": 1080}, "Desktop Full HD"),
            ({"width": 1366, "height": 768}, "Standard Laptop"),
            ({"width": 768, "height": 1024}, "Tablet iPad"),
            ({"width": 390, "height": 844}, "Mobile iPhone 13/14"),
            ({"width": 375, "height": 667}, "Mobile iPhone SE"),
        ],
    )
    def test_no_horizontal_overflow_across_viewports(
        self, page: Page, base_url: str, viewport_size: dict, device_name: str
    ):
        """TC-RSP-01: Ensure no accidental horizontal scrolling/overflow occurs."""
        page.set_viewport_size(viewport_size)
        page.goto(base_url, wait_until="domcontentloaded")

        # Evaluate if scrollWidth exceeds innerWidth
        has_horizontal_overflow = page.evaluate(
            "() => document.documentElement.scrollWidth > window.innerWidth"
        )
        assert not has_horizontal_overflow, (
            f"Horizontal overflow detected on device: {device_name} ({viewport_size['width']}x{viewport_size['height']})"
        )

    def test_mobile_project_cards_stack_cleanly(self, page: Page, base_url: str):
        """TC-RSP-02: Project cards adapt and remain readable on mobile screens."""
        page.set_viewport_size({"width": 390, "height": 844})
        hp = HomePage(page)
        hp.load()

        for card in hp.projects.cards.all():
            expect(card).to_be_visible()
            box = card.bounding_box()
            assert box is not None
            assert box["width"] > 250, "Project card width is too constrained on mobile"

