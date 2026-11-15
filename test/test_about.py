import re

from playwright.sync_api import expect


class TestAbout:
    def test_visible_elements(self, about_page):
        expect(about_page.page).to_have_url(about_page.full_url(about_page.PAGE_URL))
        expect(about_page.page).to_have_title(re.compile("О нас"))

        expect(about_page.page_title_locator).to_have_text("Официальный интернет-магазин группы Актион")
        expect(about_page.banner_image_locator).to_be_visible()
        expect(about_page.trust_title_locator).to_be_visible()
        expect(about_page.trust_list_locator).to_be_visible()
        expect(about_page.quality_title_locator).to_be_visible()
