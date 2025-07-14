from .base_page import BasePage
from playwright.sync_api import expect
import time

class TrainBookingPage(BasePage):
    def go_to_train_tab(self):
        self.page.keyboard.press("Escape")  # Dismiss login modal
        self.page.goto("https://www.makemytrip.com/railways/")
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_selector("input#fromCity", timeout=15000)

    def enter_source_destination(self, source, destination):
        self.click("#fromCity")
        self.fill("input[placeholder='From']", source)
        self.press_enter("input[placeholder='From']")

        self.click("#toCity")
        self.fill("input[placeholder='To']", destination)
        self.press_enter("input[placeholder='To']")

    def select_journey_date(self):
        # Click calendar and select tomorrow’s date
        self.click("label[for='travelDate']")
        self.page.wait_for_selector("div.DayPicker-Day--today + div")
        self.click("div.DayPicker-Day--today + div")  # Select next day

    def search_trains(self):
        # Handle popups or overlays (e.g. notification iframe or sticky banners)
        try:
            # Remove iframe if it exists
            if self.page.locator("iframe[title='notification-frame-~']").is_visible():
                self.page.locator("iframe[title='notification-frame-~']").evaluate("node => node.remove()")
        except:
            pass

        # Press ESC to close login overlays or any modals
        self.page.keyboard.press("Escape")

        # Random click to dismiss autocomplete dropdowns
        self.page.mouse.click(50, 50)

        # Give slight delay to settle UI
        self.page.wait_for_timeout(1000)

        # Scroll search button into view and click forcefully if needed
        search_button = self.page.locator("a.primaryBtn.font24.latoBold.widgetSearchBtn")
        search_button.scroll_into_view_if_needed()
        search_button.wait_for(state="visible", timeout=10000)
        search_button.click(force=True)

    def select_first_available_train(self):
        self.page.wait_for_selector("div.trainCard", timeout=20000)
        cards = self.page.locator("div.trainCard")
        assert cards.count() > 0, "No train cards found!"
        cards.nth(0).click()

    # Update selector if needed

    def choose_class(self, class_name):
        # Scroll to class selection and click the desired class
        self.page.locator("div.coach-class-options").scroll_into_view_if_needed()
        self.click(f"text={class_name}")

    def enter_passenger_details(self, name, age, gender):
        self.fill("input[placeholder='Name']", name)
        self.fill("input[placeholder='Age']", age)
        self.click(f"label:has-text('{gender}')")  # Gender radio button

    def click_continue(self):
        self.click("button:has-text('Continue')")

    def is_login_or_payment_displayed(self):
        # Use expect in test; here just return locator
        return self.page.locator("div.login-content")  # Or another payment selector
