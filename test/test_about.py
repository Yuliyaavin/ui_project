import re

from playwright.sync_api import expect


class TestAbout:
    def test_open_about_from_header(self, main_page, about_page):
        main_page.header_control.open_about_company()
        expect(about_page.page).to_have_url(about_page.full_url(about_page.PAGE_URL))

    def test_visible_elements(self, main_page, about_page):
        main_page.header_control.open_about_company()
        expect(about_page.page).to_have_title(re.compile("О нас"))

        expect(about_page.page_title_locator).to_have_text("Официальный интернет-магазин группы Актион")
        expect(about_page.banner_image_locator).to_be_visible()
        expect(about_page.trust_title_locator).to_be_visible()
        expect(about_page.trust_list_locator).to_be_visible()
        expect(about_page.quality_title_locator).to_be_visible()
