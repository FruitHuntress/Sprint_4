from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LocatorRentInfoFormPage:
    order_button_top = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/button[1]"]
    order_button_bottom = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]"]

    date = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]"]
    rental_time_field = [By.XPATH, ".//div[@class='Dropdown-control']"]
    calendar_button = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[1]"]
    rental_time_button = [By.XPATH, "//div[contains(text(),'двое суток')]"]
    order_button_final = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]"]
    yes_button = [By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div[2]/button[2]"]
    placed_order_window_title = [By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div[1]"]
    order_status_button = [By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div[2]/button"]



class RentInfoFormPage(BasePage):
    def fill_in_the_form_rent_info(self):
        date_field = self.find_element(LocatorRentInfoFormPage.date, time=3)
        date_field.send_keys('24.04.2023')
        calendar_button = self.find_element(LocatorRentInfoFormPage.calendar_button, time=3)
        calendar_button.click()

        rental_time_field = self.find_element(LocatorRentInfoFormPage.rental_time_field, time=3)
        rental_time_field.click()
        rental_time_button = self.find_element(LocatorRentInfoFormPage.rental_time_button, time=3)
        rental_time_button.click()

        order_button_final = self.find_element(LocatorRentInfoFormPage.order_button_final, time=3)
        order_button_final.click()

    def confirm_order(self):
        yes_button = self.find_element(LocatorRentInfoFormPage.yes_button, time=3)
        yes_button.click()

        placed_order_window_title = self.find_element(LocatorRentInfoFormPage.placed_order_window_title, time=3)
        return placed_order_window_title.text

    def scroll_down(self, driver):
        order_button_bottom = self.find_element(LocatorRentInfoFormPage.order_button_bottom, time=3)
        driver.execute_script("arguments[0].scrollIntoView();", order_button_bottom)
        time.sleep(0.2)

    def click_order_status_button(self):
        order_status_button = self.find_element(LocatorRentInfoFormPage.order_status_button, time=3)
        order_status_button.click()
        time.sleep(5)

















