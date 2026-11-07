import datetime
from pathlib import Path
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.about_page import AboutPage


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configures pytest-html with a timestamped filename and purges older reports."""
    # Run only on the controller process (prevents duplicate execution on xdist workers)
    if not hasattr(config, "workerinput"):
        reports_dir = Path("reports")
        reports_dir.mkdir(parents=True, exist_ok=True)

        # Automatically purge older HTML reports so only the fresh run is retained
        for old_report in reports_dir.glob("*.html"):
            try:
                old_report.unlink()
            except OSError:
                pass

        # Generate unique date and time stamp for current run
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_path = reports_dir / f"report_{timestamp}.html"

        # Apply configuration to pytest-html
        config.option.htmlpath = str(report_path)
        config.option.self_contained_html = True


def pytest_html_report_title(report):
    """Sets a descriptive header title in the generated HTML report."""
    report.title = "Oyendri Sana Portfolio - Test Execution Report"


@pytest.fixture
def home_page(page: Page, base_url: str) -> HomePage:
    """Fixture providing an initialized and loaded HomePage instance."""
    hp = HomePage(page)
    hp.load()
    return hp


@pytest.fixture
def about_page(page: Page, base_url: str) -> AboutPage:
    """Fixture providing an initialized and loaded AboutPage instance."""
    ap = AboutPage(page)
    ap.load()
    return ap


@pytest.fixture(autouse=True)
def capture_console_errors(page: Page):
    """Monitors console errors and uncaught exceptions across all test runs."""
    console_errors = []

    def on_console(msg):
        if msg.type == "error":
            console_errors.append(f"Console [ERROR]: {msg.text}")

    def on_page_error(exc):
        console_errors.append(f"Page [EXCEPTION]: {exc}")

    page.on("console", on_console)
    page.on("pageerror", on_page_error)

    yield

    assert len(console_errors) == 0, (
        f"Detected {len(console_errors)} unexpected console/page error(s):\n"
        + "\n".join(console_errors)
    )
