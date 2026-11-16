from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self,locator):
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,text):
        # self.driver.find_element(*locator).send_keys(text)
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

