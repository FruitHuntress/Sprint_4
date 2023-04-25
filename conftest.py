import pytest
from selenium import webdriver
from pages.ya_samokat_main_page import YaSamokatMainPage
from pages.ya_samokat_main_page import LocatorYaSamokatMainPage
from pages.for_who_form_page import ForWhoFormPage
from pages.for_who_form_page import LocatorOrderForms

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def initiation(driver):
    ya_samokat_main_page = YaSamokatMainPage(driver)
    ya_samokat_main_page.go_to_site()
    ya_samokat_main_page.close_cookie_message()
    question_section = ya_samokat_main_page.find_element(LocatorYaSamokatMainPage.question_section, time=3)
    ya_samokat_main_page.scroll_down(driver, question_section)
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
    button = for_who_form_page.find_element(LocatorOrderForms.order_button_bottom, time=3)
    for_who_form_page.scroll_down(driver, button)
    for_who_form_page.click_order_button_bottom()
    return for_who_form_page
