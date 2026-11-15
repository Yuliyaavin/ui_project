from pages.common_page import CommonPage


class AboutPage(CommonPage):
    PAGE_URL = "about/"

    # селекторы
    _page_title_selector = ".static-page-h2"
    _banner_image_selector = ".banner .banner__image_content"
    _trust_title_selector = "//h2[normalize-space()='Почему нам доверяют']"
    _trust_list_selector = ".content .content__list"
    _quality_title_selector = "//h2[normalize-space()='Гарантии качества']"

    # локаторы
    @property
    def page_title_locator(self):
        return self.element(self._page_title_selector)

    @property
    def banner_image_locator(self):
        return self.element(self._banner_image_selector)

    @property
    def trust_title_locator(self):
        return self.element(self._trust_title_selector)

    @property
    def trust_list_locator(self):
        return self.element(self._trust_list_selector)

    @property
    def quality_title_locator(self):
        return self.element(self._quality_title_selector)
