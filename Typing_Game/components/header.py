import reflex as rx


def header() -> rx.Component:
    return rx.fragment(
        rx.hstack(
            rx.spacer(),
            rx.heading("Tipping Game", size="6", class_name="place-self-center"),
            rx.spacer(),
            rx.color_mode.button(),
            position="top",
            padding="1em",
            padding_bottom="0px",
            width="100%",
        ),
        rx.divider(),
    )
