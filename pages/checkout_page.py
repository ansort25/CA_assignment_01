import re

from playwright.async_api import Page, expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sign_up_form = ['First Name', 'Last Name', 'Your email address', 'Password']
        self.buy_form = ['Company name', 'First name', 'Last name', 'Email',
                         'Billing address', 'City', 'Post code', 'Region/State']
        self.payment = ['Credit Card', 'Paypal']

    async def check_sign_up_form(self):
        for elem in self.sign_up_form:
            elem_loc = self.page.get_by_placeholder(elem)
            await expect(elem_loc).to_be_visible()
        # not_robot_loc = self.page.frame_locator("iframe[name=\"a-nkfvx855i6e8\"]").get_by_label("I'm not a robot")
        # await expect(not_robot_loc).to_be_visible()

    async def check_buy_form(self):
        select_members_loc = self.page.locator(".Select__single-value > .sc-400bbb3f-0").first
        await expect(select_members_loc).to_be_visible()
        length_loc = self.page.get_by_text("Enterprise Yearly€295/month€")
        await expect(length_loc).to_be_visible()
        for elem in self.buy_form:
            elem_loc = self.page.get_by_placeholder(elem)
            await expect(elem_loc).to_be_visible()
        country_loc = (self.page.locator("form").get_by_label("Select")
                       .locator("div").filter(has_text="Select Country").nth(1))
        await expect(country_loc).to_be_visible()
        for elem in self.payment:
            elem_loc = self.page.locator("div").filter(has_text=re.compile(rf"^{elem}$")).first
            await expect(elem_loc).to_be_visible()

