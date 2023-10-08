# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Button(Component):
    """A Button component.
Render button or link with button styles from mantine theme. For more information, see: https://mantine.dev/core/button/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Button label.

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
    Button color from theme.

- compact (boolean; optional):
    Reduces vertical and horizontal spacing.

- disabled (boolean; optional):
    Disabled state.

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- ff (string; optional):
    Mantine Style System Props.

- fs (a value equal to: 'initial', 'inherit', 'normal', 'italic', 'oblique'; optional):
    Mantine Style System Props.

- fullWidth (boolean; optional):
    Sets button width to 100% of parent element.

- fw (number; optional):
    Mantine Style System Props.

- fz (number; optional):
    Mantine Style System Props.

- gradient (dict; optional):
    Controls gradient settings in gradient variant only.

    `gradient` is a dict with keys:

    - deg (number; optional)

    - from (string; required)

    - to (string; required)

- h (number; optional):
    Mantine Style System Props.

- inset (string | number; optional):
    Mantine Style System Props.

- left (string | number; optional):
    Mantine Style System Props.

- leftIcon (a list of or a singular dash component, string or number; optional):
    Adds icon before button label.

- lh (string | number; optional):
    Mantine Style System Props.

- loaderPosition (a value equal to: 'left', 'right', 'center'; optional):
    Loader position relative to button label.

- loaderProps (dict; optional):
    Props spread to Loader component.

    `loaderProps` is a dict with keys:

    - color (boolean | number | string | dict | list; optional):
        Loader color from theme.

    - size (number; optional):
        Defines width of loader.

    - variant (a value equal to: 'bars', 'oval', 'dots'; optional):
        Loader appearance.

- loading (boolean; optional):
    Indicate loading state.

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

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- opacity (number; optional):
    Mantine Style System Props.

- p (number; optional):
    Mantine Style System Props.

- pb (number; optional):
    Mantine Style System Props.

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

- radius (number; optional):
    Button border-radius from theme or number to set border-radius in
    px.

- right (string | number; optional):
    Mantine Style System Props.

- rightIcon (a list of or a singular dash component, string or number; optional):
    Adds icon after button label.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Predefined button size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- ta (a value equal to: 'left', 'right', 'center', 'initial', 'inherit', 'justify'; optional):
    Mantine Style System Props.

- td (string; optional):
    Mantine Style System Props.

- top (string | number; optional):
    Mantine Style System Props.

- tt (a value equal to: 'uppercase', 'initial', 'inherit', 'none', 'capitalize', 'lowercase'; optional):
    Mantine Style System Props.

- type (a value equal to: 'submit', 'button', 'reset'; optional):
    Button type attribute.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- uppercase (boolean; optional):
    Set text-transform to uppercase.

- variant (a value equal to: 'filled', 'outline', 'light', 'white', 'default', 'subtle', 'gradient'; optional):
    Controls button appearance.

- w (number; optional):
    Mantine Style System Props."""
    _children_props = ['leftIcon', 'rightIcon']
    _base_nodes = ['leftIcon', 'rightIcon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Button'
    @_explicitize_args
    def __init__(self, children=None, size=Component.UNDEFINED, type=Component.UNDEFINED, color=Component.UNDEFINED, leftIcon=Component.UNDEFINED, rightIcon=Component.UNDEFINED, fullWidth=Component.UNDEFINED, radius=Component.UNDEFINED, variant=Component.UNDEFINED, gradient=Component.UNDEFINED, uppercase=Component.UNDEFINED, compact=Component.UNDEFINED, loading=Component.UNDEFINED, loaderProps=Component.UNDEFINED, loaderPosition=Component.UNDEFINED, disabled=Component.UNDEFINED, n_clicks=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'compact', 'disabled', 'display', 'ff', 'fs', 'fullWidth', 'fw', 'fz', 'gradient', 'h', 'inset', 'left', 'leftIcon', 'lh', 'loaderPosition', 'loaderProps', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'n_clicks', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'rightIcon', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'type', 'unstyled', 'uppercase', 'variant', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'compact', 'disabled', 'display', 'ff', 'fs', 'fullWidth', 'fw', 'fz', 'gradient', 'h', 'inset', 'left', 'leftIcon', 'lh', 'loaderPosition', 'loaderProps', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'n_clicks', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'rightIcon', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'type', 'unstyled', 'uppercase', 'variant', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Button, self).__init__(children=children, **args)
