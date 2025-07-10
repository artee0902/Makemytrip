import pytest
from pages.train_booking_page import TrainBookingPage

def test_book_train_ticket(page, config):
    train_page = TrainBookingPage(page)
    train_page.visit(config["base_url"])
    train_page.go_to_train_tab()
    train_page.enter_source_destination(config["train_source"], config["train_destination"])
    train_page.search_trains()
