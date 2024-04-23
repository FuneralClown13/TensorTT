from loguru import logger
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium import webdriver
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, browser: webdriver.Firefox, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        print('')
        logger.info(f'open: {self.url}')
        self.browser.get(self.url)
        self.skip_preload_overlay()
        self.browser.implicitly_wait(self.timeout)

    @staticmethod
    def stale_element_reference_exception_handler(f):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    f(*args, **kwargs)
                except StaleElementReferenceException:
                    logger.error('StaleElementReferenceException')
                    continue
                break
        return wrapper

    def skip_preload_overlay(self):
        skip_counter = 0
        while self.is_element_present(*BasePageLocators.preload_overlay):
            skip_counter += 1
            continue
        if skip_counter:
            logger.info(f'preload_overlay: {skip_counter} skips')

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
