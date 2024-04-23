import os
from os import listdir
from os.path import isfile, join

from loguru import logger

from config import Config
from ..base_page import BasePage
from locators import SbisDownloadPageLocators


class SbisDownloadPage(BasePage):

    @BasePage.stale_element_reference_exception_handler
    def go_to_plugin_section(self):
        logger.info('wait loading page')
        while 'tab=ereport' not in self.browser.current_url:
            continue

        plugin = self.browser.find_element(*SbisDownloadPageLocators.plugin_section)
        plugin.click()
        logger.info(f'current_url: {self.browser.current_url}')
        assert 'tab=plugin' in self.browser.current_url, self.browser.current_url
        # assert 'tab=plugin' in self.browser.current_url

    def remove_files(self):
        files = self.get_files()
        for file in files:
            os.remove(file)
        logger.info(f'remove files: remove complete')

    @staticmethod
    def get_files() -> list:
        path = Config.download_dir_path
        files = [join(path, file) for file in listdir(path) if isfile(join(path, file))]
        files.sort(key=lambda file: os.path.getmtime(file))
        return files

    @BasePage.stale_element_reference_exception_handler
    def download_plugin(self, remove_files=False):
        files = self.get_files()
        logger.info('downloading file')
        download_file = self.browser.find_element(*SbisDownloadPageLocators.file_link)
        download_file.click()

        newest_file = [file for file in self.get_files() if file not in files]
        logger.info(f'file: {newest_file}')
        assert newest_file
        if remove_files:
            self.remove_files()

    @BasePage.stale_element_reference_exception_handler
    def comparing_file_sizes(self, remove_files=False):
        self.download_plugin()

        file_info = self.browser.find_element(*SbisDownloadPageLocators.file_link)
        file_info_size = file_info.get_attribute('text')

        newest_file = self.get_files().pop()

        newest_file_size = os.path.getsize(newest_file)
        newest_file_size = str(round(newest_file_size / 1024 / 1024, 2))
        logger.info(f'file size: {newest_file_size}')

        assert newest_file_size in file_info_size, f'{newest_file_size} != {file_info_size}'
        if remove_files:
            self.remove_files()
