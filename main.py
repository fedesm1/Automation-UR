import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import Pages
import Helpers

#La siguiente clase define las pruebas con Pytest
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 5)

    def test_set_route(self):

        self.driver.maximize_window()
        self.driver.get(data.urban_routes_url)

        routes_page = Pages.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to

        self.wait.until(ec.presence_of_element_located(routes_page.from_field))
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    def test_select_tariff(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        self.wait.until(ec.element_to_be_clickable(Pages.UrbanRoutesPage.order_taxi_button))
        routes_page.click_order_taxi_button()
        routes_page.click_comfort_tariff_button()

        comfort_button = self.driver.find_element(By.CLASS_NAME, "tcard.active")
        comfort_class = comfort_button.get_attribute('class')
        assert "active" in comfort_class, "El botón Comfort no está activo."

    def test_fill_phone_number(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        routes_page.fill_in_phone_number()
        routes_page.click_next_button()
        #Recibir codigo de confirmacion
        code = Helpers.retrieve_phone_code(self.driver)
        routes_page.set_confirmation_code(code)
        assert len(code) == 4
        routes_page.click_code_confirmation_button()

    def test_add_card(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_field()
        routes_page.click_add_card_button()
        routes_page.enter_card_number()
        assert routes_page.get_card_number() == data.card_number

    def test_add_card_code(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        routes_page.enter_card_code()
        routes_page.press_tab_key()
        routes_page.click_add_button()
        routes_page.click_card_close_button()
        assert len(routes_page.get_card_code()) == 3

    def test_message_and_option(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        routes_page.enter_new_message()
        assert 'Muéstrame' in routes_page.get_message()

    def test_add_blanket_and_scarves(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_scarves()
        routes_page.get_checkbox()
        assert routes_page.get_checkbox() == True

    def test_add_icecream(self):
        routes_page = Pages.UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream()
        assert routes_page.get_counter() == '2'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

