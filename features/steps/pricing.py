import re

from behave import when, then
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect

from pages.landing_page import LandingPage
from pages.pricing_page import PricingPage


@when('The pricing button menu is clicked')
@async_run_until_complete
async def access_pricing_page(context):
    page = LandingPage(context.page)
    await page.navigate_to("Pricing")


@when('The "{submenu}" button is clicked')
@async_run_until_complete
async def click_submenu(context, submenu):
    page = PricingPage(context.page)
    await page.page.get_by_role("button", name=submenu).click()


@then('The pricing page for "{submenu}" is opened')
@async_run_until_complete
async def landed_on_selected_plans(context, submenu):
    page = PricingPage(context.page)
    await page.url_contains('pricing')
    if submenu != 'business':
        await expect(page.page).to_have_url(re.compile(f".*{submenu}"))


@then('Buttons for business and individuals are present')
@async_run_until_complete
async def sub_pricing_buttons_are_present(context):
    page = PricingPage(context.page)
    await page.check_sub_menus()


@then('Plans for "{submenu}" are visible')
@async_run_until_complete
async def plans_are_present(context, submenu):
    page = PricingPage(context.page)
    await page.check_plans(submenu)


@then('The pricing for each "{submenu}" plan is visible')
@async_run_until_complete
async def plans_are_present(context, submenu):
    page = PricingPage(context.page)
    await page.check_pricing_plans(submenu)
