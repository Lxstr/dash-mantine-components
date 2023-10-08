# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DatePicker(Component):
    """A DatePicker component.
Capture date input from user. For more information, see: https://mantine.dev/dates/date-picker/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowFreeInput (boolean; optional):
    Allow free input.

- allowLevelChange (boolean; optional):
    Allow to change level (date - month - year).

- amountOfMonths (number; optional):
    Amount of months.

- bg (boolean | number | string | dict | list; optional):
    Mantine Style System Props.

- bgp (string; optional):
    Mantine Style System Props.

- bgr (a value equal to: 'initial', 'inherit', 'repeat', 'repeat-x', 'repeat-y', 'no-repeat'; optional):
    Mantine Style System Props.

- bgsz (string | number; optional):
    Mantine Style System Props.

- bottom (string | number; optional):
    Mantine Style System Props.

- c (boolean | number | string | dict | list; optional):
    Mantine Style System Props.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- clearButtonLabel (string; optional):
    aria-label for clear button.

- clearButtonTabIndex (a value equal to: 0, -1; optional):
    Set the clear button tab index to disabled or default after input
    field.

- clearable (boolean; optional):
    Allow to clear value.

- clickOutsideEvents (list of strings; optional):
    Events that should trigger outside clicks.

- closeCalendarOnChange (boolean; optional):
    Set to False to force dropdown to stay open after date was
    selected.

- debounce (number; optional):
    Debounce time.

- description (a list of or a singular dash component, string or number; optional):
    Input description, displayed after label.

- disableOutsideEvents (boolean; optional):
    When True dates that are outside of given month cannot be clicked
    or focused.

- disabled (boolean; optional):
    Disabled input state.

- disabledDates (list of strings; optional):
    Specifies additional days between min_date_allowed and
    max_date_allowed that should be disabled.

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- dropdownPosition (a value equal to: 'bottom-start', 'top-start', 'flip'; optional):
    Dropdown positioning behavior.

- dropdownType (a value equal to: 'popover', 'modal'; optional):
    Where to show calendar in modal or popover.

- error (a list of or a singular dash component, string or number; optional):
    Displays error message after input.

- ff (string; optional):
    Mantine Style System Props.

- firstDayOfWeek (a value equal to: 'sunday', 'monday'; optional):
    Set first day of the week.

- fixOnBlur (boolean; optional):
    call onChange with last valid value onBlur.

- focusable (boolean; optional):
    Should focusable days have tabIndex={0}?.

- fs (a value equal to: 'initial', 'inherit', 'normal', 'italic', 'oblique'; optional):
    Mantine Style System Props.

- fullWidth (boolean; optional):
    Set to True to make calendar take 100% of container width.

- fw (number; optional):
    Mantine Style System Props.

- fz (number; optional):
    Mantine Style System Props.

- h (number; optional):
    Mantine Style System Props.

- hideOutsideDates (boolean; optional):
    Remove outside dates.

- hideWeekdays (boolean; optional):
    Set to False to remove weekdays row.

- icon (a list of or a singular dash component, string or number; optional):
    Adds icon on the left side of input.

- iconWidth (number; optional):
    Width of icon section in px.

- initialLevel (a value equal to: 'date', 'month', 'year'; optional):
    Initial date selection level.

- initialMonth (string; optional):
    Initial month for uncontrolled calendar.

- initiallyOpened (boolean; optional):
    Control initial dropdown opened state.

- inputFormat (string; optional):
    dayjs input format.

- inputWrapperOrder (list of a value equal to: 'label', 'description', 'error', 'input's; optional):
    Controls order of the Input.Wrapper elements.

- inset (string | number; optional):
    Mantine Style System Props.

- label (a list of or a singular dash component, string or number; optional):
    Input label, displayed before input.

- left (string | number; optional):
    Mantine Style System Props.

- lh (string | number; optional):
    Mantine Style System Props.

- locale (string; optional):
    Locale used for labels formatting, defaults to theme.datesLocale.

- lts (string | number; optional):
    Mantine Style System Props.

- m (number; optional):
    Mantine Style System Props.

- mah (number; optional):
    Mantine Style System Props.

- maw (number; optional):
    Mantine Style System Props.

- maxDate (string; optional):
    Maximum possible date.

- mb (number; optional):
    Mantine Style System Props.

- mih (number; optional):
    Mantine Style System Props.

- minDate (string; optional):
    Minimum possible date.

- miw (number; optional):
    Mantine Style System Props.

- ml (number; optional):
    Mantine Style System Props.

- modalZIndex (number; optional):
    Modal z-index.

- mr (number; optional):
    Mantine Style System Props.

- mt (number; optional):
    Mantine Style System Props.

- mx (number; optional):
    Mantine Style System Props.

- my (number; optional):
    Mantine Style System Props.

- name (string; optional):
    Name prop.

- nextDecadeLabel (string; optional):
    Next decade control aria-label.

- nextMonthLabel (string; optional):
    Next month control aria-label.

- nextYearLabel (string; optional):
    Next year control aria-label.

- opacity (number; optional):
    Mantine Style System Props.

- openDropdownOnClear (boolean; optional):
    Set to True to open dropdown on clear.

- p (number; optional):
    Mantine Style System Props.

- paginateBy (number; optional):
    Paginate by amount of months.

- pb (number; optional):
    Mantine Style System Props.

- persisted_props (list of strings; default ["value"]):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pl (number; optional):
    Mantine Style System Props.

- placeholder (string; optional):
    Placeholder.

- pos (a value equal to: 'static', 'relative', 'fixed', 'absolute', 'sticky'; optional):
    Mantine Style System Props.

- pr (number; optional):
    Mantine Style System Props.

- preventFocus (boolean; optional):
    Prevent focusing upon clicking.

- previousDecadeLabel (string; optional):
    Previous decade control aria-label.

- previousMonthLabel (string; optional):
    Previous month control aria-label.

- previousYearLabel (string; optional):
    Previous year control aria-label.

- pt (number; optional):
    Mantine Style System Props.

- px (number; optional):
    Mantine Style System Props.

- py (number; optional):
    Mantine Style System Props.

- radius (number; optional):
    Input border-radius from theme or number to set border-radius in
    px.

- required (boolean; optional):
    Sets required on input element   Adds required attribute to the
    input and red asterisk on the right side of label.

- right (string | number; optional):
    Mantine Style System Props.

- rightSection (a list of or a singular dash component, string or number; optional):
    Right section of input, similar to icon but on the right.

- rightSectionWidth (number; optional):
    Width of right section, is used to calculate input padding-right.

- shadow (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Dropdown shadow from theme or css value for custom box-shadow.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Input size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- ta (a value equal to: 'initial', 'inherit', 'left', 'right', 'center', 'justify'; optional):
    Mantine Style System Props.

- td (string; optional):
    Mantine Style System Props.

- top (string | number; optional):
    Mantine Style System Props.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    Dropdown appear/disappear transition.

- transitionDuration (number; optional):
    Dropdown appear/disappear transition duration.

- transitionTimingFunction (string; optional):
    Dropdown appear/disappear transition timing function, defaults to
    theme.transitionTimingFunction.

- tt (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase'; optional):
    Mantine Style System Props.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string; optional):
    Selected date, required with controlled input.

- variant (a value equal to: 'unstyled', 'default', 'filled'; optional):
    Defines input appearance, defaults to default in light color
    scheme and filled in dark.

- w (number; optional):
    Mantine Style System Props.

- weekendDays (list of numbers; optional):
    Indices of weekend days.

- withAsterisk (boolean; optional):
    Determines whether required asterisk should be rendered, overrides
    required prop, does not add required attribute to the input.

- zIndex (number; optional):
    Dropdown zIndex."""
    _children_props = ['icon', 'rightSection', 'label', 'description', 'error']
    _base_nodes = ['icon', 'rightSection', 'label', 'description', 'error', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'DatePicker'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, allowFreeInput=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, shadow=Component.UNDEFINED, size=Component.UNDEFINED, dropdownType=Component.UNDEFINED, dropdownPosition=Component.UNDEFINED, clearable=Component.UNDEFINED, zIndex=Component.UNDEFINED, fixOnBlur=Component.UNDEFINED, clickOutsideEvents=Component.UNDEFINED, modalZIndex=Component.UNDEFINED, clearButtonTabIndex=Component.UNDEFINED, amountOfMonths=Component.UNDEFINED, paginateBy=Component.UNDEFINED, allowLevelChange=Component.UNDEFINED, initialLevel=Component.UNDEFINED, disabledDates=Component.UNDEFINED, disableOutsideEvents=Component.UNDEFINED, fullWidth=Component.UNDEFINED, preventFocus=Component.UNDEFINED, focusable=Component.UNDEFINED, maxDate=Component.UNDEFINED, minDate=Component.UNDEFINED, hideWeekdays=Component.UNDEFINED, hideOutsideDates=Component.UNDEFINED, weekendDays=Component.UNDEFINED, firstDayOfWeek=Component.UNDEFINED, closeCalendarOnChange=Component.UNDEFINED, openDropdownOnClear=Component.UNDEFINED, inputFormat=Component.UNDEFINED, initiallyOpened=Component.UNDEFINED, initialMonth=Component.UNDEFINED, locale=Component.UNDEFINED, clearButtonLabel=Component.UNDEFINED, nextMonthLabel=Component.UNDEFINED, previousMonthLabel=Component.UNDEFINED, nextYearLabel=Component.UNDEFINED, previousYearLabel=Component.UNDEFINED, nextDecadeLabel=Component.UNDEFINED, previousDecadeLabel=Component.UNDEFINED, icon=Component.UNDEFINED, iconWidth=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, required=Component.UNDEFINED, radius=Component.UNDEFINED, variant=Component.UNDEFINED, disabled=Component.UNDEFINED, placeholder=Component.UNDEFINED, name=Component.UNDEFINED, debounce=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, error=Component.UNDEFINED, withAsterisk=Component.UNDEFINED, inputWrapperOrder=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowFreeInput', 'allowLevelChange', 'amountOfMonths', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonLabel', 'clearButtonTabIndex', 'clearable', 'clickOutsideEvents', 'closeCalendarOnChange', 'debounce', 'description', 'disableOutsideEvents', 'disabled', 'disabledDates', 'display', 'dropdownPosition', 'dropdownType', 'error', 'ff', 'firstDayOfWeek', 'fixOnBlur', 'focusable', 'fs', 'fullWidth', 'fw', 'fz', 'h', 'hideOutsideDates', 'hideWeekdays', 'icon', 'iconWidth', 'initialLevel', 'initialMonth', 'initiallyOpened', 'inputFormat', 'inputWrapperOrder', 'inset', 'label', 'left', 'lh', 'locale', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'mih', 'minDate', 'miw', 'ml', 'modalZIndex', 'mr', 'mt', 'mx', 'my', 'name', 'nextDecadeLabel', 'nextMonthLabel', 'nextYearLabel', 'opacity', 'openDropdownOnClear', 'p', 'paginateBy', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'preventFocus', 'previousDecadeLabel', 'previousMonthLabel', 'previousYearLabel', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'shadow', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'value', 'variant', 'w', 'weekendDays', 'withAsterisk', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allowFreeInput', 'allowLevelChange', 'amountOfMonths', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonLabel', 'clearButtonTabIndex', 'clearable', 'clickOutsideEvents', 'closeCalendarOnChange', 'debounce', 'description', 'disableOutsideEvents', 'disabled', 'disabledDates', 'display', 'dropdownPosition', 'dropdownType', 'error', 'ff', 'firstDayOfWeek', 'fixOnBlur', 'focusable', 'fs', 'fullWidth', 'fw', 'fz', 'h', 'hideOutsideDates', 'hideWeekdays', 'icon', 'iconWidth', 'initialLevel', 'initialMonth', 'initiallyOpened', 'inputFormat', 'inputWrapperOrder', 'inset', 'label', 'left', 'lh', 'locale', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'mih', 'minDate', 'miw', 'ml', 'modalZIndex', 'mr', 'mt', 'mx', 'my', 'name', 'nextDecadeLabel', 'nextMonthLabel', 'nextYearLabel', 'opacity', 'openDropdownOnClear', 'p', 'paginateBy', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'preventFocus', 'previousDecadeLabel', 'previousMonthLabel', 'previousYearLabel', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'shadow', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'value', 'variant', 'w', 'weekendDays', 'withAsterisk', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DatePicker, self).__init__(**args)
