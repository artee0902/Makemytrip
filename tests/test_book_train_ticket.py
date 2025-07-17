import pytest
from pages.train_booking_page import TrainBookingPage
from playwright.sync_api import expect


@pytest.mark.order(1)
def test_book_train_ticket(page, config):
    train_page = TrainBookingPage(page)
    train_page.visit(config["base_url"])
    train_page.go_to_train_tab()
    train_page.enter_source_destination(config["train_source"], config["train_destination"])
    train_page.search_trains()

@pytest.mark.order(2)
def test_visit_homepage(page, config):
    page.goto(config["base_url"],timeout=6000)
    expect(page).to_have_url(config["base_url"])
    expect(page.locator("li.menu_Trains")).to_be_visible()

@pytest.mark.order(3)
def test_train_search_results_displayed(page, config):
    train_page = TrainBookingPage(page)
    train_page.visit(config["base_url"])
    train_page.go_to_train_tab()
    train_page.enter_source_destination(config["train_source"], config["train_destination"])
    train_page.search_trains()

    # expect(page.locator("div.trainCard")).to_be_visible(timeout=15000)  # At least one train card is shown

# @pytest.mark.order(4)
# def test_select_first_train_and_class(page, config):
#     train_page = TrainBookingPage(page)
#     train_page.visit(config["base_url"])
#     train_page.go_to_train_tab()
#     train_page.enter_source_destination(config["train_source"], config["train_destination"])
#     train_page.select_journey_date()  # ✅ Needed
#     train_page.search_trains()
#
#     train_page.select_first_available_train()
#     train_page.choose_class("Sleeper")  # Or "3A", "2A", etc.



