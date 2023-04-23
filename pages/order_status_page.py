from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LocatorOrderStatusPage:
    yandex_logo = [By.XPATH, ".//img[@src='/assets/ya.svg']"]
    samokat_logo = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    order_status_button = [By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div[2]/button"]
    dzen_title = [By.XPATH, "/html/head/title"]


class OrderStatusPage(BasePage):
    def click_on_yandex_logo(self, driver):
        yandex_logo = self.find_element(LocatorOrderStatusPage.yandex_logo, time=3)
        yandex_logo.click()

    def switch_to_another_tab(self, driver):
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(1)
        new_url = driver.current_url
        return new_url

    def click_on_samokat_logo(self):
        samokat_logo = self.find_element(LocatorOrderStatusPage.samokat_logo, time=3)
        samokat_logo.click()

















