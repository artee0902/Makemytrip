from pages.train_booking_page import TrainBookingPage
from playwright.sync_api import expect

def test_train_selection_and_class(page, config):
    train_page = TrainBookingPage(page)

    train_page.visit(config["base_url"])
    train_page.go_to_train_tab()
    train_page.enter_source_destination("Pune", "Mumbai")
    train_page.select_journey_date()
    train_page.search_trains()
    page.wait_for_url("**/railways/listing**", timeout=15000)


# def test_passenger_entry_and_continue(page, config):
#     train_page = TrainBookingPage(page)
#
#     train_page.visit(config["base_url"])
#     train_page.go_to_train_tab()
#     train_page.enter_source_destination(config["train_source"], config["train_destination"])
#     train_page.select_journey_date()
#     train_page.search_trains()
#     train_page.select_first_available_train()
#     train_page.choose_class("Sleeper")
#     train_page.enter_passenger_details(name="Test User", age="30", gender="Male")
#     train_page.click_continue()

    # expect(page.locator("div.login-content")).to_be_visible()  # Or replace with payment element
