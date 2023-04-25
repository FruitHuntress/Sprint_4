from pages.ya_samokat_main_page import YaSamokatMainPage
from pages.ya_samokat_main_page import LocatorYaSamokatMainPage
import allure
from data import DataMainPage


@allure.story('TestDropdownList')
class TestDropdownList:
    @allure.feature('test panel unwrapping with answer about price')
    def test_question_price(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_price)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_price_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_price

    def test_question_quantity(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_quantity)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_quantity_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_quantity

    def test_question_time(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_time)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_time_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_time

    def test_question_order_today(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_order_today)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_order_today_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_order_today

    def test_question_prolongation(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_prolongation)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_prolongation_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_prolongation

    def test_question_charger(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_charger)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_charger_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_charger

    def test_question_cancellation(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_cancellation)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_cancellation_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_cancellation

    def test_question_long_distance(self, driver, initiation):
        initiation.click_question_element(LocatorYaSamokatMainPage.question_long_distance)

        ya_samokat_main_page = YaSamokatMainPage(driver)
        panel_text = ya_samokat_main_page.get_question_panel_text(LocatorYaSamokatMainPage.question_long_distance_accordion_panel)

        data_main_page = DataMainPage()
        assert panel_text == data_main_page.data_question_long_distance



