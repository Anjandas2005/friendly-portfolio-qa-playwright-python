import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.projects
class TestProjects:
    """Featured projects section verification tests."""

    def test_projects_section_heading_and_count(self, home_page: HomePage):
        """TC-PRJ-01: Verify section heading and total project cards."""
        expect(home_page.projects.heading).to_have_text("Featured Projects")
        assert home_page.projects.count() == 3, f"Expected 3 projects, got {home_page.projects.count()}"

    def test_project_titles(self, home_page: HomePage):
        """TC-PRJ-02: Verify project card titles."""
        expected_titles = [
            "Netflix Clone",
            "Energy Bill Optimization",
            "Intelligent Health Assistant(in progress)",
        ]
        actual_titles = home_page.projects.get_project_titles()
        assert actual_titles == expected_titles, f"Project titles mismatch: {actual_titles}"

    def test_project_tech_stacks(self, home_page: HomePage):
        """TC-PRJ-03: Verify tech stack tags for each project card."""
        expected_tags = {
            0: ["HTML", "CSS", "JavaScript"],
            1: ["Utility Management", "Dashboard"],
            2: ["Data Processing", "Web UI"],
        }
        for index, tags in expected_tags.items():
            card_data = home_page.projects.get_project_data(index)
            assert card_data["tech_stack"] == tags, (
                f"Project {card_data['title']} tags mismatch: {card_data['tech_stack']} vs {tags}"
            )
            assert len(card_data["description"]) > 20, (
                f"Project {card_data['title']} description too short or empty"
            )

