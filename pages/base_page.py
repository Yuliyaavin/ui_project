from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://action-press.ru"

    def __init__(self, page: Page):
        self.page = page

    def full_url(self, url):
        return f"{self.BASE_URL}/{url}"

    def open_page(self, url):
        self.page.goto(self.full_url(url), wait_until="domcontentloaded")

    def element(self, selector):
        return self.page.locator(selector)
