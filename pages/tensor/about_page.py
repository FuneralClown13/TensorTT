
from ..base_page import BasePage
from locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    def check_size_photos(self):
        photos = self.browser.find_elements(*TensorAboutPageLocators.working_content)
        photo_size = photos.pop(0).size
        for p in photos:
            assert photo_size == p.size
