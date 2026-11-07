import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.contact
class TestContact:
    """Contact section and communication channels verification."""

    def test_contact_heading_and_buttons(self, home_page: HomePage):
        """TC-CNT-01: Verify section header and communication buttons."""
        expect(home_page.contact.section).to_be_visible()
        expect(home_page.contact.heading).to_have_text("Get In Touch")
        expect(home_page.contact.all_buttons).to_have_count(3)

        button_texts = [btn.inner_text().strip() for btn in home_page.contact.all_buttons.all()]
        assert button_texts == ["Email Me", "LinkedIn", "GitHub"]

    def test_contact_links_targets_and_security(self, home_page: HomePage):
        """TC-CNT-02: Ensure external links open in new tab (target=_blank)."""
        for btn in home_page.contact.all_buttons.all():
            expect(btn).to_have_attribute("target", "_blank")

    def test_contact_email_link_destination(self, home_page: HomePage):
        """TC-CNT-03: Verify email button opens Gmail compose with target address."""
        expect(home_page.contact.email_btn).to_have_attribute(
            "href", "https://mail.google.com/mail/?view=cm&fs=1&to=oyendri.sana.in@gmail.com"
        )

    def test_contact_social_destinations(self, home_page: HomePage):
        """TC-CNT-04: Verify LinkedIn and GitHub URLs."""
        expect(home_page.contact.linkedin_btn).to_have_attribute(
            "href", "https://linkedin.com/in/oyendri-sana-14b73035a"
        )
        expect(home_page.contact.github_btn).to_have_attribute(
            "href", "https://github.com/oyendrisana"
        )

