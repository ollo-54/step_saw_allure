from pages.departure_page import DeparturePage
from pages.tour_page import TourPage
from data_handler import Data
from urllib.parse import urljoin
import pytest


def test_tour_title_on_departure_page_and_tour_page(browser, link):
    link_dep = urljoin(link, "/departure/msk")
    page = DeparturePage(browser, link_dep)
    page.open()
    departure_tour_title_text = page.get_departure_tour_title_text()
    page.click_on_the_tour_cards_link()
    page = TourPage(browser, link_dep)
    tour_title_text = page.get_tour_title_text()
    page.should_be_exact_text(departure_tour_title_text.lower(), tour_title_text.lower())
    

def test_tour_general_info(browser, link):
    link_tour = urljoin(link, "/tour/4")
    page = TourPage(browser, link_tour)
    page.open()
    data = Data()
    tour_page_title_text = page.get_tour_description_text()
    
    tour_description_text = f'{data.get_tour_duration_of_stay(id=4)} Ночей'
    page.should_be_exact_text(tour_description_text.lower(), tour_page_title_text.lower())
    
    tour_page_title = data.get_departure(departure='msk')
    page.should_be_exact_text(tour_page_title.lower(), tour_page_title_text.lower())


@pytest.mark.regression
def test_tour_price(browser, link):
    link_tour = urljoin(link, "/tour/4")
    page = TourPage(browser, link_tour)
    page.open()
    data = Data()
    tour_page_price_text = page.get_tour_price_text()
    tour_page_price = f'за {data.get_tour_price(id=4)}'
    page.should_be_exact_text(tour_page_price.lower(), tour_page_price_text.lower())


def test_tours_have_different_pictures_and_content(browser, link):
    for i in range(1, 3):
        link_tour = urljoin(link, f"/tour/{i}")
        page = TourPage(browser, link_tour)
        page.open()
        
        tour_picture_on_page = page.get_picture_src_on_tour_page()
        tour_content_on_page = page.get_content_on_tour_page_text()
        
        data = Data()
        tour_picture = data.get_tour_picture(id=i)
        assert tour_picture == tour_picture_on_page, f'Different pictures on tour page {i} and data'

        tour_content = data.get_tour_content(id=i)
        assert tour_content == tour_content_on_page, f'Different content on tour page {i} and data'

