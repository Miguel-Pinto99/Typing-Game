import reflex as rx


def header() -> rx.Component:
    return rx.fragment(
        rx.hstack(
            rx.spacer(),
            rx.heading(
                "Typing Game",
                size="6",
                class_name="place-self-center",
                font="Arial",
                color_scheme="gray",
            ),
            rx.spacer(),
            position="top",
            padding="1em",
            padding_bottom="0px",
            width="100%",
        ),
        rx.divider(),
    )
