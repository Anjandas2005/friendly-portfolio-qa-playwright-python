from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage

scenarios("../../features/projects.feature")


@given("the user opens the portfolio homepage")
def open_homepage(home_page: HomePage):
    return home_page


@when('the user views the "Featured Projects" section')
def view_projects(home_page: HomePage):
    home_page.scroll_to(home_page.projects.section)


@then(parsers.parse("there should be {count:d} project cards displayed"))
def verify_cards_count(home_page: HomePage, count: int):
    assert home_page.projects.count() == count


@then(parsers.parse('the projects should include "{p1}", "{p2}", and "{p3}"'))
def verify_project_titles(home_page: HomePage, p1: str, p2: str, p3: str):
    titles = home_page.projects.get_project_titles()
    assert titles == [p1, p2, p3]

