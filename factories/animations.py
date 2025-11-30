from . import t
from flet import (
    AnimatedSwitcher,
    Lottie,
    Rive
)


def generate_animated_switcher_component(options: t.Options) -> t.Any:
    return AnimatedSwitcher(
        content=options.get("content"),
        duration=options.get("duration", 300),
        reverse_duration=options.get("reverse_duration", 300),
        transition=options.get("transition", "fade"),
    )



def generate_lottie_component(options: t.Options) -> t.Any:
    return Lottie(
        src=options.get("src"),
        repeat=options.get("repeat", True),
        reverse=options.get("reverse", False),
        animate=options.get("animate", True),
        width=options.get("width"),
        height=options.get("height"),
        fit=options.get("fit"),
        background_color=options.get("background_color"),
    )



def generate_rive_component(options: t.Options) -> t.Any:
    return Rive(
        src=options.get("src"),
        artboard=options.get("artboard"),
        animation=options.get("animation"),
        width=options.get("width"),
        height=options.get("height"),
        fit=options.get("fit"),
        antialiasing=options.get("antialiasing", True),
    )