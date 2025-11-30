from . import t
from flet import Icons
from flet import (
    # Canvas,
    CircleAvatar,
    CupertinoActivityIndicator,
    Icon,
    Image,
    Markdown,
    Text,
    ProgressBar,
    ProgressRing,
    WebView,
)

# [ENUM] INFO_DISPLAY: InfoDisplay


def generate_canvas_component(options: t.Options) -> t.Any:
    pass
    # return Canvas(
    #     shapes=options.get("shapes", []),
    #     width=options.get("width"),
    #     height=options.get("height"),
    #     on_paint=options.get("on_paint"),
    # )



def generate_circle_avatar_component(options: t.Options) -> t.Any:
    return CircleAvatar(
        content=options.get("content"),
        foreground_image_src=options.get("foreground_image_src"),
        background_image_src=options.get("background_image_src"),
        radius=options.get("radius"),
        bgcolor=options.get("bgcolor"),
    )


def generate_cupertino_activity_indicator_component(options: t.Options) -> t.Any:
    return CupertinoActivityIndicator(
        radius=options.get("radius"),
        color=options.get("color"),
        animating=options.get("animating"),
    )



def generate_icon_component(options: t.Options) -> t.Any:
    name = options.get("name") or Icons.HELP_OUTLINE

    return Icon(
        name=name,
        size=options.get("size", 24),
        color=options.get("color"),
        tooltip=options.get("tooltip"),
    )



def generate_image_component(options: t.Options) -> t.Any:
    src = options.get("src") or ""

    return Image(
        src=src,
        width=options.get("width"),
        height=options.get("height"),
        fit=options.get("fit"),
        repeat=options.get("repeat"),
        border_radius=options.get("border_radius"),
    )


def generate_markdown_component(options: t.Options) -> t.Any:
    return Markdown(
        value=options.get("value"),
        selectable=options.get("selectable"),
        extension_set=options.get("extension_set"),
        on_tap_link=options.get("on_tap_link"),
    )


def generate_text_component(options):
    return Text(
        value=options.get("value"),
        size=options.get("size"),
        color=options.get("color"),
        weight=options.get("weight"),
        opacity=options.get('opacity')
    )


def generate_progress_bar_component(options: t.Options) -> t.Any:
    return ProgressBar(
        value=options.get("value"),
        bgcolor=options.get("bgcolor"),
        color=options.get("color"),
        bar_height=options.get("bar_height", 4),
    )



def generate_progress_ring_component(options: t.Options) -> t.Any:
    return ProgressRing(
        value=options.get("value"),
        width=options.get("width", 32),
        height=options.get("height", 32),
        stroke_width=options.get("stroke_width", 4),
        color=options.get("color"),
        bgcolor=options.get("bgcolor"),
    )


def generate_web_view_component(options: t.Options) -> t.Any:
    return WebView(
        url=options.get("url"),
        width=options.get("width"),
        height=options.get("height"),
        on_page_started=options.get("on_page_started"),
        on_page_ended=options.get("on_page_ended"),
        js_bridge=options.get("js_bridge"),
    )
