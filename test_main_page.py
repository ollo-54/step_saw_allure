from pages.main_page import MainPage
from pages.departure_page import DeparturePage
from pages.tour_page import TourPage
import pytest


def test_logo_link_should_be_presented(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page_link_on_logo()


def test_menu_should_be_presented(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_menu_on_page()

@pytest.mark.regression
def test_amount_tour_cards_on_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    tour_cards_amount = page.get_amount_of_tour_cards()
    assert tour_cards_amount >= 3, f"Expected 3+ tours tour card, but got {tour_cards_amount}"

@pytest.mark.regression
def test_links_lead_to_different_pages(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.links_lead_to_different_pages()


def test_tour_cards_have_different_pictures(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.tour_cards_have_different_pictures()


def test_tour_cards_have_different_content(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.tour_cards_have_different_content()


def test_tour_cards_have_different_link(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.tour_cards_have_different_links()


def test_link_leads_to_the_departure_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.click_on_the_departure_link()
    page_departure = DeparturePage(browser, link)
    page_departure.should_be_departure_page()


def test_link_leads_to_tour_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.click_on_the_tour_cards_link()
    page_tour = TourPage(browser, link)
    page_tour.should_be_tour_page()

