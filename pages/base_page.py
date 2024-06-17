from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def title_contains(self, text):
        title = await self.page.title()
        if title.find(text) == -1:
            return False
        else:
            return True

    async def url_contains(self, text):
        if self.page.url.find(text) == -1:
            return False
        else:
            return True

    async def press_key(self, key):
        await self.page.keyboard.press(key)
