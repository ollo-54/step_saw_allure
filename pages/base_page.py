from selenium.common.exceptions import NoSuchElementException
from pages.locators import MainPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=3):
        super().__init__()
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_exact_text(self, expected_text, real_text):
        assert expected_text in real_text, f"Should be text '{expected_text}' in '{real_text}'"



    def tour_cards_have_different_pictures(self):
        picture_on_tour_cards = self.browser.find_elements(*MainPageLocators.PICTURE_ON_TOUR_CARD)
        amount_of_tour_cards_with_picture = len(picture_on_tour_cards)
        print('Amount of tour cards with pictures ' + str(amount_of_tour_cards_with_picture))
        i = 0
        list_of_pictures = []
        for element in picture_on_tour_cards:
            new_picture = element.get_attribute("src")
            print('Picture # ' + str(i) + '\n' + new_picture)
            list_of_pictures.append(new_picture)
            i = i + 1
        list_of_pictures_set = set(list_of_pictures)
        print('Total ' + str(len(list_of_pictures)) + ' pictures, ' + str(len(list_of_pictures_set)) + ' of which are unique')
        assert len(list_of_pictures) == len(list_of_pictures_set), 'Duplicate pictures'

    def tour_cards_have_different_content(self):
        content_on_tour_cards = self.browser.find_elements(*MainPageLocators.CONTENT_ON_TOUR_CARD)
        amount_of_tour_cards_with_content = len(content_on_tour_cards)
        print('Amount of tour cards with content ' + str(amount_of_tour_cards_with_content))
        i = 0
        list_of_content = []
        for element in content_on_tour_cards:
            new_content = element.text
            list_of_content.append(new_content)
            print('Content # ' + str(i) + '\n' + new_content)
            i = i + 1
        list_of_content_set = set(list_of_content)
        print('Total ' + str(len(list_of_content)) + ' contents, ' + str(len(list_of_content_set)) + ' of which are unique')
        assert len(list_of_content) == len(list_of_content_set), 'Duplicate content'

    def tour_cards_have_different_links(self):
        link_on_tour_cards = self.browser.find_elements(*MainPageLocators.LINK_ON_TOUR_CARD)
        amount_of_tour_cards_with_link = len(link_on_tour_cards)
        print('Amount of cards with link ' + str(amount_of_tour_cards_with_link))
        i = 0
        list_of_links = []
        for element in link_on_tour_cards:
            new_link = element.get_attribute('href')
            list_of_links.append(new_link)
            print('Link # ' + str(i) + '\n' + new_link)
            i = i + 1 
        list_of_links_set = set(list_of_links)
        print('Total ' + str(len(list_of_links)) + ' links, ' + str(len(list_of_links_set)) + ' of which are unique')
        assert len(list_of_links) == len(list_of_links_set), 'Links do not lead to internal pages'

    def click_on_the_tour_cards_link(self):
        tour_cards_link = self.browser.find_element(*MainPageLocators.LINK_ON_TOUR_CARD)
        tour_cards_link.click()


    def get_amount_of_tour_cards(self):
        link_on_tour_cards = self.browser.find_elements(*MainPageLocators.LINK_ON_TOUR_CARD)
        amount_of_tour_cards_with_link = len(link_on_tour_cards)
        print('Amount of tour cards per page ' + str(amount_of_tour_cards_with_link))
        return amount_of_tour_cards_with_link

