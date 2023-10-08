# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RangeSlider(Component):
    """A RangeSlider component.
Capture user feedback from a range of values. For more information, see: https://mantine.dev/core/slider/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

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

- color (boolean | number | string | dict | list; optional):
    Color from theme.colors.

- disabled (boolean; optional):
    Disables slider.

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- ff (string; optional):
    Mantine Style System Props.

- fs (a value equal to: 'initial', 'inherit', 'normal', 'italic', 'oblique'; optional):
    Mantine Style System Props.

- fw (number; optional):
    Mantine Style System Props.

- fz (number; optional):
    Mantine Style System Props.

- h (number; optional):
    Mantine Style System Props.

- inset (string | number; optional):
    Mantine Style System Props.

- labelAlwaysOn (boolean; optional):
    If True label will be not be hidden when user stops dragging.

- labelTransition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    Label appear/disappear transition.

- labelTransitionDuration (number; optional):
    Label appear/disappear transition duration in ms.

- labelTransitionTimingFunction (string; optional):
    Label appear/disappear transition timing function, defaults to
    theme.transitionRimingFunction.

- left (string | number; optional):
    Mantine Style System Props.

- lh (string | number; optional):
    Mantine Style System Props.

- lts (string | number; optional):
    Mantine Style System Props.

- m (number; optional):
    Mantine Style System Props.

- mah (number; optional):
    Mantine Style System Props.

- marks (list of dicts; optional):
    Marks which will be placed on the track.

    `marks` is a list of dicts with keys:

    - label (a list of or a singular dash component, string or number; optional)

    - value (number; required)

- maw (number; optional):
    Mantine Style System Props.

- max (number; optional):
    Maximum possible value.

- maxRange (number; optional):
    Maximum range interval.

- mb (number; optional):
    Mantine Style System Props.

- mih (number; optional):
    Mantine Style System Props.

- min (number; optional):
    Minimal possible value.

- minRange (number; optional):
    Minimal range interval.

- miw (number; optional):
    Mantine Style System Props.

- ml (number; optional):
    Mantine Style System Props.

- mr (number; optional):
    Mantine Style System Props.

- mt (number; optional):
    Mantine Style System Props.

- mx (number; optional):
    Mantine Style System Props.

- my (number; optional):
    Mantine Style System Props.

- opacity (number; optional):
    Mantine Style System Props.

- p (number; optional):
    Mantine Style System Props.

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

- pos (a value equal to: 'static', 'relative', 'fixed', 'absolute', 'sticky'; optional):
    Mantine Style System Props.

- pr (number; optional):
    Mantine Style System Props.

- precision (number; optional):
    Amount of digits after the decimal point.

- pt (number; optional):
    Mantine Style System Props.

- px (number; optional):
    Mantine Style System Props.

- py (number; optional):
    Mantine Style System Props.

- radius (number; optional):
    Track border-radius from theme or number to set border-radius in
    px.

- right (string | number; optional):
    Mantine Style System Props.

- showLabelOnHover (boolean; optional):
    If True slider label will appear on hover.

- size (number; optional):
    Predefined track and thumb size, number to set sizes in px.

- step (number; optional):
    Number by which value will be incremented/decremented with thumb
    drag and arrows.

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

- thumbChildren (a list of or a singular dash component, string or number; optional):
    Thumb children, can be used to add icon.

- thumbFromLabel (string; optional):
    First thumb aria-label.

- thumbSize (number; optional):
    Thumb width and height in px.

- thumbToLabel (string; optional):
    Second thumb aria-label.

- top (string | number; optional):
    Mantine Style System Props.

- tt (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase'; optional):
    Mantine Style System Props.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- updatemode (a value equal to: 'mouseup', 'drag'; default 'mouseup'):
    Determines when the component should update its value property. If
    mouseup (the default) then the slider will only trigger its value
    when the user has finished dragging the slider. If drag, then the
    slider will update its value continuously as it is being dragged.

- value (boolean | number | string | dict | list; optional):
    Current value for controlled slider.

- w (number; optional):
    Mantine Style System Props."""
    _children_props = ['marks[].label', 'thumbChildren']
    _base_nodes = ['thumbChildren', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'RangeSlider'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, minRange=Component.UNDEFINED, maxRange=Component.UNDEFINED, thumbFromLabel=Component.UNDEFINED, thumbToLabel=Component.UNDEFINED, color=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, step=Component.UNDEFINED, precision=Component.UNDEFINED, marks=Component.UNDEFINED, labelTransition=Component.UNDEFINED, labelTransitionDuration=Component.UNDEFINED, labelTransitionTimingFunction=Component.UNDEFINED, labelAlwaysOn=Component.UNDEFINED, showLabelOnHover=Component.UNDEFINED, thumbChildren=Component.UNDEFINED, disabled=Component.UNDEFINED, thumbSize=Component.UNDEFINED, updatemode=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'labelAlwaysOn', 'labelTransition', 'labelTransitionDuration', 'labelTransitionTimingFunction', 'left', 'lh', 'lts', 'm', 'mah', 'marks', 'maw', 'max', 'maxRange', 'mb', 'mih', 'min', 'minRange', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'precision', 'pt', 'px', 'py', 'radius', 'right', 'showLabelOnHover', 'size', 'step', 'style', 'styles', 'sx', 'ta', 'td', 'thumbChildren', 'thumbFromLabel', 'thumbSize', 'thumbToLabel', 'top', 'tt', 'unstyled', 'updatemode', 'value', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'labelAlwaysOn', 'labelTransition', 'labelTransitionDuration', 'labelTransitionTimingFunction', 'left', 'lh', 'lts', 'm', 'mah', 'marks', 'maw', 'max', 'maxRange', 'mb', 'mih', 'min', 'minRange', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'precision', 'pt', 'px', 'py', 'radius', 'right', 'showLabelOnHover', 'size', 'step', 'style', 'styles', 'sx', 'ta', 'td', 'thumbChildren', 'thumbFromLabel', 'thumbSize', 'thumbToLabel', 'top', 'tt', 'unstyled', 'updatemode', 'value', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(RangeSlider, self).__init__(**args)
