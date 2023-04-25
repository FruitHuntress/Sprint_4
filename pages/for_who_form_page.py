from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorOrderForms:
    order_button_top = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[contains(text(), 'Заказать')]"]
    order_button_bottom = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]"]
    name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]

    date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат"]
    rental_time_field = [By.XPATH, ".//div[@class='Dropdown-control']"]
    calendar_button = [By.XPATH, ".//div[@aria-label='Choose понедельник, 24-е апреля 2023 г.']"]
    rental_time_button = [By.XPATH, "//div[contains(text(),'двое суток')]"]
    order_button_final = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    yes_button = [By.XPATH, "//button[contains(text(),'Да')]"]
    placed_order_window_title = [By.XPATH, "//div[contains(text(),'Хотите оформить заказ?')]"]
    order_status_button = [By.XPATH, "//button[contains(text(),'Посмотреть статус')]"]


class ForWhoFormPage(BasePage):
    def click_order_button_top(self):
        order_button_top = self.find_element(LocatorOrderForms.order_button_top, time=3)
        order_button_top.click()

    def click_order_button_bottom(self):
        order_button_bottom = self.find_element(LocatorOrderForms.order_button_bottom, time=3)
        order_button_bottom.click()

    def fill_in_the_form_for_who(self, name, surname, address, station, phone):
        name_field = self.find_element(LocatorOrderForms.name, time=3)
        name_field.send_keys(name)

        surname_field = self.find_element(LocatorOrderForms.surname, time=3)
        surname_field.send_keys(surname)

        address_field = self.find_element(LocatorOrderForms.address, time=3)
        address_field.send_keys(address)

        station_field = self.find_element(LocatorOrderForms.station, time=3)
        station_field.send_keys(station)
        station_field.send_keys(Keys.DOWN)
        station_field.send_keys(Keys.ENTER)

        phone_field = self.find_element(LocatorOrderForms.phone, time=3)
        phone_field.send_keys(phone)

        next_button = self.find_element(LocatorOrderForms.next_button, time=3)
        next_button.click()




















