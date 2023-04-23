import pytest
from selenium import webdriver
from pages.ya_samokat_main_page import YaSamokatMainPage
from pages.for_who_form_page import ForWhoFormPage


@pytest.fixture
def driver():
    # options = Options()
    # options.add_argument('--window-size=1200,1200')
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def initiation(driver):
    ya_samokat_main_page = YaSamokatMainPage(driver)
    ya_samokat_main_page.go_to_site()
    ya_samokat_main_page.close_cookie_message()
    ya_samokat_main_page.scroll_down(driver)
    return ya_samokat_main_page


@pytest.fixture
def form_opened_by_top_order_button(driver):
    for_who_form_page = ForWhoFormPage(driver)
    for_who_form_page.go_to_site()
    for_who_form_page.click_order_button_top()

    return for_who_form_page


@pytest.fixture
def form_opened_by_bottom_order_button(driver):
    for_who_form_page = ForWhoFormPage(driver)
    for_who_form_page.go_to_site()
    for_who_form_page.scroll_down(driver)
    for_who_form_page.click_order_button_bottom()
    return for_who_form_page
