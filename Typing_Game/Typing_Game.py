"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.header import header
from .components.game_form import game_form


def index() -> rx.Component:
    return rx.vstack(
        header(),
        game_form(),
        align="center",
    )


app = rx.App()
app.add_page(index, title="Typing Game")
