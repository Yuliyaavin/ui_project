from playwright.sync_api import Page


class SearchControl:
    def __init__(self, page: Page):
        self.page = page


    # селекторы
    _open_search_selector = "//nav[contains(@class, 'navbar-sub-header')]//input[@placeholder='Поиск']"
    _search_input_selector = "input[placeholder='Что вы хотите найти?']"
    _search_button_selector = ".l-ss-c-search-input-action-search"
    _close_search_selector = ".l-ss-c-search-popup-close-button"
    _result_title_selector = ".l-ss-c-offer-info-title span"

    # локаторы
    @property
    def open_search_locator(self):
        return self.page.locator(self._open_search_selector)

    @property
    def search_input_locator(self):
        return self.page.locator(self._search_input_selector)

    @property
    def search_button_locator(self):
        return self.page.locator(self._search_button_selector)

    @property
    def close_search_locator(self):
        return self.page.locator(self._close_search_selector)

    @property
    def result_title_locator(self):
        return self.page.locator(self._result_title_selector)

    # методы
    def open_search(self):
        self.open_search_locator.click()

    def fill_search_input(self, text):
        self.search_input_locator.fill(text)

    def start_search(self):
        self.search_button_locator.click()

    def close_search_popup(self):
        self.close_search_locator.click()

    # комбинированный метод
    def search(self, text):
        self.open_search()
        self.fill_search_input(text)
        self.start_search()
