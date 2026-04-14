class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def wait_for(self, locator):
        self.page.wait_for_selector(locator)

    def get_text(self, locator):
        return self.page.inner_text(locator)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()
    
    def take_screenshot(self, name="screnshot.png"):
        self.page.screenshot(path=f"screenshots/{name}")