from selenium.webdriver.common.by import By


class SbisDownloadPageLocators:
    plugin_section = By.CSS_SELECTOR, '[data-id="plugin"]'
    file_link = By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]'
