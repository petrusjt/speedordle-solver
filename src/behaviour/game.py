from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from szozat_solver.submodules.guess_recommendation import GuessRecommendation

from src.pages.game import GamePage

WORDMAP = {0: "abhor", 1: "dingy", 2: "fleck", 3: "stump"}


class GameBehaviour:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.game_page = GamePage(driver)
        self.wordle_map = {}
        self.current_present = []
        self.current_not_present = []
        self.current_regex = ['.' for _ in range(5)]

    def play(self):
        i = 0
        while True:
            nth_wordle = self.game_page.nth_wordle(i)
            for j in range(4):
                self.game_page.get_row_col_from_wordle(nth_wordle, j).send_keys(WORDMAP.get(j))
                if self.collect_word_data(nth_wordle, j, WORDMAP.get(j)):
                    break
            if j and j == 3:
                for j in range(4, 6):
                    recommended_word = self.get_recommendation()
                    self.game_page.get_row_col_from_wordle(nth_wordle, j).send_keys(recommended_word)
                    if self.collect_word_data(nth_wordle, j, recommended_word):
                        break

            self.reset_current()
            i += 1

    def collect_word_data(self, nth_wordle: WebElement, row: int, current_word: str) -> bool:
        correct_poss = 0
        for i in range(5):
            elem = self.game_page.get_row_col_from_wordle(nth_wordle, row, i)
            classes = elem.get_attribute("class")
            if "correct-pos" in classes:
                correct_poss += 1
                if current_word[i] not in self.current_present:
                    self.current_present.append(current_word[i])
                self.current_regex[i] = current_word[i]
            elif "correct-letter" in classes:
                if current_word[i] not in self.current_present:
                    self.current_present.append(current_word[i])
                regex_for_i = self.current_regex[i]
                if regex_for_i.startswith("^") and current_word[i] not in regex_for_i:
                    self.current_regex[i] += current_word[i]
                elif regex_for_i == ".":
                    self.current_regex[i] = f"^{current_word[i]}"
            else:
                if current_word[i] not in self.current_not_present:
                    self.current_not_present.append(current_word[i])

        return correct_poss == 5

    def get_recommendation(self) -> str:
        formatted_regex_list = [f"[{regex}]" if regex.startswith("^") else regex for regex in self.current_regex]
        options_list = GuessRecommendation(False,
                                           ",".join(self.current_present),
                                           ",".join(self.current_not_present),
                                           "".join(formatted_regex_list),
                                           "en").get_recommendations()
        return options_list[0] if len(options_list) else "abhor"

    def reset_current(self):
        self.current_present = []
        self.current_not_present = []
        self.current_regex = ['.' for _ in range(5)]
