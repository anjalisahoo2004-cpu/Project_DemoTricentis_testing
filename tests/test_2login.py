import pytest
from DemoTricentis_BasePage.pages.login import LoginPage
from DemoTricentis_BasePage.utilities.read_login_data import get_login_data

#@pytest.mark.parametrize("email,password",get_login_data())
@pytest.mark.parametrize("email,password",[('student','student_123')])
def test_login(setup_and_teardown,email,password):

    login_page = LoginPage(setup_and_teardown)
    login_page.click_login_link()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
