from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.pages_base import PagesBase


class IndexPage(PagesBase):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def play_easy_mode(self) -> WebElement:
        return self.element_present((By.ID, "play-easy-mode"))
