import time

from selenium.webdriver import Chrome, ChromeOptions

from src.behaviour.game import GameBehaviour
from src.pages.index import IndexPage

options = ChromeOptions()
options.add_argument("--start-maximized")

driver = Chrome(options=options)
driver.get("https://speedordle.com/")

index = IndexPage(driver)
index.play_easy_mode().click()

try:
    game = GameBehaviour(driver)
    game.play()
    time.sleep(10000)
except Exception as e:
    time.sleep(60)
    raise e
finally:
    driver.close()
