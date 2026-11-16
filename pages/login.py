from selenium.webdriver.common.by import By

from DemoTricentis_BasePage.pages.basepage import BasePage

class LoginPage(BasePage):
    login_link = (By.XPATH,'//a[text()="Log in"]')
    email = (By.ID,'Email')
    password = (By.ID,'Password')
    login_button = (By.XPATH,'//input[@value="Log in"]')

    def click_login_link(self):
        self.click(self.login_link)

    def enter_email(self,email_txt):
        self.enter_text(self.email,email_txt)

    def enter_password(self,password_txt):
        self.enter_text(self.password,password_txt)

    def click_login_button(self):
        self.click(self.login_button)