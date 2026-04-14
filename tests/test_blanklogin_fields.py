from pages.login_page import LoginPage

def test_inv_login(page, config):
    login_page = LoginPage(page)

    login_page.load(config.get("url"))
    login_page.login("", "")

    login_page.take_screenshot("blank_login_error.png")
    
    assert page.locator("text=Required").first.is_visible()