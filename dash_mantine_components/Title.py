# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Title(Component):
    """A Title component.
Render icon inside element with theme colors. For more information, see: https://mantine.dev/core/theme-icon/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- align (a value equal to: 'initial', 'inherit', 'left', 'right', 'center', 'justify', 'end', 'start', '-moz-initial', 'revert', 'unset', 'match-parent'; optional):
    Sets text-align css property.

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
    Key of theme.colors or any valid CSS color.

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

- gradient (dict; optional):
    Controls gradient settings in gradient variant only.

    `gradient` is a dict with keys:

    - deg (number; optional)

    - from (string; required)

    - to (string; required)

- h (number; optional):
    Mantine Style System Props.

- inherit (boolean; optional):
    Inherit font properties from parent element.

- inline (boolean; optional):
    Sets line-height to 1 for centering.

- inset (string | number; optional):
    Mantine Style System Props.

- italic (boolean; optional):
    Adds font-style: italic style.

- left (string | number; optional):
    Mantine Style System Props.

- lh (string | number; optional):
    Mantine Style System Props.

- lineClamp (number; optional):
    CSS -webkit-line-clamp property.

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

- order (a value equal to: 1, 2, 3, 4, 5, 6; optional):
    Defines component and styles which will be used.

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

- right (string | number; optional):
    Mantine Style System Props.

- size (string | number; optional):
    Title font-size: h1-h6 or any valid CSS font-size value.

- span (boolean; optional):
    Shorthand for component=\"span\".

- strikethrough (boolean; optional):
    Add strikethrough styles.

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

- transform (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase', '-moz-initial', 'revert', 'unset', 'full-size-kana', 'full-width'; optional):
    Sets text-transform css property.

- truncate (boolean | number | string | dict | list; optional):
    CSS truncate overflowing text with an ellipsis.

- tt (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase'; optional):
    Mantine Style System Props.

- underline (boolean; optional):
    Underline the text.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (a value equal to: 'gradient', 'text', 'link'; optional):
    Link or text variant.

- w (number; optional):
    Mantine Style System Props.

- weight (number; optional):
    Sets font-weight css property."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Title'
    @_explicitize_args
    def __init__(self, children=None, order=Component.UNDEFINED, size=Component.UNDEFINED, variant=Component.UNDEFINED, gradient=Component.UNDEFINED, color=Component.UNDEFINED, inherit=Component.UNDEFINED, italic=Component.UNDEFINED, inline=Component.UNDEFINED, weight=Component.UNDEFINED, truncate=Component.UNDEFINED, transform=Component.UNDEFINED, align=Component.UNDEFINED, lineClamp=Component.UNDEFINED, underline=Component.UNDEFINED, strikethrough=Component.UNDEFINED, span=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'gradient', 'h', 'inherit', 'inline', 'inset', 'italic', 'left', 'lh', 'lineClamp', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'order', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'span', 'strikethrough', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transform', 'truncate', 'tt', 'underline', 'unstyled', 'variant', 'w', 'weight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'gradient', 'h', 'inherit', 'inline', 'inset', 'italic', 'left', 'lh', 'lineClamp', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'order', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'span', 'strikethrough', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transform', 'truncate', 'tt', 'underline', 'unstyled', 'variant', 'w', 'weight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Title, self).__init__(children=children, **args)
