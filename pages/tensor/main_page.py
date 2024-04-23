from selenium.webdriver.common.by import By

from ..base_page import BasePage
from locators import TensorMainPageLocators

class TensorMainPage(BasePage):
    @BasePage.stale_element_reference_exception_handler
    def go_to_about_page(self):
        about_link = self.browser.find_element(*TensorMainPageLocators.about_page_link)
        about_link.location_once_scrolled_into_view
        about_link.click()
        assert 'https://tensor.ru/about' in self.browser.current_url

    def should_be_about_block_content(self):
        assert self.is_element_present(*TensorMainPageLocators.power_in_people_content)

    def check_size_photos(self):
        photos = self.browser.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper')
        photo_size = photos.pop(0).size
        for p in photos:
            assert photo_size == p.size
