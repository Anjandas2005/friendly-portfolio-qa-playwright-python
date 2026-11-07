import re
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.home_page import HomePage

scenarios("../../features/contact.feature")


@given("the user opens the portfolio homepage")
def open_homepage(home_page: HomePage):
    return home_page


@when('the user scrolls to the "Get In Touch" section')
def scroll_to_contact(home_page: HomePage):
    home_page.scroll_to(home_page.contact.section)


@then(parsers.parse('the email button should link to Gmail compose for "{email}"'))
def verify_email_btn(home_page: HomePage, email: str):
    expect(home_page.contact.email_btn).to_have_attribute("href", re.compile(re.escape(email)))


@then(parsers.parse('the LinkedIn button should link to "{url}"'))
def verify_linkedin_btn(home_page: HomePage, url: str):
    expect(home_page.contact.linkedin_btn).to_have_attribute("href", url)


@then(parsers.parse('the GitHub button should link to "{url}"'))
def verify_github_btn(home_page: HomePage, url: str):
    expect(home_page.contact.github_btn).to_have_attribute("href", url)


@then("all social links should open in a new tab")
def verify_new_tab(home_page: HomePage):
    for btn in home_page.contact.all_buttons.all():
        expect(btn).to_have_attribute("target", "_blank")

