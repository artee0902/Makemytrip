from .base_page import BasePage
import time

class TrainBookingPage(BasePage):
    def go_to_train_tab(self):
        self.page.keyboard.press("Escape")  # dismiss login modal
        self.page.goto("https://www.makemytrip.com/railways/")
        self.page.wait_for_load_state("domcontentloaded")  # less strict
        self.page.wait_for_selector("input#fromCity", timeout=15000)  # wait for field to appear

    def enter_source_destination(self, source, destination):
        # Click and fill 'From'
        self.click("#fromCity")
        self.fill("input[placeholder='From']", source)
        self.press_enter("input[placeholder='From']")

        # Click and fill 'To'
        self.click("#toCity")
        self.fill("input[placeholder='To']", destination)
        self.press_enter("input[placeholder='To']")

    def search_trains(self):
        self.page.keyboard.press("Escape")  # Close any overlay/modal
        self.page.mouse.click(100, 100)  # Click outside to dismiss suggestions
        self.page.wait_for_timeout(1000)  # Give time for popup to close
        self.page.locator("a.primaryBtn.font24.latoBold.widgetSearchBtn").scroll_into_view_if_needed()
        self.click("a.primaryBtn.font24.latoBold.widgetSearchBtn")  # Click "Search"



