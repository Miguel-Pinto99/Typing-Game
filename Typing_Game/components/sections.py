import reflex as rx
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

