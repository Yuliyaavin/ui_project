from pages.base_page import BasePage
from controls.header_control import HeaderControl
from controls.catalog_control import CatalogControl
from controls.search_control import SearchControl


class CommonPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_control = HeaderControl(self.page)
        self.catalog_control = CatalogControl(self.page)
        self.search_control = SearchControl(self.page)
