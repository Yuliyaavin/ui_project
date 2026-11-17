import re

from playwright.sync_api import expect


class TestContacts:
    def test_open_contacts_from_header(self, main_page, contacts_page):
        main_page.header_control.open_contacts()
        expect(contacts_page.page).to_have_url(contacts_page.full_url(contacts_page.PAGE_URL))

    def test_visible_elements(self, main_page, contacts_page):
        main_page.header_control.open_contacts()
        expect(contacts_page.page).to_have_title(re.compile("Контакты"))

        expect(contacts_page.map_locator).to_be_visible()
        expect(contacts_page.contact_msc_locator).to_be_visible()
        expect(contacts_page.contact_msc_locator).to_contain_text("Адрес:")
        expect(contacts_page.chat_locator).to_be_visible()
        expect(contacts_page.other_shops_locator).to_be_visible()
