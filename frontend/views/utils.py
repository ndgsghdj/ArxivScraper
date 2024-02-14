from flet import Page, TextField
import flet_material as fm
from typing import List

class WrongCreds:
    def __init__(self, page: Page, inputs: List[TextField], error_strings: List[str]) -> None:
        self.page = page
        self.wrong_creds = zip(inputs, error_strings)
        self.page.update()

    def on_focus_input(self, e):
        for input, error_string in self.wrong_creds:
            input.error_text = None
        self.page.update()

    def set_error(self):
        for input, error_string in self.wrong_creds:
            input.error_text = error_string
            input.on_focus = self.on_focus_input
        self.page.update()
    