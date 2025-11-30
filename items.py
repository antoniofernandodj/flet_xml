from typing import Any, Dict, Optional, Union
from enum import Enum
from typing import Annotated
import flet as ft


class Layout(Enum):
    CARD: Annotated[
        str,
        "A material design card: a panel with slightly rounded corners and an elevation shadow."
    ] = "Card"

    COLUMN: Annotated[
        str,
        "A control that displays its children in a vertical array."
    ] = "Column"
    CONTAINER: Annotated[
        str,
        "Container allows to decorate a control with background color and border and position it with padding, margin and alignment."
    ] = "Container"
    CUPERTINO_LIST_TILE: Annotated[
        str,
        "An iOS-style list tile. The CupertinoListTile is a Cupertino equivalent of Material ListTile."
    ] = "CupertinoListTile"
    DATA_TABLE: Annotated[
        str,
        "A Material Design data table."
    ] = "DataTable"
    DISMISSIBLE: Annotated[
        str,
        "A control that can be dismissed by dragging in the indicated dismiss_direction."
    ] = "Dismissible"
    DIVIDER: Annotated[
        str,
        "A thin horizontal line, with padding on either side."
    ] = "Divider"
    EXPANSION_PANEL_LIST: Annotated[
        str,
        "A material expansion panel list that lays out its children and animates expansions."
    ] = "ExpansionPanelList"
    EXPANSION_TILE: Annotated[
        str,
        "A single-line ListTile with an expansion arrow icon that expands or collapses the tile to reveal or hide its children."
    ] = "ExpansionTile"
    GRID_VIEW: Annotated[
        str,
        "A scrollable, 2D array of controls."
    ] = "GridView"
    LIST_TILE: Annotated[
        str,
        "A single fixed-height row that typically contains some text as well as a leading or trailing icon."
    ] = "ListTile"
    LIST_VIEW: Annotated[
        str,
        "A scrollable list of controls arranged linearly."
    ] = "ListView"
    PAGE: Annotated[
        str,
        "Page is a container for View controls."
    ] = "Page"
    PAGELET: Annotated[
        str,
        "Pagelet implements the basic Material Design visual layout structure."
    ] = "Pagelet"
    PLACEHOLDER: Annotated[
        str,
        "A control that draws a box that represents where other widgets will one day be added."
    ] = "Placeholder"
    REORDERABLE_LIST_VIEW: Annotated[
        str,
        "A control that allows the user to reorder its children by dragging a handle."
    ] = "ReorderableListView"
    RESPONSIVE_ROW: Annotated[
        str,
        "ResponsiveRow borrows the idea of grid layout from Bootstrap web framework."
    ] = "ResponsiveRow"
    ROW: Annotated[
        str,
        "A control that displays its children in a horizontal array."
    ] = "Row"
    SAFE_AREA: Annotated[
        str,
        "A control that insets its content by sufficient padding to avoid intrusions by the operating system."
    ] = "SafeArea"
    STACK: Annotated[
        str,
        "A control that positions its children on top of each other."
    ] = "Stack"
    TABS: Annotated[
        str,
        "Control for navigating multiple category views via tabs."
    ] = "Tabs"
    VERTICAL_DIVIDER: Annotated[
        str,
        "A thin vertical line, with padding on either side."
    ] = "VerticalDivider"
    VIEW: Annotated[
        str,
        "View is the top most container for all other controls."
    ] = "View"


class Navigation(Enum):
    APP_BAR: Annotated[
        str,
        "A material design app bar."
    ] = "AppBar"
    BOTTOM_APP_BAR: Annotated[
        str,
        "A material design bottom app bar."
    ] = "BottomAppBar"
    CUPERTINO_APP_BAR: Annotated[
        str,
        "An iOS-styled application bar."
    ] = "CupertinoAppBar"
    CUPERTINO_NAVIGATION_BAR: Annotated[
        str,
        "An iOS-styled bottom navigation tab bar."
    ] = "CupertinoNavigationBar"
    MENU_BAR: Annotated[
        str,
        "A menu bar that manages cascading child menus."
    ] = "MenuBar"
    NAVIGATION_BAR: Annotated[
        str,
        "Material 3 Navigation Bar component."
    ] = "NavigationBar"
    NAVIGATION_DRAWER: Annotated[
        str,
        "Material Design Navigation Drawer component."
    ] = "NavigationDrawer"
    NAVIGATION_RAIL: Annotated[
        str,
        "A material widget displayed at app edge for navigation."
    ] = "NavigationRail"


