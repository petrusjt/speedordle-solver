from typing import Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PagesBase:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element_present(self, locator: Tuple[By, str]) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
