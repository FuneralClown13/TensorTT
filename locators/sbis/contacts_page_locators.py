from selenium.webdriver.common.by import By


class SbisContactsPageLocators:
    region_chooser = By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text'
    contacts_logo_tensor = By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor'

    contacts_list = By.CSS_SELECTOR, '.sbisru-Contacts-List__name'
    title = By.CSS_SELECTOR, '.state-1'
