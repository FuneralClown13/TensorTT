
from ..base_page import BasePage
from locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    @BasePage.stale_element_reference_exception_handler
    def check_size_photos(self):
        """
        Проверка размеров фото
        """
        photos = self.browser.find_elements(*TensorAboutPageLocators.working_content)
        photo_size = photos.pop(0).size
        for i, p in enumerate(photos):
            assert photo_size == p.size, f'Размер 1 и {i + 2} не совпадают'
