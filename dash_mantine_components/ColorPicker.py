# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ColorPicker(Component):
    """A ColorPicker component.
Inline color picker. For more information, see: https://mantine.dev/core/color-picker/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- alphaLabel (string; optional):
    Alpha slider aria-label.

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

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- ff (string; optional):
    Mantine Style System Props.

- focusable (boolean; optional):
    Should interactive elements be focusable.

- format (a value equal to: 'hex', 'hexa', 'rgba', 'rgb', 'hsl', 'hsla'; optional):
    Color format.

- fs (a value equal to: 'initial', 'inherit', 'normal', 'italic', 'oblique'; optional):
    Mantine Style System Props.

- fullWidth (boolean; optional):
    Force picker to take 100% width of its container.

- fw (number; optional):
    Mantine Style System Props.

- fz (number; optional):
    Mantine Style System Props.

- h (number; optional):
    Mantine Style System Props.

- hueLabel (string; optional):
    Hue slider aria-label.

- inset (string | number; optional):
    Mantine Style System Props.

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

- pt (number; optional):
    Mantine Style System Props.

- px (number; optional):
    Mantine Style System Props.

- py (number; optional):
    Mantine Style System Props.

- right (string | number; optional):
    Mantine Style System Props.

- saturationLabel (string; optional):
    Saturation slider aria-label.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Predefined component size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- swatches (list of strings; optional):
    Predefined colors.

- swatchesPerRow (number; optional):
    Number of swatches displayed in one row.

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

- tt (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase'; optional):
    Mantine Style System Props.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string; optional):
    Controlled component value.

- w (number; optional):
    Mantine Style System Props.

- withPicker (boolean; optional):
    Set to False to display swatches only."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'ColorPicker'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, format=Component.UNDEFINED, withPicker=Component.UNDEFINED, swatches=Component.UNDEFINED, swatchesPerRow=Component.UNDEFINED, size=Component.UNDEFINED, fullWidth=Component.UNDEFINED, focusable=Component.UNDEFINED, saturationLabel=Component.UNDEFINED, hueLabel=Component.UNDEFINED, alphaLabel=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alphaLabel', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'focusable', 'format', 'fs', 'fullWidth', 'fw', 'fz', 'h', 'hueLabel', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'saturationLabel', 'size', 'style', 'styles', 'swatches', 'swatchesPerRow', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'value', 'w', 'withPicker']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alphaLabel', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'focusable', 'format', 'fs', 'fullWidth', 'fw', 'fz', 'h', 'hueLabel', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'saturationLabel', 'size', 'style', 'styles', 'swatches', 'swatchesPerRow', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'value', 'w', 'withPicker']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ColorPicker, self).__init__(**args)
