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
                    "Type the displayed word as quickly and accurately as possible."
                ),
                rx.spacer(height="10px"),
                rx.list.item("The game will end when the time is up."),
                rx.spacer(height="10px"),
                rx.list.item(
                    "Your performance will be displayed at the end of the game."
                ),
                align="left",
                spacing="1",
                height="100%",
            ),
        ),
    )


def render_btns_card(state: rx.State) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.button(
                "Start",
                variant="solid",
                on_click=[state.start_game, state.update_time],
                loading=state.game_doing,
            ),
            rx.button(
                "Reset",
                variant="solid",
                on_click=state.reset_game,
            ),
            align="center",
            justify="center",
        ),
        align="center",
        justify="between",
        width="15em",
    )


def render_time_text(state: rx.State) -> rx.Component:
    return rx.text(
        f"Time remaining: {state.remaining_time}",
        font_size="1.5em",
        color="gray",
    )


def render_words_card(state: rx.State) -> rx.Component:
    return rx.card(
        rx.grid(
            rx.text(
                state.word_to_write,
                spacing="1",
                font_size="3em",
                font_weight="bold",
                align="center",
                justify="center",
            ),
            rx.input(
                value=state.wrote_word,
                on_change=state.check_answer,
                disabled=~state.game_doing,
                placeholder="write here",
                text_align="center",
                font_size="2em",
                align="center",
            ),
            class_name="grid-rows-[repeat(2,50%)]",
            width="100%",
            justify="center",
            align="center",
            height="30em",
        ),
        height="27.5em",
        width="100%",
        justify="center",
        align="center",
    )


def render_options_card(state: rx.State) -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.grid(
                rx.text("Difficulty"),
                rx.select(
                    ["Easy", "Medium", "Hard"],
                    value=state.difficulty,
                    on_change=state.set_difficulty,
                    disabled=state.game_doing,
                    width="10em",
                ),
                rx.text("Duration"),
                rx.select(
                    ["10", "30", "60", "90", "120"],
                    value=state.duration,
                    on_change=state.set_duration,
                    disabled=state.game_doing,
                    width="10em",
                ),
                class_name="grid-cols-[repeat(2,max-content)]",
                align="center",
                spacing="1",
            ),
            height="100%",
            width="15em",
        ),
    )


def render_results_card(results: list[dict]) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("Results"),
            rx.divider(),
            rx.data_list.root(
                rx.foreach(
                    results,
                    lambda item: rx.data_list.item(
                        rx.data_list.label(item["word"]),
                        rx.data_list.value(item["time_taken"]),
                    ),
                ),
                align="center",
                spacing="1",
            ),
        ),
        height="100%",
    )
