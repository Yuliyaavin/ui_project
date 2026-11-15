from pages.common_page import CommonPage


class MainPage(CommonPage):
    PAGE_URL = ""

    # селекторы
    _recommendation_title_selector = ".title-text"
    _product_card_selector = ".card.flex-fill"
    _news_selector = "[data-qa-locator='mainBlockNews']"

    # локаторы
    @property
    def recommendation_title_locator(self):
        return self.element(self._recommendation_title_selector)

    @property
    def product_card_locator(self):
        return self.element(self._product_card_selector).first

    @property
    def news_locator(self):
        return self.element(self._news_selector)
