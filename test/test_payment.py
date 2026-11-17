import re

from playwright.sync_api import expect


class TestPayment:
    def test_open_payment_from_header(self, main_page, payment_page):
        main_page.header_control.open_payment()
        expect(payment_page.page).to_have_url(payment_page.full_url(payment_page.PAGE_URL))

    def test_visible_elements(self, main_page, payment_page):
        main_page.header_control.open_payment()
        expect(payment_page.page).to_have_title(re.compile("Способы оплаты"))

        expect(payment_page.title_payment_locator).to_have_text("Способы оплаты")
        expect(payment_page.non_cash_title_locator).to_be_visible()
        expect(payment_page.cash_title_locator).to_be_visible()
        expect(payment_page.bank_card_title_locator).to_be_visible()
        expect(payment_page.payment_system_labels_locator).to_be_visible()
        expect(payment_page.money_back_title_locator).to_be_visible()
