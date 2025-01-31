import reflex as rx


class GameFormState(rx.State):
    letters: int = 0
    duration: int = 0

    def set_maximum_value(self, value: str):
        self.letters = int(value)

    def set_duration(self, value: str):
        self.duration = int(value)


def game_form() -> rx.Component:
    return rx.card(
        rx.grid(
            rx.text("Number of letters"),
            rx.input(
                value=GameFormState.letters,
                on_change=GameFormState.set_maximum_value,
            ),
            type="number",
            max_width="5em",
        ),
        rx.text("Duration"),
        rx.input(
            value=GameFormState.duration,
            on_change=GameFormState.set_duration,
            type="number",
            max_width="5em",
        ),
        class_name="grid-cols-[repeat(3,max-content)]",
        align="center",
        spacing="1",
    )
