from . import t
from flet import (
    AutoComplete,
    AutofillGroup,
    Checkbox,
    Chip,
    CupertinoCheckbox,
    CupertinoRadio,
    CupertinoSlider,
    CupertinoSwitch,
    CupertinoTextField,
    Dropdown,
    dropdown,
    DropdownM2,
    Radio,
    RangeSlider,
    SearchBar,
    Slider,
    Switch,
    TextField,
)

# [ENUM] INPUT_SELECTION: InputSelection


def generate_auto_complete_component(options: t.Options) -> t.Any:
    return AutoComplete(
        suggestions=options.get("suggestions", []),
        on_select=options.get("on_select"),
        on_change=options.get("on_change"),
        width=options.get("width"),
        height=options.get("height"),
        value=options.get("value"),
        disabled=options.get("disabled"),
    )


def generate_autofill_group_component(options: t.Options) -> t.Any:
    return AutofillGroup(
        content=options.get("content"),
    )


def generate_checkbox_component(options: t.Options) -> t.Any:
    return Checkbox(
        label=options.get("label"),
        value=options.get("value"),
        tristate=options.get("tristate"),
        on_change=options.get("on_change"),
        fill_color=options.get("fill_color"),
        check_color=options.get("check_color"),
    )



def generate_chip_component(options: t.Options) -> t.Any:
    return Chip(
        label=options.get("label"),
        leading=options.get("leading"),
        trailing=options.get("trailing"),
        selected=options.get("selected"),
        on_select=options.get("on_select"),
        bgcolor=options.get("bgcolor"),
        disabled=options.get("disabled"),
    )


def generate_cupertino_checkbox_component(options: t.Options) -> t.Any:
    return CupertinoCheckbox(
        value=options.get("value"),
        on_change=options.get("on_change"),
        fill_color=options.get("fill_color"),
        check_color=options.get("check_color"),
    )


def generate_cupertino_radio_component(options: t.Options) -> t.Any:
    return CupertinoRadio(
        value=options.get("value"),
        group_value=options.get("group_value"),
        label=options.get("label"),
        on_change=options.get("on_change"),
    )



def generate_cupertino_slider_component(options: t.Options) -> t.Any:
    return CupertinoSlider(
        value=options.get("value", 0.0),
        min=options.get("min", 0.0),
        max=options.get("max", 1.0),
        on_change=options.get("on_change"),
        color=options.get("color"),
    )


def generate_cupertino_switch_component(options: t.Options) -> t.Any:
    return CupertinoSwitch(
        value=options.get("value"),
        on_change=options.get("on_change"),
    )


def generate_cupertino_text_field_component(options: t.Options) -> t.Any:
    return CupertinoTextField(
        placeholder=options.get("placeholder"),
        value=options.get("value"),
        prefix=options.get("prefix"),
        suffix=options.get("suffix"),
        on_change=options.get("on_change"),
        password=options.get("password"),
        read_only=options.get("read_only"),
        keyboard_type=options.get("keyboard_type"),
    )


def generate_dropdown_component(options: t.Options) -> t.Any:
    return Dropdown(
        border_width=options.get("border_width"),
        border_color=options.get('border_color'),
        focused_border_color=options.get('focused_border_color'),
        value=options.get("value"),
        options=options.get("options", []),
        label=options.get("label"),
        prefix_icon=options.get("prefix_icon"),
        on_change=options.get("on_change"),
        width=options.get("width"),
        # height=options.get("height"),
    )


def generate_dropdown_option_component(options: t.Options) -> t.Any:
    return dropdown.Option(
        text=options.get("text") or options.get("label") or "",
        key=options.get("key"),
        disabled=options.get("disabled")
    )



def generate_dropdown_m2_component(options: t.Options) -> t.Any:
    items = options.get("items", [])

    return DropdownM2(
        value=options.get("value"),
        options=[dropdown.Option(i) for i in items],
        label=options.get("label"),
        prefix_icon=options.get("prefix_icon"),
        on_change=options.get("on_change"),
        width=options.get("width"),
        height=options.get("height"),
    )



def generate_radio_component(options: t.Options) -> t.Any:
    return Radio(
        value=options.get("value"),
        group_value=options.get("group_value"),
        label=options.get("label"),
        on_change=options.get("on_change"),
        fill_color=options.get("fill_color"),
    )



def generate_range_slider_component(options: t.Options) -> t.Any:
    return RangeSlider(
        start=options.get("start", 0.0),
        end=options.get("end", 1.0),
        min=options.get("min", 0.0),
        max=options.get("max", 1.0),
        divisions=options.get("divisions"),
        on_change=options.get("on_change"),
    )


def generate_search_bar_component(options: t.Options) -> t.Any:
    return SearchBar(
        value=options.get("value"),
        on_change=options.get("on_change"),
        on_submit=options.get("on_submit"),
        on_clear=options.get("on_clear"),
        hint_text=options.get("hint_text", "Search"),
        width=options.get("width"),
    )



def generate_slider_component(options: t.Options) -> t.Any:
    return Slider(
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
    return Switch(
        label=options.get("label"),
        value=options.get("value"),
        on_change=options.get("on_change"),
        thumb_color=options.get("thumb_color"),
        track_color=options.get("track_color"),
    )


def generate_text_field_component(options: t.Options) -> t.Any:
    return TextField(
        label=options.get("label"),
        value=options.get("value"),
        width=options.get("width"),
        hint_text=options.get("hint_text"),
        border_color=options.get("border_color"),
        border_radius=options.get("border_radius"),
        border_width=options.get("border_width"),
        focused_border_color=options.get("focused_border_color"),
        password=options.get("password"),
        read_only=options.get("read_only"),
        multiline=options.get("multiline"),
        can_reveal_password=options.get('can_reveal_password'),
        on_change=options.get("on_change"),
        prefix_icon=options.get("prefix_icon"),
        suffix=options.get("suffix"),
        autofocus=options.get("autofocus"),
    )