from playwright.sync_api import Page


class HeaderControl:
    def __init__(self, page: Page):
        self.page = page


    # селекторы
    _about_company_selector = "//a[@data-qa-locator='desctop_top_menu_item' and normalize-space()='О нас']"
    _contacts_selector = "//a[@data-qa-locator='desctop_top_menu_item' and normalize-space()='Контакты']"
    _payment_selector = "//a[@data-qa-locator='desctop_top_menu_item' and normalize-space()='Способы оплаты']"
    _delivery_selector = "//a[@data-qa-locator='desctop_top_menu_item' and normalize-space()='Способы доставки']"
    _main_button_selector = "[alt='Актион-пресс']"
    _basket_selector = ".basket-item"

    # локаторы
    @property
    def about_company_locator(self):
        return self.page.locator(self._about_company_selector)

    @property
    def contacts_locator(self):
        return self.page.locator(self._contacts_selector)

    @property
    def payment_locator(self):
        return self.page.locator(self._payment_selector)

    @property
    def delivery_locator(self):
        return self.page.locator(self._delivery_selector)

    @property
    def main_button_locator(self):
        return self.page.locator(self._main_button_selector)

    @property
    def basket_locator(self):
        return self.page.locator(self._basket_selector)

    # методы
    def open_about_company(self):
        self.about_company_locator.click()

    def open_contacts(self):
        self.contacts_locator.click()

    def open_payment(self):
        self.payment_locator.click()

    def open_delivery(self):
        self.delivery_locator.click()

    def click_main_button(self):
        self.main_button_locator.click()
