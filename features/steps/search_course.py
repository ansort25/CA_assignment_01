import re

from behave import given, when, then
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect

from pages.landing_page import LandingPage
from pages.search_page import SearchPage


@given('Cloudacademy page is accessed')
@async_run_until_complete
async def navigate_to_landing_page(context):
    page = LandingPage(context.page)
    await page.navigate()


@when('Search toolbar is clicked')
@async_run_until_complete
async def click_on_search_box(context):
    page = LandingPage(context.page)
    await page.select_searchbox()


@when('The search box is filled with the value "{value}"')
@async_run_until_complete
async def fill_search_box(context, value):
    page = LandingPage(context.page)
    await page.fill_searchbox(value)


@when('Enter key is pressed')
@async_run_until_complete
async def press_enter(context):
    page = LandingPage(context.page)
    await page.press_key('Enter')


@then('The search page is opened')
@async_run_until_complete
async def check_search_page(context):
    page = SearchPage(context.page)
    await page.url_contains('search')
    await expect(page.page).to_have_url(re.compile(".*search"))


@then('A list of "{value}" courses is shown')
@async_run_until_complete
async def check_courses_on_search_page(context, value):
    page = SearchPage(context.page)
    await expect(page.page).to_have_url(re.compile(f".*{value}"))
    await page.check_results_count_for_search(value)
    await page.wait_page_load(value)
    await page.check_results_for_search(value)

