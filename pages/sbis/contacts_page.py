from time import sleep
from loguru import logger

from selenium.webdriver.common.by import By

from locators import SbisContactsPageLocators, TensorMainPageLocators
from ..base_page import BasePage


class SbisContactsPage(BasePage):
    @BasePage.stale_element_reference_exception_handler
    def go_to_region_page(self, region_name):
        """
        Переход на страницу другого региона
        :param region_name: Регион на который будет совершен переход
        """
        choicer_region = self.browser.find_element(*SbisContactsPageLocators.region_chooser)
        choicer_region.click()
        logger.info(f'change region: {region_name}')
        sleep(0.5)
        select_region = self.browser.find_element(By.CSS_SELECTOR, f'[title="{region_name}"] :nth-child(1)')
        select_region.click()

    @BasePage.stale_element_reference_exception_handler
    def go_to_tensor_website(self):
        """
        Переход на сайт tensor.ru из sbis.ru/contacts
        Проверка url
        """
        tensor_link = self.browser.find_element(*SbisContactsPageLocators.contacts_logo_tensor)
        tensor_link.click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.browser.find_element(*TensorMainPageLocators.header_logo)
        cur_url = self.browser.current_url
        logger.info(f'current_url: {cur_url}')
        assert 'tensor' in cur_url, f'Не удалось перейти на tensor.ru: {cur_url}'

    @BasePage.stale_element_reference_exception_handler
    def check_region(self):
        """
        Проверка автоопределения региона
        """
        region = self.browser.find_element(*SbisContactsPageLocators.region_chooser)
        region_name = region.text
        logger.info(f'check region: {region_name}')
        assert region_name == 'Калининградская обл.', f'Неверно определен регион: {region_name}'

    @BasePage.stale_element_reference_exception_handler
    def check_partner_list(self):
        """
        Проверка наличия блока со списком контактов
        """
        assert self.is_element_present(*SbisContactsPageLocators.contacts_list), 'Нет списка контактов'
        logger.info(f'partner_list is present')

    @BasePage.stale_element_reference_exception_handler
    def change_region_endpoint(self, region_name):
        """
        Смена региона и проверка, что url изменился
        :param region_name: Регион на который будет совершен переход
        """
        old_region = self.browser.current_url
        logger.info(f'old region: {old_region}')

        self.go_to_region_page(region_name)

        new_region = self.browser.current_url
        logger.info(f'new_region: {new_region}')

        assert old_region != new_region, 'Регион не поменялся или не изменился url'

    @BasePage.stale_element_reference_exception_handler
    def check_change_region_partner_list(self, region_name):
        """
        Смена региона и проверка, что список контактов изменился
        :param region_name: Регион на который будет совершен переход
        """
        old_contact_list = self.browser.find_elements(*SbisContactsPageLocators.contacts_list)
        old_contact_list_titles = [contact.get_attribute('title') for contact in old_contact_list]
        logger.info(f'old_contact_list: {old_contact_list_titles}')

        self.go_to_region_page(region_name)

        new_contact_list = self.browser.find_elements(*SbisContactsPageLocators.contacts_list)
        new_contact_list_titles = [contact.get_attribute('title') for contact in new_contact_list]
        logger.info(f'new_contact_list: {new_contact_list_titles}')

        assert old_contact_list_titles != new_contact_list_titles, 'Регион не поменялся или не изменился список контаков'

    @BasePage.stale_element_reference_exception_handler
    def check_change_region_title(self, region_name):
        """
        Смена региона и проверка, что title изменился
        :param region_name: Регион на который будет совершен переход
        """
        old_title = self.browser.find_element(*SbisContactsPageLocators.title)
        old_title_text = old_title.get_attribute('text')
        logger.info(f'old_title: {old_title_text}')

        self.go_to_region_page(region_name)

        new_title = self.browser.find_element(*SbisContactsPageLocators.title)
        new_title_text = new_title.get_attribute('text')
        logger.info(f'new_title: {new_title_text}')

        assert old_title_text != new_title_text, 'Регион не поменялся или не изменился title'
