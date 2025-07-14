class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url)
        self._dismiss_login_popup()

    def _dismiss_login_popup(self):
        try:
            self.page.wait_for_selector("div[data-cy='outsideModal']", timeout=5000)
            # Click close button
            self.page.locator("span[data-cy='closeModal']").click()
        except:

            pass

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, value):
        self.page.locator(selector).fill(value)

    def press_enter(self, selector):
        self.page.locator(selector).press("Enter")
