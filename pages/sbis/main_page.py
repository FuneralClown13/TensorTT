from loguru import logger

from locators import SbisMainPageLocators
from ..base_page import BasePage


class SbisMainPage(BasePage):

    @BasePage.stale_element_reference_exception_handler
    def go_to_contacts_page(self):
        """
        Переход на страницу contacts и проверка url
        """
        contacts_link = self.browser.find_element(*SbisMainPageLocators.header_menu_contacts)
        contacts_link.click()
        cur_url = self.browser.current_url
        logger.info(f'current_url: {cur_url}')

        assert 'contacts' in cur_url, 'Не удалось открыть страницу contacts'

    @BasePage.stale_element_reference_exception_handler
    def go_to_download_page(self):
        """
        Переход на страницу download и проверка url
        """
        download_link = self.browser.find_element(*SbisMainPageLocators.download_page_link)
        download_link.location_once_scrolled_into_view
        download_link.click()

        logger.info(f'current_url: {self.browser.current_url}')

        assert 'download' in self.browser.current_url, 'Не удалось открыть страницу download'

