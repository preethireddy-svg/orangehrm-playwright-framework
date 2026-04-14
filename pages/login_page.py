from pages.base_page import BasePage

class LoginPage(BasePage):  # This means Login page can use all methods of Base page, this is called inherritance-an oops concept
    def __init__(self, page):
        super().__init__(page) # This inherits/calls constructor of Parent page i.e BasePage here and so it executes self.page=page from BasePage

        # Locators
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.error_message = ".oxd-alert-content-text"

    def load(self, url):
        self.navigate(url)

    def login(self, username, password):
        self.wait_for(self.username_input)
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)
        #self.page.wait_for_timeout(2000)# not a suggestable usage of explicit wait like this

    def get_error_message(self):
        self.page.wait_for_selector(self.error_message,timeout=5000)
        return self.get_text(self.error_message)
    
    def handle_post_login_popup(self):
        try:
        # Example: close button (adjust if needed using inspector)
            self.page.locator("button:has-text('OK')").click(timeout=5000)
        except:
            pass

    def is_login_successful(self):
        # Dashboard element appears after login
         self.page.wait_for_url("**/dashboard/**", timeout=10000) # this waits for dashboard text in url
         #self.page.wait_for_selector("h6:has-text('Dashboard')", timeout=10000)  # Locator here means- Find an <h6> element anywhere on the page whose text is exactly "Dashboard"
         return True