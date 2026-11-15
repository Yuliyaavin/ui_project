import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance):
    # browser = playwright_instance.chromium.launch(headless=True)
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=1000)  # чтобы видеть шаги
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def page(context):
    return context.new_page()


@pytest.fixture
def main_page(page):
    main_page = MainPage(page)
    main_page.open_page(main_page.PAGE_URL)
    return main_page


@pytest.fixture
def about_page(page):
    about_page = AboutPage(page)
    about_page.open_page(about_page.PAGE_URL)
    return about_page


@pytest.fixture
def contacts_page(page):
    contacts_page = ContactsPage(page)
    contacts_page.open_page(contacts_page.PAGE_URL)
    return contacts_page


@pytest.fixture
def payment_page(page):
    payment_page = PaymentPage(page)
    payment_page.open_page(payment_page.PAGE_URL)
    return payment_page
