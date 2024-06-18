from playwright.async_api import Page

from pages.base_page import BasePage
from features.steps import secrets


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def login(self):
        await self.page.get_by_placeholder("Email").is_visible()
        await self.page.get_by_placeholder("Email").type(secrets.MAIL)
        await self.page.get_by_placeholder("Password").type(secrets.PSW)
        # await self.page.frame_locator("iframe[name=\"a-wj4ppzufzzuq\"]").get_by_label("I'm not a robot").click()
        await self.page.get_by_label("Log in with email button,").click()
