from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorRentInfoFormPage:
    order_button_top = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[contains(text(), 'Заказать')]"]
    order_button_bottom = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]"]

    date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    rental_time_field = [By.XPATH, ".//div[@class='Dropdown-control']"]
    calendar_button = [By.XPATH, ".//div[@class='react-datepicker__week']/div[@aria-label='Choose понедельник, 24-е апреля 2023 г.']"]
    rental_time_button = [By.XPATH, "//div[contains(text(),'двое суток')]"]
    order_button_final = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[contains(text(), 'Заказать')]"]
    yes_button = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[contains(text(), 'Да')]"]
    placed_order_window_title = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']/div[contains(text(), 'Заказ оформлен')]"]
    order_status_button = [By.XPATH, "//button[contains(text(),'Посмотреть статус')]"]


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

    def click_order_status_button(self):
        order_status_button = self.find_element(LocatorRentInfoFormPage.order_status_button, time=3)
        order_status_button.click()

















