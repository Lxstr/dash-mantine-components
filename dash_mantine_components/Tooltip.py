# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.
Renders tooltip at given element on mouse over or any other event. For more information, see: https://mantine.dev/core/tooltip/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Target element.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- arrowOffset (number; optional):
    Arrow offset in px.

- arrowSize (number; optional):
    Arrow size in px.

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

- closeDelay (number; optional):
    Close delay in ms.

- color (boolean | number | string | dict | list; optional):
    Key of theme.colors.

- disabled (boolean; optional):
    Disables tooltip.

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- events (dict; optional):
    Determines which events will be used to show tooltip.

    `events` is a dict with keys:

    - focus (boolean; required)

    - hover (boolean; required)

    - touch (boolean; required)

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

- label (a list of or a singular dash component, string or number; required):
    Tooltip label.

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

- maw (number; optional):
    Mantine Style System Props.

- mb (number; optional):
    Mantine Style System Props.

- mih (number; optional):
    Mantine Style System Props.

- miw (number; optional):
    Mantine Style System Props.

- ml (number; optional):
    Mantine Style System Props.

- mr (number; optional):
    Mantine Style System Props.

- mt (number; optional):
    Mantine Style System Props.

- multiline (boolean; optional):
    Defines whether content should be wrapped on to the next line.

- mx (number; optional):
    Mantine Style System Props.

- my (number; optional):
    Mantine Style System Props.

- offset (number; optional):
    Space between target element and tooltip in px.

- opacity (number; optional):
    Mantine Style System Props.

- openDelay (number; optional):
    Open delay in ms.

- opened (boolean; optional):
    Controls opened state.

- p (number; optional):
    Mantine Style System Props.

- pb (number; optional):
    Mantine Style System Props.

- pl (number; optional):
    Mantine Style System Props.

- pos (a value equal to: 'static', 'relative', 'fixed', 'absolute', 'sticky'; optional):
    Mantine Style System Props.

- position (a value equal to: 'top', 'right', 'bottom', 'left', 'top-end', 'top-start', 'right-end', 'right-start', 'bottom-end', 'bottom-start', 'left-end', 'left-start'; optional):
    Tooltip position relative to target element (default) or mouse
    (floating).

- pr (number; optional):
    Mantine Style System Props.

- pt (number; optional):
    Mantine Style System Props.

- px (number; optional):
    Mantine Style System Props.

- py (number; optional):
    Mantine Style System Props.

- radius (number; optional):
    Radius from theme.radius or number to set border-radius in px.

- right (string | number; optional):
    Mantine Style System Props.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- ta (a value equal to: 'right', 'left', 'initial', 'inherit', 'center', 'justify'; optional):
    Mantine Style System Props.

- td (string; optional):
    Mantine Style System Props.

- top (string | number; optional):
    Mantine Style System Props.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    One of premade transitions ot transition object.

- transitionDuration (number; optional):
    Transition duration in ms.

- tt (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase'; optional):
    Mantine Style System Props.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- w (number; optional):
    Mantine Style System Props.

- width (number; optional):
    Tooltip width in px.

- withArrow (boolean; optional):
    Determines whether component should have an arrow.

- zIndex (number; optional):
    Tooltip z-index."""
    _children_props = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Tooltip'
    @_explicitize_args
    def __init__(self, children=None, openDelay=Component.UNDEFINED, closeDelay=Component.UNDEFINED, opened=Component.UNDEFINED, offset=Component.UNDEFINED, withArrow=Component.UNDEFINED, arrowSize=Component.UNDEFINED, arrowOffset=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, events=Component.UNDEFINED, position=Component.UNDEFINED, label=Component.REQUIRED, radius=Component.UNDEFINED, color=Component.UNDEFINED, multiline=Component.UNDEFINED, width=Component.UNDEFINED, zIndex=Component.UNDEFINED, disabled=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'arrowOffset', 'arrowSize', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'closeDelay', 'color', 'disabled', 'display', 'events', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'multiline', 'mx', 'my', 'offset', 'opacity', 'openDelay', 'opened', 'p', 'pb', 'pl', 'pos', 'position', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'tt', 'unstyled', 'w', 'width', 'withArrow', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'arrowOffset', 'arrowSize', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'closeDelay', 'color', 'disabled', 'display', 'events', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'multiline', 'mx', 'my', 'offset', 'opacity', 'openDelay', 'opened', 'p', 'pb', 'pl', 'pos', 'position', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'tt', 'unstyled', 'w', 'width', 'withArrow', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Tooltip, self).__init__(children=children, **args)
