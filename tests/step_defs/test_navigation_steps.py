import re
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.home_page import HomePage

scenarios("../../features/navigation.feature")


@given("the user opens the portfolio homepage")
def open_homepage(home_page: HomePage):
    return home_page


@then(parsers.parse('the navigation bar should display logo "{logo_text}"'))
def verify_logo(home_page: HomePage, logo_text: str):
    expect(home_page.navbar.logo).to_have_text(logo_text)


@then(parsers.parse('the page title should be "{title}"'))
def verify_title(home_page: HomePage, title: str):
    expect(home_page.page).to_have_title(title)


@when('the user clicks on the "About" navigation link')
def click_about(home_page: HomePage):
    home_page.navbar.click_about()


@then(parsers.parse('the page title should change to "{title}"'))
def verify_about_title(home_page: HomePage, title: str):
    expect(home_page.page).to_have_title(title)


@then(parsers.parse('the current URL should include "{segment}"'))
def verify_url_segment(home_page: HomePage, segment: str):
    expect(home_page.page).to_have_url(re.compile(re.escape(segment) + r"$"))


@when('the user clicks on the "Home" navigation link')
def click_home(home_page: HomePage):
    home_page.navbar.click_home()


@then("the current URL should be the homepage")
def verify_home_url(home_page: HomePage):
    expect(home_page.page).to_have_url(re.compile(r"(index\.html|\.app/?)$"))

