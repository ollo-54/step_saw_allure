from pages.base_page import BasePage
from pages.locators import TourPageLocators


class TourPage(BasePage):        

    def should_be_tour_page(self):
        tour_header = self.is_element_present(*TourPageLocators.TOUR_HEADER)
        assert tour_header, 'No go to tour page'
        current_url_tour = self.browser.current_url
        print('Current url tour', current_url_tour)
        assert 'tour' in current_url_tour, f"This is not tour page, expected 'tour' in the {current_url_tour}"

    def get_picture_src_on_tour_page(self):
        picture_on_tour_page = self.browser.find_element(*TourPageLocators.PICTURE_ON_TOUR_PAGE)
        return picture_on_tour_page.get_attribute("src")

    def get_content_on_tour_page_text(self):
        content_on_tour_page_text = self.browser.find_element(*TourPageLocators.CONTENT_ON_TOUR_PAGE)
        return content_on_tour_page_text.text

    def get_tour_title_text(self):
        tour_title_text = self.browser.find_element(*TourPageLocators.TOUR_TITLE).text
        return tour_title_text

    def get_tour_description_text(self):
        tour_description_text = self.browser.find_element(*TourPageLocators.TOUR_DESCRIPTION).text
        return tour_description_text

    def get_tour_price_text(self):
        tour_price_text = self.browser.find_element(*TourPageLocators.TOUR_PRICE).text
        return tour_price_text
