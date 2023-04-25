import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorYaSamokatMainPage:
    cookie_button = [By.XPATH, "//button[@id='rcc-confirm-button']"]
    question_section = [By.XPATH, "//div[contains(text(),'Вопросы о важном')]"]
    question_price = [By.ID, 'accordion__heading-0']
    question_quantity = [By.ID, 'accordion__heading-1']
    question_time = [By.ID, 'accordion__heading-2']
    question_order_today = [By.ID, 'accordion__heading-3']
    question_prolongation = [By.ID, 'accordion__heading-4']
    question_charger = [By.ID, 'accordion__heading-5']
    question_cancellation = [By.ID, 'accordion__heading-6']
    question_long_distance = [By.ID, 'accordion__heading-7']

    question_price_accordion_panel = [By.ID, "accordion__panel-0"]
    question_quantity_accordion_panel = [By.ID, "accordion__panel-1"]
    question_time_accordion_panel = [By.ID, "accordion__panel-2"]
    question_order_today_accordion_panel = [By.ID, "accordion__panel-3"]
    question_prolongation_accordion_panel = [By.ID, "accordion__panel-4"]
    question_charger_accordion_panel = [By.ID, "accordion__panel-5"]
    question_cancellation_accordion_panel = [By.ID, "accordion__panel-6"]
    question_long_distance_accordion_panel = [By.ID, "accordion__panel-7"]

    main_title = [By.XPATH, ".//div[@class='Home_Header__iJKdX']"]


class YaSamokatMainPage(BasePage):
    @allure.step('close cookie message')
    def close_cookie_message(self):
        cookie_button = self.find_element(LocatorYaSamokatMainPage.cookie_button, time=3)
        cookie_button.click()

    def click_question_element(self, locator):
        question_title = self.find_element(locator, time=3)
        question_title.click()

    def get_question_panel_text(self, locator):
        panel = self.find_element(locator, time=3)
        return panel.text

    def get_main_title(self):
        main_title = self.find_element(LocatorYaSamokatMainPage.main_title, time=3)
        return main_title.text


