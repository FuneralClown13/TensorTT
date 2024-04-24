import pytest
from loguru import logger
from pages import SbisMainPage, SbisDownloadPage
from urls import SbisUrls


class TestCase3:
    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_go_download_page(self, browser):
        """
        Тестируется возможность посещения страницы download
        """
        page = SbisMainPage(browser, SbisUrls.main)
        page.open()
        page.go_to_download_page()

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_go_plugin_section(self, browser):
        """
        Тестируется возможность выбора в меню раздела СБИС Плагин
        """
        page = SbisDownloadPage(browser, SbisUrls.download)
        page.open()
        page.go_to_plugin_section()

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_can_download_plugin(self, browser):
        """
        Проверяется, скачивается ли плагин

        :remove_files: True, если нужно удалить файл после теста
        """
        page = SbisDownloadPage(browser, SbisUrls.download)
        page.open()
        page.go_to_plugin_section()
        page.download_plugin(remove_files=True)

    # @pytest.mark.skip
    @logger.catch(reraise=True)
    def test_comparing_file_sizes(self, browser):
        """
        Проверка размера файла

        :remove_files: True, если нужно удалить файл после теста
        """
        page = SbisDownloadPage(browser, SbisUrls.download)
        page.open()
        page.go_to_plugin_section()
        page.comparing_file_sizes(remove_files=True)
