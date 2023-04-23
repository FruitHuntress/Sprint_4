from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



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
    def close_cookie_message(self):
        cookie_button = self.find_element(LocatorYaSamokatMainPage.cookie_button, time=3)
        cookie_button.click()

    def scroll_down(self, driver):
        question_section_title = self.find_element(LocatorYaSamokatMainPage.question_section, time=3)
        driver.execute_script("arguments[0].scrollIntoView();", question_section_title)
        time.sleep(0.2)

    def click_question_price(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_price, time=3)
        question_title.click()

    def click_question_quantity(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_quantity, time=3)
        question_title.click()

    def click_question_time(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_time, time=3)
        question_title.click()

    def click_question_order_today(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_order_today, time=3)
        question_title.click()

    def click_question_prolongation(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_prolongation, time=3)
        question_title.click()

    def click_question_charger(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_charger, time=3)
        question_title.click()

    def click_question_cancellation(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_cancellation, time=3)
        question_title.click()

    def click_question_long_distance(self):
        question_title = self.find_element(LocatorYaSamokatMainPage.question_long_distance, time=3)
        question_title.click()

    def get_question_price_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_price_accordion_panel, time=3)
        return panel.text

    def get_question_quantity_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_quantity_accordion_panel, time=3)
        return panel.text

    def get_question_time_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_time_accordion_panel, time=3)
        return panel.text

    def get_question_order_today_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_order_today_accordion_panel, time=3)
        return panel.text

    def get_question_prolongation_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_prolongation_accordion_panel, time=3)
        return panel.text

    def get_question_charger_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_charger_accordion_panel, time=3)
        return panel.text

    def get_question_cancellation_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_cancellation_accordion_panel, time=3)
        return panel.text

    def get_question_long_distance_accordion_panel_text(self):
        panel = self.find_element(LocatorYaSamokatMainPage.question_long_distance_accordion_panel, time=3)
        return panel.text

    def get_main_title(self):
        main_title = self.find_element(LocatorYaSamokatMainPage.main_title, time=3)
        return main_title.text

