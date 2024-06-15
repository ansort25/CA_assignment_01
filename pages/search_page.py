from playwright.async_api import Page, expect

from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def wait_page_load(self, value):
        results_loc = self.page.get_by_text(f"results for \"{value}\"")
        await expect(results_loc).to_be_visible()
