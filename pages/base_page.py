from selenium.webdriver.remote.webdriver import WebDriver
class BasePage:
    base_url = 'https://rateyourmusic.com'
    current_url = None
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def open_page(self):
        if self.current_url:
            self.driver.get(f'{self.base_url}{self.current_url}')
        else:
            raise NotImplementedError('Page cannot be opened')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)