import pytest
from pages.bus_booking_page import BusBookingPage

def test_book_bus_ticket(page, config):
    bus_page = BusBookingPage(page)
    bus_page.visit(config["base_url"])
    bus_page.go_to_bus_tab()
    bus_page.enter_source_destination(config["bus_source"], config["bus_destination"])
    bus_page.search_buses()
