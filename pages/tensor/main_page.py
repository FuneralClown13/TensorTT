from selenium.webdriver.common.by import By

from ..base_page import BasePage
from locators import TensorMainPageLocators

class TensorMainPage(BasePage):
    @BasePage.stale_element_reference_exception_handler
    def go_to_about_page(self):
        """
        Переход на страницу about
        """
        about_link = self.browser.find_element(*TensorMainPageLocators.about_page_link)
        about_link.location_once_scrolled_into_view
        about_link.click()
        cur_url = self.browser.current_url
        assert 'https://tensor.ru/about' in cur_url, f'Открыта неверная страница: {cur_url}'

    def should_be_about_block_content(self):
        """
        Проверка, что есть блок "Сила в людях"
        """
        assert self.is_element_present(*TensorMainPageLocators.power_in_people_content), 'нет блока "Сила в людях"'