class InfoDisplay(Enum):
    CANVAS: Annotated[
        str,
        "Canvas is a control for drawing arbitrary graphics using primitives."
    ] = "Canvas"
    CIRCLE_AVATAR: Annotated[
        str,
        "A circle that represents a user."
    ] = "CircleAvatar"
    CUPERTINO_ACTIVITY_INDICATOR: Annotated[
        str,
        "An iOS-style activity indicator that spins clockwise."
    ] = "CupertinoActivityIndicator"
    ICON: Annotated[
        str,
        "Displays a Material icon."
    ] = "Icon"
    IMAGE: Annotated[
        str,
        "A graphic representation such as a photo or illustration."
    ] = "Image"
    MARKDOWN: Annotated[
        str,
        "Control for rendering text in markdown format."
    ] = "Markdown"
    TEXT: Annotated[
        str,
        "Control for displaying text."
    ] = "Text"
    PROGRESS_BAR: Annotated[
        str,
        "A material design linear progress indicator."
    ] = "ProgressBar"
    PROGRESS_RING: Annotated[
        str,
        "A circular progress indicator displaying spinning animation."
    ] = "ProgressRing"
    WEBVIEW: Annotated[
        str,
        "Displays web content."
    ] = "WebView"


class Buttons(Enum):
    CUPERTINO: Annotated[str, "iOS style button."] = "CupertinoButton"
    CUPERTINO_FILLED: Annotated[str, "iOS filled button."] = "CupertinoFilledButton"
    ELEVATED: Annotated[str, "Material elevated button."] = "ElevatedButton"
    FILLED: Annotated[str, "Material filled button."] = "FilledButton"
    FILLED_TONAL: Annotated[str, "Material filled tonal button."] = "FilledTonalButton"
    FLOATING_ACTION: Annotated[str, "Floating action button."] = "FloatingActionButton"
    ICON_BUTTON: Annotated[str, "Button with an icon."] = "IconButton"
    OUTLINED: Annotated[str, "Material outlined button."] = "OutlinedButton"
    # POPUP_MENU: Annotated[str, "Button that opens a menu."] = "PopupMenu"
    TEXT_BUTTON: Annotated[str, "Borderless text button."] = "TextButton"


class InputSelection(Enum):
    AUTOCOMPLETE: Annotated[
        str,
        "Helps the user select by entering text and choosing suggestions."
    ] = "AutoComplete"
    AUTOFILL_GROUP: Annotated[
        str,
        "Groups autofillable controls such as TextField."
    ] = "AutofillGroup"
    CHECKBOX: Annotated[
        str,
        "Selection control supporting on/off state."
    ] = "Checkbox"
    CHIP: Annotated[
        str,
        "Compact element representing text, entity, or action."
    ] = "Chip"
    CUPERTINO_CHECKBOX: Annotated[
        str,
        "macOS style checkbox."
    ] = "CupertinoCheckbox"
    CUPERTINO_RADIO: Annotated[
        str,
        "macOS style radio button."
    ] = "CupertinoRadio"
    CUPERTINO_SLIDER: Annotated[
        str,
        "macOS style slider control."
    ] = "CupertinoSlider"
    CUPERTINO_SWITCH: Annotated[
        str,
        "iOS-style switch."
    ] = "CupertinoSwitch"
    CUPERTINO_TEXTFIELD: Annotated[
        str,
        "iOS-style text field."
    ] = "CupertinoTextField"
    DROPDOWN: Annotated[
        str,
        "Material dropdown for selecting an item."
    ] = "Dropdown"
    DROPDOWN_M2: Annotated[
        str,
        "Material button for selecting list items."
    ] = "DropdownM2"
    RADIO: Annotated[
        str,
        "Single-choice radio selection control."
    ] = "Radio"
    RANGE_SLIDER: Annotated[
        str,
        "Material range slider for selecting value intervals."
    ] = "RangeSlider"
    SEARCH_BAR: Annotated[
        str,
        "Material search bar control."
    ] = "SearchBar"
    SLIDER: Annotated[
        str,
        "Material slider for continuous values."
    ] = "Slider"
    SWITCH: Annotated[
        str,
        "Toggle switch for boolean values."
    ] = "Switch"
    TEXTFIELD: Annotated[
        str,
        "Material design text field."
    ] = "TextField"


class Dialogs(Enum):
    ALERT_DIALOG: Annotated[str, "Material alert dialog."] = "AlertDialog"
    BANNER: Annotated[str, "Important message shown with user actions."] = "Banner"
    BOTTOM_SHEET: Annotated[str, "Material modal bottom sheet."] = "BottomSheet"
    CUPERTINO_ACTION_SHEET: Annotated[str, "iOS action sheet."] = "CupertinoActionSheet"
    CUPERTINO_ALERT_DIALOG: Annotated[str, "iOS alert dialog."] = "CupertinoAlertDialog"
    CUPERTINO_BOTTOM_SHEET: Annotated[str, "iOS bottom sheet."] = "CupertinoBottomSheet"
    CUPERTINO_CONTEXT_MENU: Annotated[str, "Full-screen modal via long-press."] = "CupertinoContextMenu"
    CUPERTINO_DATE_PICKER: Annotated[str, "iOS date/time picker."] = "CupertinoDatePicker"
    CUPERTINO_PICKER: Annotated[str, "iOS picker wheel."] = "CupertinoPicker"
    CUPERTINO_TIMER_PICKER: Annotated[str, "iOS countdown timer picker."] = "CupertinoTimerPicker"
    DATE_PICKER: Annotated[str, "Material date picker."] = "DatePicker"
    SNACKBAR: Annotated[str, "Temporary bottom message with optional action."] = "SnackBar"
    TIME_PICKER: Annotated[str, "Material time picker."] = "TimePicker"


