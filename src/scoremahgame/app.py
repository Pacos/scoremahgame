"""
Mahjong Scoring App
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ScoreMahGame(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        def new_game_handler(widget):
            print("new_game_button pressed")

        def continue_game_handler(widget):
            print("continue_game_button pressed")

        title_label = toga.Label("Score Mah Game", style=Pack(color="#45d18b", text_align="center", font_size="32", padding=10))

        new_game_button = toga.Button("New Game", on_press=new_game_handler, style=Pack(padding=10))
        continue_game_button = toga.Button("Continue", on_press=continue_game_handler, enabled=False, style=Pack(padding=10))

        main_box.add(title_label)
        main_box.add(new_game_button)
        main_box.add(continue_game_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return ScoreMahGame()
