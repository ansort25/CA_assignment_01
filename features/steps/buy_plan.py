import re

from behave import given, when, then
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect

from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.pricing_page import PricingPage
from pages.checkout_page import CheckoutPage


@given('A user is logged in CloudAcademy')
@async_run_until_complete
async def login(context):
    _page = LandingPage(context.page)
    await _page.navigate_to('Login')
    await _page.url_contains('login')
    _page = LoginPage(context.page)
    await _page.login()
    await _page.url_contains('dashboard')
    await expect(_page.page).to_have_url(re.compile(".*dashboard"))


@when('The Start Now button is clicked on Small Teams plan')
@async_run_until_complete
async def click_on_start_now_plan(context):
    _page = PricingPage(context.page)
    await _page.click_small_teams()


@then('The Checkout page is opened')
@async_run_until_complete
async def land_on_checkout_page(context):
    _page = CheckoutPage(context.page)
    await _page.url_contains('checkout-beta')
    await expect(_page.page).to_have_url(re.compile(r".*checkout-beta/self-serve/(account|payment)/\?annually=1&seats=5"))


@then('A form to sign up to CloudAcademy is present')
@async_run_until_complete
async def land_on_sign_up(context):
    _page = CheckoutPage(context.page)
    await _page.page.locator("a").filter(has_text="Sign up with Google").is_visible()
    await _page.check_sign_up_form()


@then('A form to buy Small Teams plan is present')
@async_run_until_complete
async def land_on_buy_form(context):
    _page = CheckoutPage(context.page)
    await _page.page.get_by_text("Welcome Andrei, let’s set you").is_visible()
    await _page.check_buy_form()

