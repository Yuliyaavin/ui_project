import re

from playwright.sync_api import expect


class TestSearch:
    def test_visible_elements(self, main_page):
        expect(main_page.page).to_have_title(re.compile("Подписка на журналы Актион"))
        expect(main_page.search_control.open_search_locator).to_be_visible()

    def test_open_search_popup(self, main_page):
        main_page.search_control.open_search()
        expect(main_page.search_control.search_input_locator).to_be_visible()

    def test_close_search_popup(self, main_page):
        main_page.search_control.open_search()
        expect(main_page.search_control.search_input_locator).to_be_visible()
        main_page.search_control.close_search_popup()
        expect(main_page.search_control.search_input_locator).to_be_hidden()

    def test_search_by_full_name(self, main_page):
        main_page.search_control.search('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
        expect(main_page.search_control.result_title_locator).to_have_text('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
