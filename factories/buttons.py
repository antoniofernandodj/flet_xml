import flet as ft
from . import t


# [ENUM] BUTTONS: Buttons

def generate_cupertino_button_component(options: t.Options) -> t.Any:
    return ft.CupertinoButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        padding=options.get("padding"),
        on_click=options.get("on_click"),
    )


def generate_cupertino_filled_button_component(options: t.Options) -> t.Any:
    return ft.CupertinoFilledButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        padding=options.get("padding"),
        on_click=options.get("on_click"),
    )


def generate_elevated_button_component(options: t.Options) -> t.Any:
    return ft.ElevatedButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        tooltip=options.get("tooltip"),
        autofocus=options.get("autofocus", False),
        on_click=options.get("on_click"),
    )


def generate_filled_button_component(options: t.Options) -> t.Any:
    return ft.FilledButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        autofocus=options.get("autofocus", False),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_filled_tonal_button_component(options: t.Options) -> t.Any:
    return ft.FilledTonalButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        autofocus=options.get("autofocus", False),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_floating_action_button_component(options: t.Options) -> t.Any:
    return ft.FloatingActionButton(
        icon=options.get("icon"),
        text=options.get("text"),
        bgcolor=options.get("bgcolor"),
        tooltip=options.get("tooltip"),
        mini=options.get("mini", False),
        shape=options.get("shape"),
        on_click=options.get("on_click"),
    )


def generate_icon_button_component(options: t.Options) -> t.Any:
    return ft.IconButton(
        icon=options.get("icon"),
        icon_color=options.get("icon_color"),
        bgcolor=options.get("bgcolor"),
        disabled=options.get("disabled", False),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_outlined_button_component(options: t.Options) -> t.Any:
    return ft.OutlinedButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        autofocus=options.get("autofocus", False),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_text_button_component(options: t.Options) -> t.Any:
    return ft.TextButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled", False),
        autofocus=options.get("autofocus", False),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )
