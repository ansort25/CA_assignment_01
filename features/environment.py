from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright


@fixture
async def browser_chrome(context):
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, slow_mo=500, channel="chrome")
    context.page = await browser.new_page()
    context.browser = browser
    return context.page


@fixture
async def close_context(context):
    await context.browser.close()


@async_run_until_complete
async def before_scenario(context, scenario):
    await use_fixture(browser_chrome, context)


@async_run_until_complete
async def after_scenario(context, scenario):
    await use_fixture(close_context, context)
