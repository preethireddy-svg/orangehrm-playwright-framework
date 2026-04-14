from pages.login_page import LoginPage
from utils.test_data import INVALID_LOGIN
import pytest # this imports code from pytest.ini

@pytest.mark.login # to mark thic tc as login
@pytest.mark.regression # to mark this tc as regression also

def test_inv_login(page, config):
    login_page = LoginPage(page)

    login_page.load(config.get("url"))
    login_page.login(INVALID_LOGIN["username"], INVALID_LOGIN["password"])


    error = login_page.get_error_message()

    login_page.take_screenshot("invalid_login.png")
    
    assert INVALID_LOGIN["error"] in error

    