from . import t
from flet import (
    Audio,
    AudioRecorder,
    Draggable,
    DragTarget,
    FilePicker,
    Flashlight,
    FletApp,
    Geolocator,
    GestureDetector,
    HapticFeedback,
    InteractiveViewer,
    # MergeSemantics,
    PermissionHandler,
    SelectionArea,
    Semantics,
    SemanticsService,
    ShaderMask,
    ShakeDetector,
    TransparentPointer,
    Video,
    WindowDragArea,
)


def generate_audio_component(options: t.Options) -> t.Any:
    return Audio(
        src=options.get("src", ""),
        autoplay=options.get("autoplay", False),
        loop=options.get("loop", False),
        volume=options.get("volume", 1.0),
    )


def generate_audio_recorder_component(options: t.Options) -> t.Any:
    return AudioRecorder(
        format=options.get("format", "wav"),
        on_record=options.get("on_record"),
        on_stop=options.get("on_stop"),
    )


def generate_draggable_component(options: t.Options) -> t.Any:
    return Draggable(
        content=options.get("content"),
        feedback=options.get("feedback"),
        axis=options.get("axis"),
        on_drag_end=options.get("on_drag_end"),
        data=options.get("data"),
    )



def generate_drag_target_component(options: t.Options) -> t.Any:
    return DragTarget(
        builder=options.get("builder"),
        on_accept=options.get("on_accept"),
        on_leave=options.get("on_leave"),
    )



def generate_file_picker_component(options: t.Options) -> t.Any:
    return FilePicker(
        allowed_extensions=options.get("allowed_extensions", []),
        allow_multiple=options.get("allow_multiple", False),
        on_result=options.get("on_result"),
        dialog_title=options.get("dialog_title", "Select file"),
    )



def generate_flashlight_component(options: t.Options) -> t.Any:
    return Flashlight(
        on_toggle=options.get("on_toggle"),
    )



def generate_flet_app_component(options: t.Options) -> t.Any:
    return FletApp(
        #
        #
        url=options.get("url"),
        reconnect_interval_ms=options.get("reconnect_interval_ms"),
        reconnect_timeout_ms=options.get("reconnect_timeout_ms"),
        show_app_startup_screen=options.get("show_app_startup_screen"),
        app_startup_screen_message=options.get("app_startup_screen_message"),
        on_error=options.get("on_error"),

        #
        # ConstrainedControl params
        #
        ref=options.get("ref"),
        width=options.get("width"),
        height=options.get("height"),
        left=options.get("left"),
        top=options.get("top"),
        right=options.get("right"),
        bottom=options.get("bottom"),
        expand=options.get("expand"),
        expand_loose=options.get("expand_loose"),
        opacity=options.get("opacity"),
        rotate=options.get("rotate"),
        scale=options.get("scale"),
        offset=options.get("offset"),
        aspect_ratio=options.get("aspect_ratio"),
        animate_opacity=options.get("animate_opacity"),
        animate_size=options.get("animate_size"),
        animate_position=options.get("animate_position"),
        animate_rotation=options.get("animate_rotation"),
        animate_scale=options.get("animate_scale"),
        animate_offset=options.get("animate_offset"),
        on_animation_end=options.get("on_animation_end"),
        tooltip=options.get("tooltip"),
        badge=options.get("badge"),
        visible=options.get("visible"),
        disabled=options.get("disabled"),
        data=options.get("data"),
    )


def generate_geolocator_component(options: t.Options) -> t.Any:
    return Geolocator(
        accuracy=options.get("accuracy"),
        on_position_changed=options.get("on_position_changed"),
        on_error=options.get("on_error"),
    )


def generate_gesture_detector_component(options: t.Options) -> t.Any:
    return GestureDetector(
        content=options.get("content"),
        on_tap=options.get("on_tap"),
        on_double_tap=options.get("on_double_tap"),
        on_long_press=options.get("on_long_press"),
        on_pan_update=options.get("on_pan_update"),
    )


def generate_haptic_feedback_component(options: t.Options) -> t.Any:
    return HapticFeedback(
        type=options.get("type"),
    )


def generate_interactive_viewer_component(options: t.Options) -> t.Any:
    return InteractiveViewer(
        content=options.get("content"),
        min_scale=options.get("min_scale", 1.0),
        max_scale=options.get("max_scale", 4.0),
        boundary_margin=options.get("boundary_margin", 0),
        on_interaction_end=options.get("on_interaction_end"),
    )


def generate_merge_semantics_component(options: t.Options) -> t.Any:
    # return MergeSemantics(
    #     content=options.get("content"),
    # )
    raise NotImplementedError


def generate_permission_handler_component(options: t.Options) -> t.Any:
    return PermissionHandler(
        permissions=options.get("permissions", []),
        on_permission_result=options.get("on_permission_result"),
    )


def generate_selection_area_component(options: t.Options) -> t.Any:
    return SelectionArea(
        content=options.get("content"),
    )


def generate_semantics_component(options: t.Options) -> t.Any:
    return Semantics(
        content=options.get("content"),
        label=options.get("label"),
        hint=options.get("hint"),
        enabled=options.get("enabled", True),
    )


def generate_semantics_service_component(options: t.Options) -> t.Any:
    return SemanticsService(
        announce=options.get("announce"),
    )


def generate_shader_mask_component(options: t.Options) -> t.Any:
    return ShaderMask(
        content=options.get("content"),
        shader=options.get("shader"),
        blend_mode=options.get("blend_mode"),
    )


def generate_shake_detector_component(options: t.Options) -> t.Any:
    return ShakeDetector(
        on_shake=options.get("on_shake"),
        sensitivity=options.get("sensitivity", 20),
    )


def generate_transparent_pointer_component(options: t.Options) -> t.Any:
    return TransparentPointer(
        content=options.get("content"),
        ignoring=options.get("ignoring", True),
    )


def generate_video_component(options: t.Options) -> t.Any:
    return Video(
        src=options.get("src", ""),
        width=options.get("width"),
        height=options.get("height"),
        autoplay=options.get("autoplay", False),
        loop=options.get("loop", False),
        volume=options.get("volume", 1.0),
        on_ended=options.get("on_ended"),
    )


def generate_window_drag_area_component(options: t.Options) -> t.Any:
    return WindowDragArea(
        content=options.get("content"),
    )
