from pages.order_status_page import OrderStatusPage
from pages.rent_info_form_page import RentInfoFormPage
from pages.ya_samokat_main_page import YaSamokatMainPage
from urls import Urls
from data import Client
import allure
import pytest


@allure.story('TestPlaceOrder')
class TestPlaceOrder:
    @allure.feature('test making order through the top order button')
    @pytest.mark.parametrize('name, surname, address, station, phone',[
        Client.Igor,
        Client.Arina
    ])
    def test_order_from_top_order_button(self, driver, form_opened_by_top_order_button, name, surname, address, station, phone):
        form_opened_by_top_order_button.fill_in_the_form_for_who(name, surname, address, station, phone)
        rent_info_form_page = RentInfoFormPage(driver)
        rent_info_form_page.fill_in_the_form_rent_info()
        text = rent_info_form_page.confirm_order()
        rent_info_form_page.click_order_status_button()
        assert 'Заказ оформлен' in text

    @allure.feature('test making order through the bottom order button')
    @pytest.mark.parametrize('name, surname, address, station, phone', [
        Client.Igor,
        Client.Arina
    ])
    def test_order_from_bottom_order_button(self, driver, form_opened_by_bottom_order_button, name, surname, address, station, phone):
        form_opened_by_bottom_order_button.fill_in_the_form_for_who(name, surname, address, station, phone)
        rent_info_form_page = RentInfoFormPage(driver)
        rent_info_form_page.fill_in_the_form_rent_info()
        text = rent_info_form_page.confirm_order()
        rent_info_form_page.click_order_status_button()
        assert 'Заказ оформлен' in text

    @allure.feature('test navigation from placed order page')
    @pytest.mark.parametrize('name, surname, address, station, phone', [
        Client.Igor,
        Client.Arina
    ])
    def test_navigation_from_order_status_page(self, driver, form_opened_by_bottom_order_button, name, surname, address, station, phone):
        form_opened_by_bottom_order_button.fill_in_the_form_for_who(name, surname, address, station, phone)
        rent_info_form_page = RentInfoFormPage(driver)
        rent_info_form_page.fill_in_the_form_rent_info()
        rent_info_form_page.confirm_order()
        rent_info_form_page.click_order_status_button()

        order_status_page = OrderStatusPage(driver)
        order_status_page.click_on_samokat_logo()

        ya_main_page = YaSamokatMainPage(driver)
        title = ya_main_page.get_main_title()

        assert 'Самокат' in title

        order_status_page.click_on_yandex_logo(driver)
        order_status_page.switch_to_another_tab(driver)
        url = Urls()
        assert driver.current_url == url.ya_main_page_url



