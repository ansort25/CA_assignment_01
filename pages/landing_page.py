from playwright.async_api import Page

from pages.base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search_box = page.get_by_placeholder("Search in our library...")

    async def navigate(self):
        await self.page.goto("https://cloudacademy.com", timeout=5000)
        await self.page.get_by_role("link", name="Allow selection").click()

    async def navigate_to(self, menu):
        await self.page.get_by_role("banner").get_by_role("link", name=menu).click()

    async def select_searchbox(self):
        await self.search_box.click()

    async def fill_searchbox(self, text):
        await self.search_box.fill(text)
