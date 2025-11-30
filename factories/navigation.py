import flet as ft
from . import t



# [ENUM] NAVIGATION: Navigation



def generate_app_bar_component(options: t.Options) -> t.Any:
    return ft.AppBar(
        title=options.get("title"),
        center_title=options.get("center_title", True),
        bgcolor=options.get("bgcolor"),
        leading=options.get("leading"),
        actions=options.get("actions", []),
        elevation=options.get("elevation", 4),
        automatically_imply_leading=options.get("automatically_imply_leading", True),
    )


def generate_bottom_app_bar_component(options: t.Options) -> t.Any:
    return ft.BottomAppBar(
        content=options.get("content"),
        notch_margin=options.get("notch_margin", 4),
        color=options.get("color"),
        elevation=options.get("elevation", 8),
    )


def generate_cupertino_app_bar_component(options: t.Options) -> t.Any:
    return ft.CupertinoAppBar(
        title=options.get("title"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        automatically_imply_leading=options.get("automatically_imply_leading", True),
        background_color=options.get("background_color"),
        elevation=options.get("elevation", 0),
    )


def generate_cupertino_navigation_bar_component(options: t.Options) -> t.Any:
    return ft.CupertinoNavigationBar(
        leading=options.get("leading"),
        middle=options.get("middle"),
        trailing=options.get("trailing"),
        background_color=options.get("background_color"),
        border=options.get("border", True),
    )


def generate_menu_bar_component(options: t.Options) -> t.Any:
    return ft.MenuBar(
        items=options.get("items", []),
        on_open=options.get("on_open"),
        on_close=options.get("on_close"),
        style=options.get("style"),
    )


def generate_navigation_bar_component(options: t.Options) -> t.Any:
    return ft.NavigationBar(
        selected_index=options.get("selected_index", 0),
        destinations=options.get("destinations", []),
        label_behavior=options.get("label_behavior", ft.NavigationDestinationLabelBehavior.ALWAYS_SHOW),
        on_change=options.get("on_change"),
        background_color=options.get("background_color"),
    )


def generate_navigation_drawer_component(options: t.Options) -> t.Any:
    return ft.NavigationDrawer(
        open=options.get("open", False),
        width=options.get("width", 250),
        content=options.get("content"),
        leading=options.get("leading"),
        footer=options.get("footer"),
        on_open_change=options.get("on_open_change"),
    )


def generate_navigation_rail_component(options: t.Options) -> t.Any:
    return ft.NavigationRail(
        selected_index=options.get("selected_index", 0),
        destinations=options.get("destinations", []),
        label_type=options.get("label_type", ft.NavigationRailLabelType.ALL),
        extended=options.get("extended", False),
        on_change=options.get("on_change"),
        background_color=options.get("background_color"),
    )