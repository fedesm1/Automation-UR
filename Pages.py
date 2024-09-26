import data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#En esta clase se define la paguina web, y las variables de la clase definen los elementos de la pagina web como atributos de la clase
class UrbanRoutesPage:

    # Localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')
    comfort_tariff_button = (By.CLASS_NAME, 'tcard')
    telephone_number = (By.CLASS_NAME, 'np-text')
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
    button_checkbox = (By.XPATH, "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']//input[@class='switch-input']")
    add_icecream = (By.CLASS_NAME, "counter-plus")
    counter_button = (By.CLASS_NAME, "counter-value")

    # Esta funcion es el contructor para los objetos de la clase
    def __init__(self, driver):
        self.driver = driver

    # las siguientes funciones definen las interacciones con los elementos de la pagina web
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

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def enter_card_code(self):
        code_fild = self.driver.find_elements(*self.card_code_field)
        code_fild[1].send_keys(data.card_code)

    def get_card_code(self):
        code_fild = self.driver.find_elements(*self.card_code_field)
        code = code_fild[1]
        return code.get_property('value')

    def press_tab_key(self):
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def click_card_close_button(self):
        self.driver.find_element(*self.card_close_button).click()

    def enter_new_message(self):
        self.driver.find_element(*self.message).send_keys(data.message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.message).get_property('value')

    def click_blanket_and_scarves(self):
        self.driver.find_element(*self.blanket_and_scarves).click()

    def get_checkbox(self):
        button = self.driver.find_element(*self.button_checkbox)
        status = button.is_selected()
        return status

    def click_add_icecream(self):
        ice_cream_click = self.driver.find_element(*self.add_icecream)
        ice_cream_click.click()
        ice_cream_click.click()

    def get_counter(self):
        counter = self.driver.find_element(*self.counter_button)
        number = counter.text
        return number
