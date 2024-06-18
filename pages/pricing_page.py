from playwright.async_api import Page, expect

from locators.pricing_locators import PricingLocators
from pages.base_page import BasePage


class PricingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sub_menus = ["For Business", "For Individuals"]

        self.plans_map = {
            'business': [
                {'plan': 'Small Teams', 'expected_price': '$55', 'index': 1},
                {'plan': 'Enterprise', 'expected_price': 'Contact Sales', 'index': 2},
                {'plan': 'VILT', 'expected_price': 'Contact Sales', 'index': 3}],
            'individual': [
                {'plan': 'Monthly', 'expected_price': '$39', 'index': 1},
                {'plan': 'Yearly', 'expected_price': '$34', 'index': 2}
            ]}

    async def check_sub_menus(self):
        for elem in self.sub_menus:
            elem_loc = self.page.get_by_role("button", name=elem)
            await expect(elem_loc).to_be_visible()

    async def check_plans(self, submenu):
        plans = self.plans_map[submenu]
        for plan in plans:
            plan_loc = self.page.get_by_text(plan['plan'], exact=True)
            await expect(plan_loc).to_be_visible()

    async def check_pricing_plans(self, submenu):
        plans = self.plans_map[submenu]
        for plan in plans:
            price_loc = self.page.locator(f'xpath={PricingLocators.PLANS_GRID}/div[{plan['index']}]{PricingLocators.PRICE_PER_PLAN}')
            await expect(price_loc).to_be_visible()
            await expect(price_loc).to_have_text(plan['expected_price'])

    async def click_small_teams(self):
        await self.page.get_by_role("button", name="Start Now").click()
