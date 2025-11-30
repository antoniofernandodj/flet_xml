import flet as ft
from . import t

# [ENUM] LAYOUT: Layout


def generate_card_component(options: t.Options) -> t.Any:
    return ft.Card(
        content=options.get("content"),
        elevation=options.get("elevation", 1),
        color=options.get("color"),
        shape=options.get("shape"),
        clip_behavior=options.get("clip_behavior", ft.ClipBehavior.ANTI_ALIAS),
        margin=options.get("margin"),
        padding=options.get("padding"),
    )


def generate_column_component(options: t.Options) -> t.Any:
    return ft.Column(
        controls=options.get("controls", []),
        alignment=options.get("alignment", ft.MainAxisAlignment.START),
        horizontal_alignment=options.get("horizontal_alignment", ft.CrossAxisAlignment.START),
        spacing=options.get("spacing", 0),
        expand=options.get("expand", False),
        scroll=options.get("scroll"),
    )


def generate_container_component(options: t.Options) -> t.Any:
    return ft.Container(
        content=options.get("content"),
        width=options.get("width"),
        height=options.get("height"),
        padding=options.get("padding"),
        margin=options.get("margin"),
        bgcolor=options.get("bgcolor"),
        border_radius=options.get("border_radius"),
        alignment=options.get("alignment"),
        expand=options.get("expand", False),
        on_click=options.get("on_click"),
    )


def generate_cupertino_list_tile_component(options: t.Options) -> t.Any:
    return ft.CupertinoListTile(
        title=options.get("title"),
        subtitle=options.get("subtitle"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        on_tap=options.get("on_tap"),
        selected=options.get("selected", False),
        enabled=options.get("enabled", True),
    )


def generate_data_table_component(options: t.Options) -> t.Any:
    return ft.DataTable(
        columns=options.get("columns", []),
        rows=options.get("rows", []),
        border=options.get("border"),
        heading_row_color=options.get("heading_row_color"),
        heading_row_height=options.get("heading_row_height"),
        data_row_height=options.get("data_row_height"),
        divider_thickness=options.get("divider_thickness"),
    )


def generate_dismissible_component(options: t.Options) -> t.Any:
    return ft.Dismissible(
        key=options.get("key"),
        content=options.get("content"),
        direction=options.get("direction", ft.DismissDirection.END_TO_START),
        on_dismissed=options.get("on_dismissed"),
        background=options.get("background"),
        secondary_background=options.get("secondary_background"),
    )


def generate_divider_component(options: t.Options) -> t.Any:
    return ft.Divider(
        color=options.get("color"),
        thickness=options.get("thickness", 1),
        height=options.get("height", 1),
        indent=options.get("indent", 0),
        end_indent=options.get("end_indent", 0),
    )


def generate_expansion_panel_list_component(options: t.Options) -> t.Any:
    return ft.ExpansionPanelList(
        children=options.get("children", []),
        expansion_callback=options.get("expansion_callback"),
        expanded=options.get("expanded", []),
        divider_color=options.get("divider_color"),
    )


def generate_expansion_tile_component(options: t.Options) -> t.Any:
    return ft.ExpansionTile(
        title=options.get("title"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        children=options.get("children", []),
        initially_expanded=options.get("initially_expanded", False),
        on_expand_change=options.get("on_expand_change"),
    )


def generate_grid_view_component(options: t.Options) -> t.Any:
    return ft.GridView(
        controls=options.get("controls", []),
        max_extent=options.get("max_extent"),
        child_aspect_ratio=options.get("child_aspect_ratio", 1),
        spacing=options.get("spacing", 0),
        run_spacing=options.get("run_spacing", 0),
        scroll=options.get("scroll"),
    )


def generate_list_tile_component(options: t.Options) -> t.Any:
    return ft.ListTile(
        title=options.get("title"),
        subtitle=options.get("subtitle"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        on_click=options.get("on_click"),
        selected=options.get("selected", False),
    )


def generate_list_view_component(options: t.Options) -> t.Any:
    return ft.ListView(
        controls=options.get("controls", []),
        spacing=options.get("spacing", 0),
        padding=options.get("padding"),
        expand=options.get("expand", True),
        scroll=options.get("scroll"),
    )


def generate_page_component(options: t.Options) -> t.Any:
    return ft.Page(
        title=options.get("title", ""),
        vertical_alignment=options.get("vertical_alignment", ft.MainAxisAlignment.START),
        horizontal_alignment=options.get("horizontal_alignment", ft.CrossAxisAlignment.START),
        controls=options.get("controls", []),
        bgcolor=options.get("bgcolor"),
    )


def generate_pagelet_component(options: t.Options) -> t.Any:
    return ft.Page(
        title=options.get("title", ""),
        controls=options.get("controls", []),
        scroll=options.get("scroll"),
    )


def generate_placeholder_component(options: t.Options) -> t.Any:
    return ft.Placeholder(
        width=options.get("width"),
        height=options.get("height"),
        color=options.get("color", ft.colors.TRANSPARENT),
        stroke_width=options.get("stroke_width", 1),
    )


def generate_reorderable_list_view_component(options: t.Options) -> t.Any:
    return ft.ReorderableListView(
        controls=options.get("controls", []),
        on_reorder=options.get("on_reorder"),
        padding=options.get("padding"),
        spacing=options.get("spacing", 0),
    )


def generate_responsive_row_component(options: t.Options) -> t.Any:
    return ft.ResponsiveRow(
        controls=options.get("controls", []),
        spacing=options.get("spacing", 0),
        run_spacing=options.get("run_spacing", 0),
        alignment=options.get("alignment", ft.MainAxisAlignment.START),
    )


def generate_row_component(options: t.Options) -> t.Any:
    return ft.Row(
        controls=options.get("controls", []),
        alignment=options.get("alignment", ft.MainAxisAlignment.START),
        vertical_alignment=options.get("vertical_alignment", ft.CrossAxisAlignment.START),
        spacing=options.get("spacing", 0),
        expand=options.get("expand", False),
        scroll=options.get("scroll"),
    )


def generate_safe_area_component(options: t.Options) -> t.Any:
    return ft.SafeArea(
        top=options.get("top", True),
        bottom=options.get("bottom", True),
        left=options.get("left", True),
        right=options.get("right", True),
        content=options.get("content"),
    )


def generate_stack_component(options: t.Options) -> t.Any:
    return ft.Stack(
        controls=options.get("controls", []),
        alignment=options.get("alignment", ft.Alignment.TOP_LEFT),
        expand=options.get("expand", False),
    )


def generate_tabs_component(options: t.Options) -> t.Any:
    return ft.Tabs(
        selected_index=options.get("selected_index", 0),
        tabs=options.get("tabs", []),
        animation_duration=options.get("animation_duration", 300),
        expand=options.get("expand", True),
    )


def generate_vertical_divider_component(options: t.Options) -> t.Any:
    return ft.VerticalDivider(
        width=options.get("width", 1),
        thickness=options.get("thickness", 1),
        color=options.get("color"),
        indent=options.get("indent", 0),
        end_indent=options.get("end_indent", 0),
    )


def generate_view_component(options: t.Options) -> t.Any:
    return ft.View(
        controls=options.get("controls", []),
        appbar=options.get("appbar"),
        bgcolor=options.get("bgcolor"),
        padding=options.get("padding"),
        scroll=options.get("scroll"),
    )
