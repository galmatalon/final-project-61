import time

import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.your_cart_page import YourCartPage
from pages.your_information_page import YourInformationPage
from utils.config_reader import ConfigReader


# Ise this code in the conftest.py
# In case you want to open browser before each class
@pytest.fixture(scope="class", autouse=True)
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    #request.cls.page.goto("https://www.saucedemo.com/")
    url = ConfigReader.read_config("general", "url")
    request.cls.page.goto(url)
    request.cls.login_page = LoginPage(request.cls.page)
    request.cls.products_page = ProductsPage(request.cls.page)
    request.cls.your_cart_page = YourCartPage(request.cls.page)
    request.cls.your_information_page = YourInformationPage(request.cls.page)

    yield
    # request.cls.page.close()
    # browser.close()
    #time.sleep(100)