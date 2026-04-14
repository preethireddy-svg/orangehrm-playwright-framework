from pages.login_page import LoginPage
import pytest # this imports code from pytest.ini

@pytest.mark.login # to mark thic tc as login
@pytest.mark.smoke # to mark this tc as smoke also
def test_valid_login(page, config):
    login_page = LoginPage(page)

    login_page.load(config.get("url"))
    login_page.login(config.get("username"), config.get("password"))
    #page.pause() 

     # Handle popup
    login_page.handle_post_login_popup()

    assert login_page.is_login_successful()