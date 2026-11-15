import re

from playwright.sync_api import expect


class TestContacts:
    def test_visible_elements(self, contacts_page):
        expect(contacts_page.page).to_have_url(contacts_page.full_url(contacts_page.PAGE_URL))
        expect(contacts_page.page).to_have_title(re.compile("Контакты"))

        expect(contacts_page.map_locator).to_be_visible()
        expect(contacts_page.contact_msc_locator).to_be_visible()
        expect(contacts_page.contact_msc_locator).to_contain_text("Адрес:")
        expect(contacts_page.chat_locator).to_be_visible()
        expect(contacts_page.other_shops_locator).to_be_visible()

    def test_close_and_reopen_jivo_chat(self, contacts_page):
        expect(contacts_page.jivo_locator).to_be_visible(timeout=15000)
        contacts_page.close_jivo_chat()
        expect(contacts_page.jivo_locator).to_be_hidden()
        contacts_page.open_jivo_chat()
        expect(contacts_page.jivo_locator).to_be_visible()
