from loguru import logger

from pages import SbisMainPage, SbisContactsPage, TensorMainPage, TensorAboutPage
from urls import SbisUrls, TensorUrls


class TestCase1:
    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_go_to_contacts_page(self, browser):
        page = SbisMainPage(browser, SbisUrls.main)
        page.open()
        page.go_to_contacts_page()

    #     @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_go_to_tensor_website(self, browser):
        page = SbisContactsPage(browser, SbisUrls.contacts)
        page.open()
        page.go_to_tensor_website()

    #     @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_power_in_people_is_present(self, browser):
        page = TensorMainPage(browser, TensorUrls.main)
        page.open()
        page.should_be_about_block_content()

    #     @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_go_to_about_page(self, browser):
        page = TensorMainPage(browser, TensorUrls.main)
        page.open()
        page.go_to_about_page()

    @logger.catch(reraise=True)
    def test_check_size_photos(self, browser):
        page = TensorAboutPage(browser, TensorUrls.about)
        page.open()
        page.check_size_photos()
