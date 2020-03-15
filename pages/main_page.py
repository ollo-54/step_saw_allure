from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page_link_on_logo(self):
        logo_link = self.browser.find_element(*MainPageLocators.LOGO_LINK).get_attribute('href')
        print('Link - ' + str(logo_link))
        main_page_url = self.browser.current_url
        assert logo_link == main_page_url, f'Wait for the link: {main_page_url}, but got {logo_link}'

    def should_be_menu_on_page(self):
        menu_main = self.is_element_present(*MainPageLocators.MENU_ON_PAGE)
        assert menu_main, 'Menu is not on the page'
    
    def links_lead_to_different_pages(self):
        menu_items = self.browser.find_elements(*MainPageLocators.MENU_ITEMS)
        amount_of_menu_items = len(menu_items)
        print('Amount of menu items ' + str(amount_of_menu_items))
        i = 0
        list_of_links = []
        for element in menu_items:
            new_link = element.get_attribute('href')
            list_of_links.append(new_link)
            print('Link # ' + str(i) + '\n' + new_link)
            i = i + 1
        list_of_links_set = set(list_of_links)
        print('Total ' + str(len(list_of_links)) + ' links, ' + str(len(list_of_links_set)) + ' of which are unique')
        assert len(list_of_links) == len(list_of_links_set), 'Duplicate links'

    def click_on_the_departure_link(self):
        menu_item = self.browser.find_element(*MainPageLocators.MENU_ITEMS)
        menu_item.click()


