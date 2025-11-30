from . import t
from flet import (
    Card,
    Column,
    Container,
    CupertinoListTile,
    DataTable,
    Dismissible,
    Divider,
    ExpansionPanelList,
    ExpansionTile,
    GridView,
    ListTile,
    ListView,
    Placeholder,
    ReorderableListView,
    ResponsiveRow,
    Row,
    SafeArea,
    Stack,
    Tabs,
    VerticalDivider,
    View
)
# [ENUM] LAYOUT: Layout


def generate_card_component(options: t.Options) -> t.Any:
    return Card(
        content=options.get("content"),
        elevation=options.get("elevation"),
        color=options.get("color"),
        shape=options.get("shape"),
        clip_behavior=options.get("clip_behavior"),
        margin=options.get("margin"),
        padding=options.get("padding"),
    )


def generate_column_component(options: t.Options) -> t.Any:
    return Column(
        controls=options.get("controls", []),
        alignment=options.get("alignment"),
        horizontal_alignment=options.get("horizontal_alignment"),
        spacing=options.get("spacing"),
        expand=options.get("expand"),
        scroll=options.get("scroll"),
    )


def generate_container_component(options: t.Options) -> t.Any:
    return Container(
        content=options.get("content"),
        width=options.get("width"),
        expand=options.get("expand"),
        height=options.get("height"),
        padding=options.get("padding"),
        margin=options.get("margin"),
        bgcolor=options.get("bgcolor"),
        border_radius=options.get("border_radius"),
        alignment=options.get("alignment"),
        on_click=options.get("on_click"),
    )


def generate_cupertino_list_tile_component(options: t.Options) -> t.Any:
    return CupertinoListTile(
        title=options.get("title"),
        subtitle=options.get("subtitle"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        on_tap=options.get("on_tap"),
        selected=options.get("selected"),
        enabled=options.get("enabled"),
    )


def generate_data_table_component(options: t.Options) -> t.Any:
    return DataTable(
        columns=options.get("columns", []),
        rows=options.get("rows", []),
        border=options.get("border"),
        heading_row_color=options.get("heading_row_color"),
        heading_row_height=options.get("heading_row_height"),
        data_row_height=options.get("data_row_height"),
        divider_thickness=options.get("divider_thickness"),
    )


def generate_dismissible_component(options: t.Options) -> t.Any:
    return Dismissible(
        key=options.get("key"),
        content=options.get("content"),
        direction=options.get("direction"),
        on_dismissed=options.get("on_dismissed"),
        background=options.get("background"),
        secondary_background=options.get("secondary_background"),
    )


def generate_divider_component(options: t.Options) -> t.Any:
    return Divider(
        color=options.get("color"),
        thickness=options.get("thickness"),
        height=options.get("height"),
        indent=options.get("indent"),
        end_indent=options.get("end_indent"),
    )


def generate_expansion_panel_list_component(options: t.Options) -> t.Any:
    return ExpansionPanelList(
        children=options.get("children", []),
        expansion_callback=options.get("expansion_callback"),
        expanded=options.get("expanded", []),
        divider_color=options.get("divider_color"),
    )


def generate_expansion_tile_component(options: t.Options) -> t.Any:
    return ExpansionTile(
        title=options.get("title"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        children=options.get("children", []),
        initially_expanded=options.get("initially_expanded", False),
        on_expand_change=options.get("on_expand_change"),
    )


def generate_grid_view_component(options: t.Options) -> t.Any:
    return GridView(
        controls=options.get("controls", []),
        max_extent=options.get("max_extent"),
        child_aspect_ratio=options.get("child_aspect_ratio"),
        spacing=options.get("spacing"),
        run_spacing=options.get("run_spacing"),
        scroll=options.get("scroll"),
    )


def generate_list_tile_component(options: t.Options) -> t.Any:
    return ListTile(
        title=options.get("title"),
        subtitle=options.get("subtitle"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        on_click=options.get("on_click"),
        selected=options.get("selected"),
    )


def generate_list_view_component(options: t.Options) -> t.Any:
    return ListView(
        controls=options.get("controls", []),
        spacing=options.get("spacing"),
        padding=options.get("padding"),
        expand=options.get("expand", True),
        scroll=options.get("scroll"),
    )


def generate_placeholder_component(options: t.Options) -> t.Any:
    return Placeholder(
        width=options.get("width"),
        height=options.get("height"),
        color=options.get("color"),
        stroke_width=options.get("stroke_width", 1),
    )


def generate_reorderable_list_view_component(options: t.Options) -> t.Any:
    return ReorderableListView(
        controls=options.get("controls", []),
        on_reorder=options.get("on_reorder"),
        padding=options.get("padding"),
        spacing=options.get("spacing", 0),
    )


def generate_responsive_row_component(options: t.Options) -> t.Any:
    return ResponsiveRow(
        controls=options.get("controls", []),
        spacing=options.get("spacing"),
        run_spacing=options.get("run_spacing"),
        alignment=options.get("alignment"),
    )


def generate_row_component(options: t.Options) -> t.Any:
    return Row(
        controls=options.get("controls", []),
        alignment=options.get("alignment"),
        vertical_alignment=(
            options.get("vertical_alignment") or
            options.get("verticalalignment")
        ),
        spacing=options.get("spacing"),
        expand=options.get("expand"),
        scroll=options.get("scroll"),
    )


def generate_safe_area_component(options: t.Options) -> t.Any:
    return SafeArea(
        top=options.get("top"),
        bottom=options.get("bottom"),
        left=options.get("left"),
        right=options.get("right"),
        content=options.get("content"),
    )


def generate_stack_component(options: t.Options) -> t.Any:
    return Stack(
        controls=options.get("controls", []),
        alignment=options.get("alignment"),
        expand=options.get("expand"),
    )


def generate_tabs_component(options: t.Options) -> t.Any:
    return Tabs(
        selected_index=options.get("selected_index"),
        tabs=options.get("tabs", []),
        animation_duration=options.get("animation_duration"),
        expand=options.get("expand", True),
    )


def generate_vertical_divider_component(options: t.Options) -> t.Any:
    return VerticalDivider(
        width=options.get("width"),
        thickness=options.get("thickness"),
        color=options.get("color"),
        indent=options.get("indent"),
        end_indent=options.get("end_indent"),
    )


def generate_view_component(options: t.Options) -> t.Any:
    return View(
        controls=options.get("controls", []),
        appbar=options.get("appbar"),
        bgcolor=options.get("bgcolor"),
        padding=options.get("padding"),
        scroll=options.get("scroll"),
    )
