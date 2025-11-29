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
    CUPERTINO: Annotated[str, "iOS style button."] = "Cupertino"
    CUPERTINO_FILLED: Annotated[str, "iOS filled button."] = "CupertinoFilled"
    ELEVATED: Annotated[str, "Material elevated button."] = "Elevated"
    FILLED: Annotated[str, "Material filled button."] = "Filled"
    FILLED_TONAL: Annotated[str, "Material filled tonal button."] = "FilledTonal"
    FLOATING_ACTION: Annotated[str, "Floating action button."] = "FloatingAction"
    ICON_BUTTON: Annotated[str, "Button with an icon."] = "IconButton"
    OUTLINED: Annotated[str, "Material outlined button."] = "Outlined"
    POPUP_MENU: Annotated[str, "Button that opens a menu."] = "PopupMenu"
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



def _search_enum_recursive(enum_cls: type[Enum], target: str) -> Optional[Enum]:
    """
    Busca dentro de enum_cls por:
      - member.name (ex: 'CARD')
      - member.value (ex: 'Card')
    E desce recursivamente se member.value for um Enum (classe).
    Retorna o membro encontrado ou None.
    """
    target_low = target.lower()

    for member in enum_cls:
        # 1) comparar pelo nome do membro (CARD)
        if member.name.lower() == target_low:
            return member

        # 2) comparar pelo valor do membro se for string ("Card")
        val = member.value
        if isinstance(val, str) and val.lower() == target_low:
            return member

        # 3) se o valor for uma classe Enum, procurar recursivamente dentro dela
        if isinstance(val, type) and issubclass(val, Enum):
            found = _search_enum_recursive(val, target)
            if found:
                return found

    return None


def get_enum_by_name(name: str):
    """
    Busca um membro Enum pelos formatos:
      - "CARD"                 -> encontra Layout.CARD (procura em todos os enums dentro de Controls)
      - "Card"                 -> encontra Layout.CARD (compara pelo value)
      - "Layout.CARD"          -> busca especificamente dentro do enum Layout
      - "Layout.Card"          -> idem
      - "Controls.Layout.CARD" -> também funciona (procura o enum Layout dentro de Controls)
    Retorna o membro Enum encontrado (por exemplo Layout.CARD) ou lança ValueError.
    """
    if not isinstance(name, str) or not name:
        raise ValueError("name deve ser uma string não vazia")

    # se veio no formato "Categoria.Membro" -> procurar categoria primeiro
    if "." in name:
        first, rest = name.split(".", 1)
        first_low = first.lower()

        # procurar qual enum dentro de Controls corresponde à primeira parte
        for top in Controls:
            top_val = top.value
            # top_val pode ser uma classe Enum (Layout, Navigation, ...)
            if isinstance(top_val, type) and issubclass(top_val, Enum):
                # comparar pelo nome da classe (Layout) ou pelo nome do membro Controls (LAYOUT)
                if top_val.__name__.lower() == first_low or top.name.lower() == first_low:
                    # agora buscar dentro do enum encontrado
                    res = _search_enum_recursive(top_val, rest)
                    if res:
                        return res

        # Se não achou o enum correspondente à primeira parte, tentar interpretar
        # como "EnumClass.Member" sem passar por Controls (ex: "Layout.CARD")
        # procura no módulo global por classe com nome `first`
        # (opcional: se não quiser essa heurística, pode remover)
        enum_cls = globals().get(first)
        if isinstance(enum_cls, type) and issubclass(enum_cls, Enum):
            res = _search_enum_recursive(enum_cls, rest)
            if res:
                return res

        raise ValueError(f"Categoria/enumeration '{first}' não encontrada dentro de Controls.")

    # sem ponto: procurar em todo o Controls recursivamente
    found = _search_enum_recursive(Controls, name)
    if found:
        return found

    raise ValueError(f"Enum/member '{name}' não encontrado em Controls.")


print(get_enum_by_name("CARD"))           # -> Layout.CARD
print(get_enum_by_name("Card"))           # -> Layout.CARD
print(get_enum_by_name("Layout.CARD"))    # -> Layout.CARD
print(get_enum_by_name("Navigation.AppBar"))  # -> Navigation.APP_BAR (também aceita value)
print(get_enum_by_name("AppBar")) 





ControlsType = Union[
    Layout,
    Navigation,
    InfoDisplay,
    Buttons,
    InputSelection,
    Dialogs,
    Charts,
    Animations,
    Utility,
]

def _generate_flet_class_map() -> Dict[str, Any]:
    class_map = {}
    for enum_class in ControlsType.__args__:
        for item in enum_class:
            class_map[item.value] = getattr(ft, item.value, None)
    return class_map


FLET_CLASS_MAP = _generate_flet_class_map()
print(FLET_CLASS_MAP)


def build_flet_control(control: ControlsType, options: dict):

    control_name = control.value
    cls = FLET_CLASS_MAP.get(control_name)

    if cls is None:
        raise ValueError(
            f"O controle '{control_name}' existe no seu Enum, "
            f"mas não existe no módulo flet. "
            f"Verifique se foi importado ou se o nome está correto."
        )

    try:
        return cls(**options)
    except TypeError as e:
        raise TypeError(
            f"Erro ao instanciar {control_name} com argumentos {options}. "
            f"Detalhes: {e}"
        )

c = build_flet_control(
    Layout.CONTAINER,
    {"padding": 20, "bgcolor": "red", "content": ft.Text("Olá!")}
)

# grid = build_flet_control(
#     Layout.GRID_VIEW,
#     {"runs_count": 3, "spacing": 10, "children": [ft.Text(str(i)) for i in range(9)]}
# )

# btn = build_flet_control(
#     Buttons.ELEVATED,
#     {"text": "Clique aqui", "on_click": lambda e: print("Clicado!")}
# )

# dialog = build_flet_control(
#     Dialogs.ALERT_DIALOG,
#     {"title": ft.Text("Alerta"), "content": ft.Text("Mensagem...")}
# )

