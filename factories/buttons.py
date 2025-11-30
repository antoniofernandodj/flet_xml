from . import t
from flet import (
    CupertinoButton,
    CupertinoFilledButton,
    ElevatedButton,
    FilledButton,
    FilledTonalButton,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    TextButton
)


def generate_cupertino_button_component(options: t.Options) -> t.Any:
    return CupertinoButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        padding=options.get("padding"),
        on_click=options.get("on_click"),
    )


def generate_cupertino_filled_button_component(options: t.Options) -> t.Any:
    return CupertinoFilledButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        padding=options.get("padding"),
        on_click=options.get("on_click"),
    )


def generate_elevated_button_component(options: t.Options) -> t.Any:
    return ElevatedButton(
        width=options.get('width'),
        height=options.get('height'),
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        tooltip=options.get("tooltip"),
        autofocus=options.get("autofocus"),
        on_click=options.get("on_click"),
    )


def generate_filled_button_component(options: t.Options) -> t.Any:
    return FilledButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        autofocus=options.get("autofocus"),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_filled_tonal_button_component(options: t.Options) -> t.Any:
    return FilledTonalButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        autofocus=options.get("autofocus"),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_floating_action_button_component(options: t.Options) -> t.Any:
    return FloatingActionButton(
        icon=options.get("icon"),
        text=options.get("text"),
        bgcolor=options.get("bgcolor"),
        tooltip=options.get("tooltip"),
        mini=options.get("mini"),
        shape=options.get("shape"),
        on_click=options.get("on_click"),
    )


def generate_icon_button_component(options: t.Options) -> t.Any:
    return IconButton(
        icon=options.get("icon"),
        icon_color=options.get("icon_color"),
        bgcolor=options.get("bgcolor"),
        disabled=options.get("disabled"),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_outlined_button_component(options: t.Options) -> t.Any:
    return OutlinedButton(
        width=options.get('width'),
        height=options.get('height'),
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        autofocus=options.get("autofocus"),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )


def generate_text_button_component(options: t.Options) -> t.Any:
    return TextButton(
        text=options.get("text"),
        icon=options.get("icon"),
        disabled=options.get("disabled"),
        autofocus=options.get("autofocus"),
        tooltip=options.get("tooltip"),
        on_click=options.get("on_click"),
    )
