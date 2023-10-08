# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Indicator(Component):
    """An Indicator component.
Display element at the corner of another element. For more information, see: https://mantine.dev/core/indicator/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Element that should have an indicator.

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
    Color from theme.colors or any other valid CSS color value.

- disabled (boolean; optional):
    When component is disabled it renders children without indicator.

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- dot (boolean; optional):
    Whether to show the dot.

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

- inline (boolean; optional):
    Determines whether indicator container should be an inline
    element.

- inset (string | number; optional):
    Mantine Style System Props.

- label (a list of or a singular dash component, string or number; optional):
    Indicator label.

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

- offset (number; optional):
    Changes position offset, usually used when element has
    border-radius.

- opacity (number; optional):
    Mantine Style System Props.

- overflowCount (number; optional):
    Indicator count overflowCount.

- p (number; optional):
    Mantine Style System Props.

- pb (number; optional):
    Mantine Style System Props.

- pl (number; optional):
    Mantine Style System Props.

- pos (a value equal to: 'static', 'relative', 'fixed', 'absolute', 'sticky'; optional):
    Mantine Style System Props.

- position (a value equal to: 'top-center', 'top-end', 'top-start', 'bottom-center', 'bottom-end', 'bottom-start', 'middle-center', 'middle-end', 'middle-start'; optional):
    Indicator position relative to child element.

- pr (number; optional):
    Mantine Style System Props.

- processing (boolean; optional):
    Indicator processing animation.

- pt (number; optional):
    Mantine Style System Props.

- px (number; optional):
    Mantine Style System Props.

- py (number; optional):
    Mantine Style System Props.

- radius (number; optional):
    border-radius from theme.radius or number value to set radius in
    px.

- right (string | number; optional):
    Mantine Style System Props.

- showZero (boolean; optional):
    When showZero is True and label is zero  renders children with
    indicator.

- size (number; optional):
    Size in px.

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

- tt (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase'; optional):
    Mantine Style System Props.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- w (number; optional):
    Mantine Style System Props.

- withBorder (boolean; optional):
    Determines whether indicator should have border.

- zIndex (number; optional):
    Indicator z-index."""
    _children_props = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Indicator'
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, offset=Component.UNDEFINED, inline=Component.UNDEFINED, size=Component.UNDEFINED, label=Component.UNDEFINED, overflowCount=Component.UNDEFINED, dot=Component.UNDEFINED, radius=Component.UNDEFINED, color=Component.UNDEFINED, withBorder=Component.UNDEFINED, disabled=Component.UNDEFINED, showZero=Component.UNDEFINED, processing=Component.UNDEFINED, zIndex=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'dot', 'ff', 'fs', 'fw', 'fz', 'h', 'inline', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'offset', 'opacity', 'overflowCount', 'p', 'pb', 'pl', 'pos', 'position', 'pr', 'processing', 'pt', 'px', 'py', 'radius', 'right', 'showZero', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'withBorder', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'dot', 'ff', 'fs', 'fw', 'fz', 'h', 'inline', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'offset', 'opacity', 'overflowCount', 'p', 'pb', 'pl', 'pos', 'position', 'pr', 'processing', 'pt', 'px', 'py', 'radius', 'right', 'showZero', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'withBorder', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Indicator, self).__init__(children=children, **args)
