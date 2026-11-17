from pages.common_page import CommonPage


class ContactsPage(CommonPage):
    PAGE_URL = "about/contacts/"

    # селекторы
    _map_selector = ".ymaps3--main-engine-container"
    _contact_msc_selector = "//*[text()='Москва']/.."
    _chat_selector = "[id='aboutChat']"
    _other_shops_selector = "//*[text()='Другие интернет-магазины группы Актион']/.."

    # локаторы
    @property
    def map_locator(self):
        return self.element(self._map_selector)

    @property
    def contact_msc_locator(self):
        return self.element(self._contact_msc_selector)

    @property
    def chat_locator(self):
        return self.element(self._chat_selector)

    @property
    def other_shops_locator(self):
        return self.element(self._other_shops_selector)
