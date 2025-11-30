import flet as ft
from . import t

# [ENUM] INFO_DISPLAY: InfoDisplay


def generate_canvas_component(options: t.Options) -> t.Any:
    return ft.Canvas(
        shapes=options.get("shapes", []),
        width=options.get("width"),
        height=options.get("height"),
        on_paint=options.get("on_paint"),
    )



def generate_circle_avatar_component(options: t.Options) -> t.Any:
    return ft.CircleAvatar(
        content=options.get("content"),
        foreground_image_src=options.get("foreground_image_src"),
        background_image_src=options.get("background_image_src"),
        radius=options.get("radius", 20),
        bgcolor=options.get("bgcolor"),
    )


def generate_cupertino_activity_indicator_component(options: t.Options) -> t.Any:
    return ft.CupertinoActivityIndicator(
        radius=options.get("radius", 12),
        color=options.get("color"),
        animating=options.get("animating", True),
    )



def generate_icon_component(options: t.Options) -> t.Any:
    name = options.get("name") or ft.icons.HELP_OUTLINE

    return ft.Icon(
        name=name,
        size=options.get("size", 24),
        color=options.get("color"),
        tooltip=options.get("tooltip"),
    )



def generate_image_component(options: t.Options) -> t.Any:
    src = options.get("src") or ""

    return ft.Image(
        src=src,
        width=options.get("width"),
        height=options.get("height"),
        fit=options.get("fit", ft.ImageFit.CONTAIN),
        repeat=options.get("repeat"),
        border_radius=options.get("border_radius"),
    )


def generate_markdown_component(options: t.Options) -> t.Any:
    return ft.Markdown(
        value=options.get("value", ""),
        selectable=options.get("selectable", False),
        extension_set=options.get("extension_set", ft.MarkdownExtensionSet.COMMONMARK),
        on_tap_link=options.get("on_tap_link"),
    )


def generate_text_component(options):
    return ft.Text(
        value=options.get("value", ""),
        size=options.get("font_size"),
        color=options.get("color"),
        weight=options.get("bold") and ft.FontWeight.BOLD,
    )


def generate_progress_bar_component(options: t.Options) -> t.Any:
    return ft.ProgressBar(
        value=options.get("value"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        bar_height=options.get("bar_height", 4),
    )



def generate_progress_ring_component(options: t.Options) -> t.Any:
    return ft.ProgressRing(
        value=options.get("value"),
        width=options.get("width", 32),
        height=options.get("height", 32),
        stroke_width=options.get("stroke_width", 4),
        color=options.get("color"),
        bgcolor=options.get("bgcolor"),
    )


def generate_web_view_component(options: t.Options) -> t.Any:
    return ft.WebView(
        url=options.get("url", ""),
        width=options.get("width"),
        height=options.get("height"),
        on_page_started=options.get("on_page_started"),
        on_page_ended=options.get("on_page_ended"),
        js_bridge=options.get("js_bridge"),
    )
