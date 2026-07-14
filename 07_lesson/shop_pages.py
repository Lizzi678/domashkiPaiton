from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self._username_field = (By.CSS_SELECTOR, "#user-name")
        self._password_field = (By.CSS_SELECTOR, "#password")
        self._login_button = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self._username_field).send_keys(username)
        self.driver.find_element(*self._password_field).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self._backpack_btn = (
            By.CSS_SELECTOR,
            "#add-to-cart-sauce-labs-backpack",
        )
        self._tshirt_btn = (
            By.CSS_SELECTOR,
            "#add-to-cart-sauce-labs-bolt-t-shirt",
        )
        self._onesie_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self._cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_backpack(self):
        self.driver.find_element(*self._backpack_btn).click()

    def add_tshirt(self):
        self.driver.find_element(*self._tshirt_btn).click()

    def add_onesie(self):
        self.driver.find_element(*self._onesie_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self._checkout_btn = (By.CSS_SELECTOR, "#checkout")

    def click_checkout(self):
        self.driver.find_element(*self._checkout_btn).click()


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self._first_name_field = (By.CSS_SELECTOR, "#first-name")
        self._last_name_field = (By.CSS_SELECTOR, "#last-name")
        self._postal_code_field = (By.CSS_SELECTOR, "#postal-code")
        self._continue_button = (By.CSS_SELECTOR, "#continue")
        self._total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self._first_name_field).send_keys(first_name)
        self.driver.find_element(*self._last_name_field).send_keys(last_name)
        self.driver.find_element(*self._postal_code_field).send_keys(
            postal_code
        )
        self.driver.find_element(*self._continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self._total_label).text