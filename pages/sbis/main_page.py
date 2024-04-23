from loguru import logger

from locators import SbisMainPageLocators
from ..base_page import BasePage


class SbisMainPage(BasePage):

    @BasePage.stale_element_reference_exception_handler
    def go_to_contacts_page(self):
        contacts_link = self.browser.find_element(*SbisMainPageLocators.header_menu_contacts)
        contacts_link.click()

        logger.info(f'current_url: {self.browser.current_url}')

        assert 'contacts' in self.browser.current_url

    @BasePage.stale_element_reference_exception_handler
    def go_to_download_page(self):
        download_link = self.browser.find_element(*SbisMainPageLocators.download_page_link)
        download_link.location_once_scrolled_into_view
        download_link.click()

        logger.info(f'current_url: {self.browser.current_url}')

        assert 'download' in self.browser.current_url

