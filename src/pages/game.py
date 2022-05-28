from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.pages_base import PagesBase


class GamePage(PagesBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def nth_wordle(self, n: int = 0) -> WebElement:
        return self.element_present((By.ID, f'MyWordle[{n}]'))

    def get_row_col_from_wordle(self, wordle: WebElement, row: int, col: int = 0) -> WebElement:
        return wordle.find_element(By.ID, f"text[{row}]square[{col}]")
