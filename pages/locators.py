from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGO_LINK = (By.CLASS_NAME, 'navbar-brand')
    HEADING_MAIN = (By.CLASS_NAME, 'display-4')
    MENU_ON_PAGE = (By.CLASS_NAME, 'navbar-expand-lg')
    TOUR_CARDS = (By.CLASS_NAME, 'mb-3')
    MENU_ITEMS = (By.CLASS_NAME, 'nav-link')
    PICTURE_ON_TOUR_CARD = (By.CLASS_NAME, 'card-img-top')
    CONTENT_ON_TOUR_CARD = (By.CLASS_NAME, 'card-text')
    LINK_ON_TOUR_CARD = (By.CLASS_NAME, 'btn-primary')

class DeparturePageLocators():
    DEPARTURE_HEADER = (By.CLASS_NAME, 'display-5')
    DEPARTURE_DESCRIPTION = (By.CLASS_NAME, 'mb-4')
    DEPARTURE_TOUR_TITLE = (By.CLASS_NAME, 'card-title')
    
class TourPageLocators():
    TOUR_HEADER = (By.CLASS_NAME, 'btn-success')
    PRICE_TOUR = (By.CLASS_NAME, 'btn-lg')
    TOUR_TITLE = (By.CLASS_NAME, 'mt-4')
    TOUR_DESCRIPTION = (By.CLASS_NAME, 'lead')
    TOUR_PRICE = (By.CLASS_NAME, 'btn-lg')
    PICTURE_ON_TOUR_PAGE = (By.TAG_NAME, 'img.w-75')
    CONTENT_ON_TOUR_PAGE = (By.CLASS_NAME, 'my-4')

