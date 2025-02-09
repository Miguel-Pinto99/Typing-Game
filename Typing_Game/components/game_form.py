import reflex as rx
from .sections import (
    render_options_card,
    render_btns_card,
    render_warning_card,
    render_instructions_card,
    render_results_card,
    render_words_card,
    render_time_text,
)
import random
from time import time
from asyncio import sleep
from ..data.words import easy_words, medium_words, hard_words


class GameFormState(rx.State):
    difficulty: str = ""
    duration: str = "0"
    remaining_time: int = 0

    game_doing: bool = False
    icon_color: str = ""
    warning_show: bool = False
    message: str = ""
    text_color: str = ""
    icon_tag: str = ""
    word_to_write: str = ""
    wrote_word: str = ""
    start_time: float = 0
    time_on_word: float = 0
    results: list[dict] = []
    show_results: bool = False

    # @rx.background
    # async def countdown(self):
    #     if time() - self.start_time >= int(self.duration):
    #         while self.countdown_second > 0:
    #             async with self:
    #                 self.countdown_second -= 1
    #             await asyncio.sleep(1)

    @rx.event
    def set_difficulty(self, value: str):
        self.difficulty = value

    @rx.event
    def set_duration(self, value: str):
        self.duration = value

    @rx.event
    def set_wrote_word(self, value: str):
        self.wrote_word = value

    @rx.event
    def set_word_to_write(self) -> None:
        if self.difficulty == "Easy":
            word_list = easy_words
        elif self.difficulty == "Medium":
            word_list = medium_words
        elif self.difficulty == "Hard":
            word_list = hard_words
        else:
            raise ValueError("Invalid difficulty")

        word_list_length = len(word_list)
        random_index = random.randint(0, word_list_length - 1)
        self.word_to_write = word_list[random_index]

    @rx.event
    def set_warning(
        self,
        warning_show: bool,
        icon_color: str,
        icon_tag: str,
        message: str,
        text_color: str,
    ) -> None:
        self.icon_color = icon_color
        self.warning_show = warning_show
        self.message = message
        self.text_color = text_color
        self.icon_tag = icon_tag

    @rx.event
    def reset_game(self):
        self.difficulty = ""
        self.duration = "0"
        self.game_doing = False
        self.icon_color = ""
        self.warning_show = False
        self.message = ""
        self.text_color = ""
        self.icon_tag = ""
        self.word_to_write = ""
        self.wrote_word = ""
        self.start_time = 0
        self.time_on_word = 0
        self.results = []
        self.show_results = False
        self.remaining_time = 0

    @rx.event
    def validate_inputs(self) -> bool:
        if "0" == self.duration:
            self.set_warning(
                True, "orange", "triangle-alert", "Fill all the inputs", "orange"
            )
            return False
        elif "" == self.difficulty:
            self.set_warning(
                True, "orange", "triangle-alert", "Fill all the inputs", "orange"
            )
            return False
        return True

    @rx.event
    def check_answer(self, value) -> None:
        self.wrote_word = value
        if time() >= self.start_time + int(self.duration):
            self.end_game()
            return

        if self.wrote_word == self.word_to_write:
            yield self.set_wrote_word("")
            time_taken = time() - self.time_on_word
            readable_time_taken = f"{time_taken % 60:.2f}s"
            self.results.append(
                {"word": self.word_to_write, "time_taken": readable_time_taken}
            )
            self.set_word_to_write()
            self.time_on_word = time()

    @rx.event
    def start_game(self):
        if not self.validate_inputs():
            return
        self.results = []
        self.game_doing = True
        self.set_word_to_write()
        self.start_time = time()
        self.time_on_word = time()
        self.remaining_time = int(self.duration)

    @rx.event
    def end_game(self):
        self.game_doing = False
        self.show_results = True

    @rx.event(background=True)
    async def update_time(self):
        while self.game_doing:
            if time() - self.start_time >= int(self.duration):
                async with self:
                    self.end_game()
                break
            else:
                async with self:
                    self.remaining_time = round(self.remaining_time - 0.1, 1)
                await sleep(0.1)


def game_form() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                render_instructions_card(),
                render_words_card(GameFormState),
                rx.vstack(
                    render_options_card(GameFormState), render_btns_card(GameFormState)
                ),
                height="35em",
                spacing="1",
                align="center",
            ),
            rx.cond(
                GameFormState.game_doing,
                render_time_text(GameFormState),
            ),
            rx.cond(
                GameFormState.show_results,
                render_results_card(GameFormState.results),
            ),
            rx.cond(
                GameFormState.warning_show,
                render_warning_card(
                    GameFormState,
                    GameFormState.icon_color,
                    GameFormState.icon_tag,
                    GameFormState.message,
                    GameFormState.text_color,
                ),
            ),
            align="center",
        )
    )
