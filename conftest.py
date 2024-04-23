import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config import Config
from logs import logger_config


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", Config.download_dir_path)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

    logger.add(**logger_config[0])

    browser = webdriver.Firefox(
        options=options
    )

    yield browser

    browser.quit()
