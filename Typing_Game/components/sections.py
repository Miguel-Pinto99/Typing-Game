import reflex as rx

style1 = {
    "color": "white",
    "font_family": "Comic Sans MS",
    "border_radius": "10px",
    "background_color": "rgb(107,99,246)",
    "padding": "10px",
    "align": "center",
}


def render_warning_card(
    obj_class, icon_color: str, icon_tag: str, message: str, text_color: str
) -> rx.Component:
    return rx.card(
        rx.hstack(
            dynamic_icon(icon_tag, icon_color),
            rx.text(
                message,
                color=text_color,
                align="left",
                text_wrap="wrap",
            ),
            rx.icon(
                tag="circle-x",
                color=icon_color,
                cursor="pointer",
                on_click=obj_class.set_warning(False, "", "", "", ""),
            ),
            align="center",
            justify="between",
        ),
        border_width="1px",
        border_color=icon_color,
    )


def dynamic_icon(icon_name: str, icon_color: str):
    return rx.match(
        icon_name,
        ("triangle-alert", rx.icon("triangle-alert", color=icon_color)),
        ("circle-check-big", rx.icon("circle-check-big", color=icon_color)),
    )


def render_instructions_card():
    return (
        rx.card(
            rx.text("Instructions", style=style1),
            rx.divider(),
            rx.spacer(height="10px"),
            rx.list.ordered(
                rx.list.item("Enter the number of letters you want to type."),
                rx.spacer(height="10px"),
                rx.list.item("Enter the duration for the game (in seconds)."),
                rx.spacer(height="10px"),
                rx.list.item("Click 'Start Game' to begin."),
                rx.spacer(height="10px"),
                rx.list.item(
                    "Type the displayed letter as quickly and accurately as possible."
                ),
                rx.spacer(height="10px"),
                rx.list.item("The game will end when the time is up."),
                rx.spacer(height="10px"),
                rx.list.item(
                    "Your performance will be displayed at the end of the game."
                ),
                align="left",
                spacing="1",
                max_width="20em",
            ),
        ),
    )
