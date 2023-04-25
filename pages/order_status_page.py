from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.for_who_form_page import LocatorOrderForms


class LocatorOrderStatusPage:
    yandex_logo = [By.XPATH, ".//img[@src='/assets/ya.svg']"]
    samokat_logo = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    order_status_button = [By.XPATH, "//button[contains(text(),'Посмотреть статус')]"]
    dzen_title = [By.XPATH, "/html/head/title"]


class OrderStatusPage(BasePage):
    def click_on_yandex_logo(self, driver):
        yandex_logo = self.find_element(LocatorOrderStatusPage.yandex_logo, time=3)
        yandex_logo.click()

    def click_on_samokat_logo(self):
        samokat_logo = self.find_element(LocatorOrderStatusPage.samokat_logo, time=3)
        samokat_logo.click()

















