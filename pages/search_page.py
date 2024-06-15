from playwright.async_api import Page

from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def wait_page_load(self, value):
        await self.page.get_by_text(f"results for \"{value}\"").is_visible(timeout=5000)
