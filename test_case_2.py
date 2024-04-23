from loguru import logger

from pages import SbisMainPage, SbisContactsPage
from urls import SbisUrls


class TestCase2:
    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_go_to_contacts_page(self, browser):
        page = SbisMainPage(browser, SbisUrls.main)
        page.open()
        page.go_to_contacts_page()

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_check_region(self, browser):
        page = SbisContactsPage(browser, SbisUrls.contacts)
        page.open()
        page.check_region()

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_check_partner_list(self, browser):
        page = SbisContactsPage(browser, SbisUrls.contacts)
        page.open()
        page.check_partner_list()

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_change_region_endpoint(self, browser):
        page = SbisContactsPage(browser, SbisUrls.contacts)
        page.open()
        page.change_region_endpoint(region_name="Камчатский край")

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_check_change_region_partner_list(self, browser):
        page = SbisContactsPage(browser, SbisUrls.contacts)
        page.open()
        page.check_change_region_partner_list(region_name="Камчатский край")

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_check_change_region_title(self, browser):
        page = SbisContactsPage(browser, SbisUrls.contacts)
        page.open()
        page.check_change_region_title(region_name="Камчатский край")
