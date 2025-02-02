import reflex as rx
from .sections import render_warning_card, render_instructions_card

# import readchar
import random
from time import time
from colorama import Fore, Style


class GameFormState(rx.State):
    letters: int = 0
    duration: int = 0

    game_doing: bool = False
    icon_color: str = ""
    warning_show: bool = False
    message: str = ""
    text_color: str = ""
    icon_tag: str = ""
    key_to_press: str = ""
    key_pressed: str = ""

    @rx.event
    def set_maximum_value(self, value: str):
        self.letters = int(value)

    @rx.event
    def set_duration(self, value: str):
        self.duration = int(value)

    @rx.event
    def set_key_to_press(self, key: str) -> None:
        self.key_to_press = key

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
        self.letters = 0
        self.duration = 0
        self.game_doing = False
        self.warning_show = False
        self.message = ""
        self.text_color = ""
        self.icon_tag = ""
        self.icon_color = ""
        self.key_to_press = ""

    @rx.event
    def validate_inputs(self) -> bool:
        if 0 in [
            self.letters,
            self.duration,
        ]:
            self.set_warning(
                True, "orange", "triangle-alert", "Fill all the inputs", "orange"
            )
            return False

        elif self.duration > 60:
            self.set_warning(True, "orange", "triangle-alert", "Game to long", "orange")
            return False
        return True

    @rx.event
    def start_game(self, event) -> None:
        self.game_doing = True
        valid = self.validate_inputs()
        if not valid:
            self.game_doing = False
            return

        test_start = time()
        time_c = 0
        time_w = 0
        number_of_hits = 0
        number_of_types = 0
        number_of_misses = 0

        if event.key:
            print(event.key)

        while True:
            random_char = chr(random.randint(97, 122))
            self.set_key_to_press(random_char)
            print(Fore.CYAN + "\nType " + str(random_char) + Style.RESET_ALL)
            duration = time()
            pressed_char = "a"
            duration = time() - duration

            if time() >= test_start + self.duration:
                break
            # inputs.append(Input(random_char, pressed_char, duration))

            if random_char == pressed_char:
                print(
                    "\nYou typed "
                    + Fore.GREEN
                    + pressed_char
                    + Style.RESET_ALL
                    + ". "
                    + "Correct!"
                )
                number_of_hits += 1
                number_of_types += 1
                time_c += duration
            elif pressed_char == "140":
                self.reset_game()
            else:
                print(
                    "\nYou typed "
                    + Fore.RED
                    + pressed_char
                    + Style.RESET_ALL
                    + ". "
                    + "Wrong!"
                )
                number_of_misses += 1
                number_of_types += 1
                time_w += duration

        test_duration = time_w + time_c
        self.set_warning(
            True,
            "green",
            "check-circle",
            f"Game Over! Hits: {number_of_hits}, Misses: {number_of_misses}, Duration: {test_duration:.2f}s",
            "green",
        )
        self.game_doing = False

    # @rx.event
    # def key_pressed(self, event):
    #     random_char = self.get_random_char()
    #     self.set_key_to_press(random_char)
    #     print(Fore.CYAN + "\nType " + str(random_char) + Style.RESET_ALL)
    #     duration = time.time()
    #     pressed_char = event.char
    #     duration = time.time() - duration

    #     if time.time() >= self.test_start + self.duration:
    #         return
    #     self.inputs.append(Input(random_char, pressed_char, duration))

    #     if random_char == pressed_char:
    #         print(
    #             "\nYou typed "
    #             + Fore.GREEN
    #             + pressed_char
    #             + Style.RESET_ALL
    #             + ". "
    #             + "Correct!"
    #         )
    #         self.number_of_hits += 1
    #         self.number_of_types += 1
    #         self.time_c += duration
    #     elif pressed_char == "140":
    #         self.reset_game()
    #     else:
    #         print(
    #             "\nYou typed "
    #             + Fore.RED
    #             + pressed_char
    #             + Style.RESET_ALL
    #             + ". "
    #             + "Wrong!"
    #         )
    #         self.number_of_misses += 1
    #         self.number_of_types += 1
    #         self.time_w += duration

    def get_random_char(self):
        return random.choice("abcdefghijklmnopqrstuvwxyz")


def game_form() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                render_instructions_card(),
                rx.card(
                    rx.text(
                        GameFormState.key_to_press,
                        align="center",
                        spacing="1",
                        width="15em",
                        height="5em",
                        font_size="3em",
                        font_weight="bold",
                    )
                ),
                rx.vstack(
                    rx.card(
                        rx.grid(
                            rx.text("Number of letters"),
                            rx.input(
                                value=GameFormState.letters,
                                on_change=GameFormState.set_maximum_value,
                                type="number",
                                max_width="10em",
                            ),
                            rx.text("Duration"),
                            rx.input(
                                value=GameFormState.duration,
                                on_change=GameFormState.set_duration,
                                type="number",
                                max_width="10em",
                            ),
                            class_name="grid-cols-[repeat(2,max-content)]",
                            align="center",
                            spacing="1",
                        )
                    ),
                    rx.button(
                        "Start",
                        variant="solid",
                        on_click=GameFormState.set_key_to_press(
                            "Press any key to start"
                        ),
                        loading=GameFormState.game_doing,
                    ),
                    rx.button(
                        "Reset",
                        variant="solid",
                        on_click=GameFormState.reset_game,
                    ),
                    rx.input(
                        type="hidden",
                        on_key_down=GameFormState.key_pressed,
                    ),
                ),
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
