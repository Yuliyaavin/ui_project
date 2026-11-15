from playwright.sync_api import Page


class CatalogControl:
    def __init__(self, page: Page):
        self.page = page


    # селекторы
    _title_catalog_selector = "//span[text()='Каталог']"
    _print_editions_selector = "//*[@data-qa-locator='leftMenuEshop']//a[text()='Печатные и электронные издания']"
    _editions_for_manager_selector = "//*[@data-qa-locator='leftMenuEshop']//a[contains(@href, 'izdaniya-dlya-rukovoditelya')]"
    _editions_for_financier_selector = "//*[@data-qa-locator='leftMenuEshop']//a[contains(@href, 'izdaniya-dlya-finansista')]"
    _prof_training_selector = "//*[@data-qa-locator='leftMenuEshop']//a[normalize-space()='Профессиональное обучение']"
    _training_for_manager_selector = "//*[@data-qa-locator='leftMenuEshop']//a[contains(@href, '-/dlya-rukovoditelya')]"
    _training_for_financier_selector = "//*[@data-qa-locator='leftMenuEshop']//a[contains(@href, '-/dlya-finansista')]"

    # локаторы
    # для теста видимости заголовка
    @property
    def title_catalog_locator(self):
        return self.page.locator(self._title_catalog_selector)

    @property
    def print_editions_locator(self):
        return self.page.locator(self._print_editions_selector)

    @property
    def editions_for_manager_locator(self):
        return self.page.locator(self._editions_for_manager_selector)

    @property
    def editions_for_financier_locator(self):
        return self.page.locator(self._editions_for_financier_selector)

    @property
    def prof_training_locator(self):
        return self.page.locator(self._prof_training_selector)

    @property
    def training_for_manager_locator(self):
        return self.page.locator(self._training_for_manager_selector)

    @property
    def training_for_financier_locator(self):
        return self.page.locator(self._training_for_financier_selector)

    # методы
    def open_print_editions(self):
        self.print_editions_locator.click()

    def open_editions_for_manager(self):
        self.editions_for_manager_locator.click()

    def open_editions_for_financier(self):
        self.editions_for_financier_locator.click()

    def open_prof_training(self):
        self.prof_training_locator.click()

    def open_training_for_manager(self):
        self.training_for_manager_locator.click()

    def open_training_for_financier(self):
        self.training_for_financier_locator.click()
