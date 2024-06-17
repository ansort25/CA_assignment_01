import re

from playwright.async_api import Page, expect

from locators.search_locators import SearchLocators
from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search_pattern = {
            'aws': 'aws|amazon',
            'gcp': 'google',
            'azure': 'azure|microsoft'
        }

    async def check_results_count_for_search(self, value):
        results_loc = self.page.get_by_text(f"results for \"{value}\"")
        await expect(results_loc).to_be_visible()

    async def wait_page_load(self, value):
        loc = self.page.locator(f'xpath={SearchLocators.SEARCH_RESULTS_GRIDBOX}')
        await expect(loc).to_be_visible()

    async def check_results_for_search(self, value):
        el = await self.page.locator(f'xpath={SearchLocators.SEARCH_RESULTS_GRIDBOX}/div').count()
        for i in range(1, el+1):
            elem_loc = self.page.locator(f'xpath={SearchLocators.SEARCH_RESULTS_GRIDBOX}/div[{i}]')
            await expect(elem_loc).to_contain_text(re.compile(self.search_pattern[value]), ignore_case=True)
