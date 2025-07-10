from .base_page import BasePage
import time

class BusBookingPage(BasePage):
    def go_to_bus_tab(self):
        self.page.keyboard.press("Escape")
        self.page.goto("https://www.makemytrip.com/bus-tickets/")
        self.page.wait_for_load_state("networkidle")
        self.page.screenshot(path="bus_page_debug.png")
        self.page.wait_for_selector("#src", timeout=15000)

    def enter_source_destination(self, source, destination):
        self.click("#src")
        self.fill("#src", source)
        time.sleep(1)
        self.press_enter("#src")

        self.click("#dest")
        self.fill("#dest", destination)
        time.sleep(1)
        self.press_enter("#dest")

    def search_buses(self):
        self.click("label[for='onward_cal']")  # open calendar
        self.click("//td[@class='wd day' or @class='current day']/following-sibling::td[1]")  # select next day
        self.click("button#search_btn")
