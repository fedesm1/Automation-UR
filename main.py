import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code




#En esta clase se define la paguina web, y las variables de la clase definen los elementos de la pagina web como atributos de la clase
class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')
    comfort_tariff_button = (By.CLASS_NAME, 'tcard')
    telephone_number = (By.CLASS_NAME, 'np-text' )
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[contains(text(), "Siguiente")]')
    code_field = (By.ID, 'code')
    code_confirmation_button = (By.XPATH, '//*[contains(text(), "Confirmar")]')
    payment_method = (By.CLASS_NAME, "pp-text")
    add_card = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_number_field = (By.NAME, 'number')
    card_code_field = (By.CLASS_NAME, 'card-input')
    add_button = (By.XPATH, '//button[text()="Agregar"]')
    card_close_button = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')
    message = (By.ID, 'comment')
    blanket_and_scarves = (By.CLASS_NAME, "switch")
    add_icecream = (By.CLASS_NAME, "counter-plus")


    # Esta funcion es el contructor para los objetos de la clase
    def __init__(self, driver):
        self.driver = driver

    #las siguientes funciones definen las interacciones con los elementos de la pagina web
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()

    def click_comfort_tariff_button(self):
        tariff = self.driver.find_elements(*self.comfort_tariff_button)
        tariff[4].click()

    def click_phone_number_field(self):
        self.driver.find_element(*self.telephone_number).click()

    def fill_in_phone_number(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_confirmation_code(self, code):
        self.driver.find_element(*self.code_field).send_keys(code)

    def click_code_confirmation_button(self):
        self.driver.find_element(*self.code_confirmation_button).click()

    def click_payment_method_field(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card).click()

    def enter_card_number(self):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)

    def enter_card_code(self):
        key = self.driver.find_elements(*self.card_code_field)
        key[1].send_keys(data.card_code)

    def press_tab_key(self):
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def click_card_close_button(self):
        self.driver.find_element(*self.card_close_button).click()

    def enter_new_message(self):
        self.driver.find_element(*self.message).send_keys(data.message_for_driver)

    def click_blanket_and_scarves(self):
        self.driver.find_element(*self.blanket_and_scarves).click()

    def click_add_icecream(self):
        ice_cream_click = self.driver.find_element(*self.add_icecream)
        ice_cream_click.click()
        ice_cream_click.click()

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

    def test_set_route_taxi_and_comfort_tariff(self):

        self.driver.maximize_window()
        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to

        self.wait.until(ec.presence_of_element_located(routes_page.from_field))
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        self.wait.until(ec.element_to_be_clickable(UrbanRoutesPage.order_taxi_button))
        routes_page.click_order_taxi_button()
        routes_page.click_comfort_tariff_button()


    def test_telephone_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        routes_page.fill_in_phone_number()
        routes_page.click_next_button()

        code = retrieve_phone_code(self.driver)
        routes_page.set_confirmation_code(code)
        routes_page.click_code_confirmation_button()

    def test_payment_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_field()
        routes_page.click_add_card_button()
        routes_page.enter_card_number()
        routes_page.enter_card_code()
        routes_page.press_tab_key()
        routes_page.click_add_button()
        routes_page.click_card_close_button()

    def test_message_and_option(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_new_message()
        routes_page.click_blanket_and_scarves()
        routes_page.click_add_icecream()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()