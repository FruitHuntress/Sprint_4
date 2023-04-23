from pages.order_status_page import OrderStatusPage
from pages.rent_info_form_page import RentInfoFormPage
from pages.ya_samokat_main_page import YaSamokatMainPage
import allure
import pytest


@allure.story('TestDropdownList')
class TestDropdownList:
    def test_question_price(self, driver, initiation):
        initiation.click_question_price()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_price_accordion_panel_text()
        assert panel_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_question_quantity(self, driver, initiation):
        initiation.click_question_quantity()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_quantity_accordion_panel_text()
        assert panel_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_question_time(self, driver, initiation):
        initiation.click_question_time()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_time_accordion_panel_text()
        assert panel_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_question_order_today(self, driver, initiation):
        initiation.click_question_order_today()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_order_today_accordion_panel_text()
        assert panel_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_question_prolongation(self, driver, initiation):
        initiation.click_question_prolongation()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_prolongation_accordion_panel_text()
        assert panel_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_question_charger(self, driver, initiation):
        initiation.click_question_charger()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_charger_accordion_panel_text()
        assert panel_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_question_cancellation(self, driver, initiation):
        initiation.click_question_cancellation()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_cancellation_accordion_panel_text()
        assert panel_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_question_long_distance(self, driver, initiation):
        initiation.click_question_long_distance()

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_long_distance_accordion_panel_text()
        assert panel_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


@allure.story('TestPlaceOrder')
class TestPlaceOrder:
    @allure.feature('test making order through the top order button')
    @pytest.mark.parametrize('name, surname, address, station, phone',[
        ['Игорь', 'Колесников', 'Тверская улица, дом 13', 'Черкизовская', '+79117777777'],
        ['Арина', 'Родионова', 'улица Академика Колмогорова, дом 7', 'Южная', '+79115555555']
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
        ['Игорь', 'Колесников', 'Тверская улица, дом 13', 'Черкизовская', '+79117777777'],
        ['Арина', 'Родионова', 'улица Академика Колмогорова, дом 7', 'Южная', '+79115555555']
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
        ['Игорь', 'Колесников', 'Тверская улица, дом 13', 'Черкизовская', '+79117777777'],
        ['Арина', 'Родионова', 'улица Академика Колмогорова, дом 7', 'Южная', '+79115555555']
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
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'