class Charts(Enum):
    BAR: Annotated[str, "Draws a bar chart."] = "BarChart"
    LINE: Annotated[str, "Draws a line chart."] = "LineChart"
    MATPLOTLIB: Annotated[str, "Displays Matplotlib chart."] = "MatplotlibChart"
    PIE: Annotated[str, "Draws a pie chart."] = "PieChart"
    PLOTLY: Annotated[str, "Displays Plotly chart."] = "PlotlyChart"


class Animations(Enum):
    ANIMATED_SWITCHER: Annotated[
        str,
        "Control that cross-fades between old and new widgets."
    ] = "AnimatedSwitcher"
    LOTTIE: Annotated[
        str,
        "Displays an animation from a Lottie file."
    ] = "Lottie"
    RIVE: Annotated[
        str,
        "Displays an animation from a Rive file."
    ] = "Rive"


class Utility(Enum):
    AUDIO: Annotated[str, "Control for playing multiple audio files."] = "Audio"
    AUDIO_RECORDER: Annotated[str, "Records audio from microphone."] = "AudioRecorder"
    DRAGGABLE: Annotated[str, "Draggable control."] = "Draggable"
    DRAG_TARGET: Annotated[str, "Completes drag operations."] = "DragTarget"
    FILE_PICKER: Annotated[str, "Native file explorer picker."] = "FilePicker"
    FLASHLIGHT: Annotated[str, "Device flashlight control."] = "Flashlight"
    FLET_APP: Annotated[str, "Embeds another Flet app."] = "FletApp"
    GEOLOCATOR: Annotated[str, "Gets GPS position."] = "Geolocator"
    GESTURE_DETECTOR: Annotated[str, "Detects gestures."] = "GestureDetector"
    HAPTIC_FEEDBACK: Annotated[str, "Device haptic feedback."] = "HapticFeedback"
    INTERACTIVE_VIEWER: Annotated[str, "Pan/zoom/rotate content."] = "InteractiveViewer"
    MERGE_SEMANTICS: Annotated[str, "Merges semantic nodes."] = "MergeSemantics"
    PERMISSION_HANDLER: Annotated[str, "Checks and requests permissions."] = "PermissionHandler"
    SELECTION_AREA: Annotated[str, "Enables content selection."] = "SelectionArea"
    SEMANTICS: Annotated[str, "Semantic description wrapper."] = "Semantics"
    SEMANTICS_SERVICE: Annotated[str, "Access platform accessibility."] = "SemanticsService"
    SHADER_MASK: Annotated[str, "Applies shader mask to child."] = "ShaderMask"
    SHAKE_DETECTOR: Annotated[str, "Detects phone shakes."] = "ShakeDetector"
    TRANSPARENT_POINTER: Annotated[str, "Allows gestures to pass through."] = "TransparentPointer"
    VIDEO: Annotated[str, "Video player control."] = "Video"
    WINDOW_DRAG_AREA: Annotated[str, "Allows window dragging."] = "WindowDragArea"








class Controls(Enum):
    LAYOUT = Layout
    NAVIGATION = Navigation
    INFO_DISPLAY = InfoDisplay
    BUTTONS = Buttons
    INPUT_SELECTION = InputSelection
    DIALOGS = Dialogs
    CHATS = Charts
    ANIMATIONS = Animations
    UTILITY = Utility



from enum import Enum


def pascal_case_to_snake_case(string: str) -> str:
    # Coloca underscore entre:
    # 1) letra minúscula/numero seguido de letra maiúscula  → aA, 1A
    # 2) sequências tipo: ABCWord → ABC_Word
    import re
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)
    return string.lower()


def generate_def(enum: str):

    enum_name = pascal_case_to_snake_case(enum)

    print(f'  "{enum}": generate_{enum_name}_component,')


def walk_enum(e):
    """Percorre recursivamente enums aninhados e imprime todos os valores."""
    if not issubclass(e, Enum):
        return

    for member in e:
        if isinstance(member.value, type) and issubclass(member.value, Enum):
            # Caso seja um Enum dentro de outro Enum
            print(f"  # [ENUM] {member.name}: {member.value.__name__}")
            walk_enum(member.value)
        else:
            # Caso seja um item normal (str, int, ...)
            # print(f"{e.__name__}.{member.name} = {member.value}")
            generate_def(member.value)
