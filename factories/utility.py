# [ENUM] UTILITY: Utility

import flet as ft
from . import t


import flet as ft
from . import t


def generate_audio_component(options: t.Options) -> t.Any:
    return ft.Audio(
        src=options.get("src", ""),
        autoplay=options.get("autoplay", False),
        loop=options.get("loop", False),
        volume=options.get("volume", 1.0),
    )


def generate_audio_recorder_component(options: t.Options) -> t.Any:
    return ft.AudioRecorder(
        format=options.get("format", "wav"),
        on_record=options.get("on_record"),
        on_stop=options.get("on_stop"),
    )


def generate_draggable_component(options: t.Options) -> t.Any:
    return ft.Draggable(
        content=options.get("content"),
        feedback=options.get("feedback"),
        axis=options.get("axis"),
        on_drag_end=options.get("on_drag_end"),
        data=options.get("data"),
    )



def generate_drag_target_component(options: t.Options) -> t.Any:
    return ft.DragTarget(
        builder=options.get("builder"),
        on_accept=options.get("on_accept"),
        on_leave=options.get("on_leave"),
    )



def generate_file_picker_component(options: t.Options) -> t.Any:
    return ft.FilePicker(
        allowed_extensions=options.get("allowed_extensions", []),
        allow_multiple=options.get("allow_multiple", False),
        on_result=options.get("on_result"),
        dialog_title=options.get("dialog_title", "Select file"),
    )



def generate_flashlight_component(options: t.Options) -> t.Any:
    return ft.Flashlight(
        on_toggle=options.get("on_toggle"),
    )



def generate_flet_app_component(options: t.Options) -> t.Any:
    return ft.FletApp(
        name=options.get("name", "Flet App"),
        target=options.get("target"),
        view=options.get("view", ft.WEB_BROWSER),
    )


def generate_geolocator_component(options: t.Options) -> t.Any:
    return ft.Geolocator(
        accuracy=options.get("accuracy", ft.GeolocationAccuracy.HIGH),
        on_position_changed=options.get("on_position_changed"),
        on_error=options.get("on_error"),
    )


def generate_gesture_detector_component(options: t.Options) -> t.Any:
    return ft.GestureDetector(
        content=options.get("content"),
        on_tap=options.get("on_tap"),
        on_double_tap=options.get("on_double_tap"),
        on_long_press=options.get("on_long_press"),
        on_pan_update=options.get("on_pan_update"),
    )


def generate_haptic_feedback_component(options: t.Options) -> t.Any:
    return ft.HapticFeedback(
        type=options.get("type", ft.HapticFeedbackType.LIGHT_IMPACT),
    )


def generate_interactive_viewer_component(options: t.Options) -> t.Any:
    return ft.InteractiveViewer(
        content=options.get("content"),
        min_scale=options.get("min_scale", 1.0),
        max_scale=options.get("max_scale", 4.0),
        boundary_margin=options.get("boundary_margin", 0),
        on_interaction_end=options.get("on_interaction_end"),
    )


def generate_merge_semantics_component(options: t.Options) -> t.Any:
    return ft.MergeSemantics(
        content=options.get("content"),
    )


def generate_permission_handler_component(options: t.Options) -> t.Any:
    return ft.PermissionHandler(
        permissions=options.get("permissions", []),
        on_permission_result=options.get("on_permission_result"),
    )


def generate_selection_area_component(options: t.Options) -> t.Any:
    return ft.SelectionArea(
        content=options.get("content"),
    )


def generate_semantics_component(options: t.Options) -> t.Any:
    return ft.Semantics(
        content=options.get("content"),
        label=options.get("label"),
        hint=options.get("hint"),
        enabled=options.get("enabled", True),
    )


def generate_semantics_service_component(options: t.Options) -> t.Any:
    return ft.SemanticsService(
        announce=options.get("announce"),
    )


def generate_shader_mask_component(options: t.Options) -> t.Any:
    return ft.ShaderMask(
        content=options.get("content"),
        shader=options.get("shader"),
        blend_mode=options.get("blend_mode", ft.BlendMode.SRC_IN),
    )


def generate_shake_detector_component(options: t.Options) -> t.Any:
    return ft.ShakeDetector(
        on_shake=options.get("on_shake"),
        sensitivity=options.get("sensitivity", 20),
    )


def generate_transparent_pointer_component(options: t.Options) -> t.Any:
    return ft.TransparentPointer(
        content=options.get("content"),
        ignoring=options.get("ignoring", True),
    )


def generate_video_component(options: t.Options) -> t.Any:
    return ft.Video(
        src=options.get("src", ""),
        width=options.get("width"),
        height=options.get("height"),
        autoplay=options.get("autoplay", False),
        loop=options.get("loop", False),
        volume=options.get("volume", 1.0),
        on_ended=options.get("on_ended"),
    )


def generate_window_drag_area_component(options: t.Options) -> t.Any:
    return ft.WindowDragArea(
        content=options.get("content"),
    )
