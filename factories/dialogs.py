from . import t
from flet import (
    AlertDialog,
    Banner,
    BottomSheet,
    CupertinoActionSheet,
    CupertinoAlertDialog,
    CupertinoBottomSheet,
    CupertinoContextMenu,
    CupertinoDatePicker,
    CupertinoPicker,
    CupertinoTimerPicker,
    DatePicker,
    SnackBar,
    TimePicker,
)



def generate_alert_dialog_component(options: t.Options) -> t.Any:
    return AlertDialog(
        modal=options.get("modal", False),
        title=options.get("title"),
        content=options.get("content"),
        actions=options.get("actions", []),
        actions_alignment=options.get("actions_alignment"),
        on_dismiss=options.get("on_dismiss"),
    )


def generate_banner_component(options: t.Options) -> t.Any:
    return Banner(
        bgcolor=options.get("bgcolor"),
        leading=options.get("leading"),
        content=options.get("content"),
        actions=options.get("actions", []),
        force_actions_below=options.get("force_actions_below", False),
        elevation=options.get("elevation"),
    )



def generate_bottom_sheet_component(options: t.Options) -> t.Any:
    return BottomSheet(
        content=options.get("content"),
        open=options.get("open", False),
        on_dismiss=options.get("on_dismiss")
    )


def generate_cupertino_action_sheet_component(options: t.Options) -> t.Any:
    return CupertinoActionSheet(
        title=options.get("title"),
        message=options.get("message"),
        actions=options.get("actions", []),
        cancel=options.get("cancel")
    )


def generate_cupertino_alert_dialog_component(options: t.Options) -> t.Any:
    return CupertinoAlertDialog(
        title=options.get("title"),
        content=options.get("content"),
        actions=options.get("actions", [])
    )



def generate_cupertino_bottom_sheet_component(options: t.Options) -> t.Any:
    return CupertinoBottomSheet(
        content=options.get("content"),
        open=options.get("open", False),
        on_dismiss=options.get("on_dismiss")
    )



def generate_cupertino_context_menu_component(options: t.Options) -> t.Any:
    return CupertinoContextMenu(
        actions=options.get("actions", []),
        child=options.get("child")
    )



def generate_cupertino_date_picker_component(options: t.Options) -> t.Any:
    return CupertinoDatePicker(
        mode=options.get("mode"),
        initial_date=options.get("initial_date"),
        minimum_date=options.get("minimum_date"),
        maximum_date=options.get("maximum_date"),
        on_change=options.get("on_change")
    )



def generate_cupertino_picker_component(options: t.Options) -> t.Any:
    return CupertinoPicker(
        optionss=options.get("optionss", []),
        looping=options.get("looping", False),
        on_change=options.get("on_change"),
        diameter_ratio=options.get("diameter_ratio"),
        background=options.get("background"),
        squeeze=options.get("squeeze"),
    )



def generate_cupertino_timer_picker_component(options: t.Options) -> t.Any:
    return CupertinoTimerPicker(
        mode=options.get("mode"),
        initial_timer_duration=options.get("initial_timer_duration"),
        on_change=options.get("on_change")
    )



def generate_date_picker_component(options: t.Options) -> t.Any:
    return DatePicker(
        on_change=options.get("on_change"),
        on_dismiss=options.get("on_dismiss"),
        first_date=options.get("first_date"),
        last_date=options.get("last_date"),
        current_date=options.get("current_date")
    )



def generate_snack_bar_component(options: t.Options) -> t.Any:
    return SnackBar(
        content=options.get("content"),
        action=options.get("action"),
        bgcolor=options.get("bgcolor"),
        duration=options.get("duration"),
        open=options.get("open", False)
    )



def generate_time_picker_component(options: t.Options) -> t.Any:
    return TimePicker(
        on_change=options.get("on_change"),
        on_dismiss=options.get("on_dismiss"),
        value=options.get("value")
    )
