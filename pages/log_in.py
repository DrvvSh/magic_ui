from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import log_in_locators as loc

class LogIn(BasePage):
    current_url = '/account/login'


    def fill_in_the_form(self, user, passw):
        username = self.find(loc.username_loc)
        password = self.find(loc.password_loc)
        login_button = self.find(loc.login_button_loc)
        # Test data input
        username.send_keys(user)
        password.send_keys(passw)
        login_button.click()


    def check_error_message_text_is(self, text):
        wait = WebDriverWait(self.driver, 5)
        error_message = wait.until(
            EC.visibility_of_element_located(loc.error_message_loc)
        )
        assert error_message.text == text

