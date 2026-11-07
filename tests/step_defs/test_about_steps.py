from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.about_page import AboutPage

scenarios("../../features/about.feature")


@given("the user navigates directly to the About page")
def open_about(about_page: AboutPage):
    return about_page


@then(parsers.parse('the main heading should be "{heading}"'))
def verify_heading(about_page: AboutPage, heading: str):
    expect(about_page.main_heading).to_have_text(heading)


@then(parsers.parse("there should be {count:d} education history items listed"))
def verify_education_count(about_page: AboutPage, count: int):
    assert about_page.get_education_count() == count


@then(parsers.parse('the primary degree should be "{degree}"'))
def verify_primary_degree(about_page: AboutPage, degree: str):
    expect(about_page.education_items.first.locator("h4")).to_contain_text(degree)


@then(parsers.parse('the technical skills should include "{s1}", "{s2}", and "{s3}"'))
def verify_skills(about_page: AboutPage, s1: str, s2: str, s3: str):
    categories = about_page.get_skill_category_titles()
    assert categories == [s1, s2, s3]

