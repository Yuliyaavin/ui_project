import re

from playwright.sync_api import expect


class TestMainPage:
    def test_open_delivery_from_header(self, main_page):
        main_page.header_control.open_delivery()
        expect(main_page.page).to_have_url(main_page.full_url("about/deliver/"))

    def test_logo_opens_main_page(self, main_page):
        main_page.header_control.open_about_company()
        expect(main_page.page).to_have_url(main_page.full_url("about/"))
        main_page.header_control.click_main_button()
        expect(main_page.page).to_have_url(main_page.full_url(main_page.PAGE_URL))
        expect(main_page.recommendation_title_locator).to_have_text("Рекомендованные издания")

    def test_visible_elements(self, main_page):
        expect(main_page.header_control.basket_locator).to_be_visible()
        expect(main_page.recommendation_title_locator).to_have_text("Рекомендованные издания")
        expect(main_page.product_card_locator).to_be_visible()
        expect(main_page.news_locator).to_be_visible()
        expect(main_page.catalog_control.title_catalog_locator).to_be_visible()

    def test_open_print_editions_from_catalog(self, main_page):
        main_page.catalog_control.open_print_editions()
        expect(main_page.page).to_have_title(re.compile("Подписка онлайн"))

    def test_open_editions_for_manager_from_catalog(self, main_page):
        main_page.catalog_control.open_editions_for_manager()
        expect(main_page.page).to_have_title(re.compile("Журналы для руководителя"))

    def test_open_editions_for_financier_from_catalog(self, main_page):
        main_page.catalog_control.open_editions_for_financier()
        expect(main_page.page).to_have_title(re.compile("Журналы для финансиста"))

    def test_open_prof_training_from_catalog(self, main_page):
        main_page.catalog_control.open_prof_training()
        expect(main_page.page).to_have_title(re.compile("Профессиональное обучение"))

    def test_open_training_for_manager_from_catalog(self, main_page):
        main_page.catalog_control.open_training_for_manager()
        expect(main_page.page).to_have_title(re.compile("Обучение для руководителя"))

    def test_open_training_for_financier_from_catalog(self, main_page):
        main_page.catalog_control.open_training_for_financier()
        expect(main_page.page).to_have_title(re.compile("Обучение для финансиста"))
