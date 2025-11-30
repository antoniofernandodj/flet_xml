from . import t
import flet as ft

# [ENUM] INPUT_SELECTION: InputSelection


def generate_auto_complete_component(options: t.Options) -> t.Any:
    return ft.AutoComplete(
        suggestions=options.get("suggestions", []),
        on_select=options.get("on_select"),
        on_change=options.get("on_change"),
        width=options.get("width"),
        height=options.get("height"),
        value=options.get("value", ""),
        disabled=options.get("disabled", False),
    )


def generate_autofill_group_component(options: t.Options) -> t.Any:
    return ft.AutofillGroup(
        content=options.get("content"),
    )


def generate_checkbox_component(options: t.Options) -> t.Any:
    return ft.Checkbox(
        label=options.get("label", ""),
        value=options.get("value", False),
        tristate=options.get("tristate", False),
        on_change=options.get("on_change"),
        fill_color=options.get("fill_color"),
        check_color=options.get("check_color"),
    )



def generate_chip_component(options: t.Options) -> t.Any:
    return ft.Chip(
        label=options.get("label", ""),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        selected=options.get("selected", False),
        on_select=options.get("on_select"),
        bgcolor=options.get("bgcolor"),
        disabled=options.get("disabled", False),
    )


def generate_cupertino_checkbox_component(options: t.Options) -> t.Any:
    return ft.CupertinoCheckbox(
        value=options.get("value", False),
        on_change=options.get("on_change"),
        fill_color=options.get("fill_color"),
        check_color=options.get("check_color"),
    )


def generate_cupertino_radio_component(options: t.Options) -> t.Any:
    return ft.CupertinoRadio(
        value=options.get("value"),
        group_value=options.get("group_value"),
        label=options.get("label"),
        on_change=options.get("on_change"),
    )



def generate_cupertino_slider_component(options: t.Options) -> t.Any:
    return ft.CupertinoSlider(
        value=options.get("value", 0.0),
        min=options.get("min", 0.0),
        max=options.get("max", 1.0),
        on_change=options.get("on_change"),
        color=options.get("color"),
    )


def generate_cupertino_switch_component(options: t.Options) -> t.Any:
    return ft.CupertinoSwitch(
        value=options.get("value", False),
        on_change=options.get("on_change"),
    )


def generate_cupertino_text_field_component(options: t.Options) -> t.Any:
    return ft.CupertinoTextField(
        placeholder=options.get("placeholder", ""),
        value=options.get("value", ""),
        prefix=options.get("prefix"),
        suffix=options.get("suffix"),
        on_change=options.get("on_change"),
        password=options.get("password", False),
        read_only=options.get("read_only", False),
        keyboard_type=options.get("keyboard_type"),
    )


def generate_dropdown_component(options: t.Options) -> t.Any:
    items = options.get("items", [])

    return ft.Dropdown(
        value=options.get("value"),
        options=[ft.dropdown.Option(i) for i in items],
        label=options.get("label"),
        prefix_icon=options.get("prefix_icon"),
        on_change=options.get("on_change"),
        width=options.get("width"),
        height=options.get("height"),
    )



def generate_dropdown_m2_component(options: t.Options) -> t.Any:
    items = options.get("items", [])

    return ft.DropdownM2(
        value=options.get("value"),
        options=[ft.dropdown.Option(i) for i in items],
        label=options.get("label"),
        prefix_icon=options.get("prefix_icon"),
        on_change=options.get("on_change"),
        width=options.get("width"),
        height=options.get("height"),
    )



def generate_radio_component(options: t.Options) -> t.Any:
    return ft.Radio(
        value=options.get("value"),
        group_value=options.get("group_value"),
        label=options.get("label"),
        on_change=options.get("on_change"),
        fill_color=options.get("fill_color"),
    )



def generate_range_slider_component(options: t.Options) -> t.Any:
    return ft.RangeSlider(
        start=options.get("start", 0.0),
        end=options.get("end", 1.0),
        min=options.get("min", 0.0),
        max=options.get("max", 1.0),
        divisions=options.get("divisions"),
        on_change=options.get("on_change"),
    )


def generate_search_bar_component(options: t.Options) -> t.Any:
    return ft.SearchBar(
        value=options.get("value", ""),
        on_change=options.get("on_change"),
        on_submit=options.get("on_submit"),
        on_clear=options.get("on_clear"),
        hint_text=options.get("hint_text", "Search"),
        width=options.get("width"),
    )



def generate_slider_component(options: t.Options) -> t.Any:
    return ft.Slider(
        value=options.get("value", 0.0),
        min=options.get("min", 0.0),
        max=options.get("max", 100.0),
        divisions=options.get("divisions"),
        label=options.get("label"),
        on_change=options.get("on_change"),
        color=options.get("color"),
        thumb_color=options.get("thumb_color"),
    )


def generate_switch_component(options: t.Options) -> t.Any:
    return ft.Switch(
        label=options.get("label"),
        value=options.get("value", False),
        on_change=options.get("on_change"),
        thumb_color=options.get("thumb_color"),
        track_color=options.get("track_color"),
    )



def generate_text_field_component(options: t.Options) -> t.Any:
    return ft.TextField(
        label=options.get("label"),
        value=options.get("value", ""),
        hint_text=options.get("hint_text"),
        password=options.get("password", False),
        read_only=options.get("read_only", False),
        multiline=options.get("multiline", False),
        on_change=options.get("on_change"),
        prefix_icon=options.get("prefix_icon"),
        suffix=options.get("suffix"),
        autofocus=options.get("autofocus", False),
    )