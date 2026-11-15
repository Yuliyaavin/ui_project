from pages.common_page import CommonPage


class PaymentPage(CommonPage):
    PAGE_URL = "about/payment/"

    # селекторы
    _title_payment_selector = ".static-page-h2"
    _non_cash_title_selector = "//h3[@class='payment__descr-title' and normalize-space()='Безналичный платеж']"
    _cash_title_selector = "//h3[@class='payment__descr-title' and normalize-space()='Наличный платеж']"
    _bank_card_title_selector = "//h3[@class='payment__descr-title' and normalize-space()='Оплата банковской картой']"
    _payment_system_labels_selector = "//*[contains(@class, 'payment__descr-img')]"
    _money_back_title_selector = "//*[contains(@class, 'title-bottom-refund')]"

    # локаторы
    @property
    def title_payment_locator(self):
        return self.element(self._title_payment_selector)

    @property
    def non_cash_title_locator(self):
        return self.element(self._non_cash_title_selector)

    @property
    def cash_title_locator(self):
        return self.element(self._cash_title_selector)

    @property
    def bank_card_title_locator(self):
        return self.element(self._bank_card_title_selector)

    @property
    def payment_system_labels_locator(self):
        return self.element(self._payment_system_labels_selector)

    @property
    def money_back_title_locator(self):
        return self.element(self._money_back_title_selector)
