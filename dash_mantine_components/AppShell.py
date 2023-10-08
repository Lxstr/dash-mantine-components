# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AppShell(Component):
    """An AppShell component.
Responsive shell for your application with header and navbar. For more information, see: https://mantine.dev/core/app-shell/

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    AppShell content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aside (a list of or a singular dash component, string or number; optional):
    <Aside /> component.

- asideOffsetBreakpoint (number; optional):
    Breakpoint at which Aside component should no longer be offset
    with padding-right, applicable only for fixed position.

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

- fixed (boolean; optional):
    True to switch from static layout to fixed.

- footer (a list of or a singular dash component, string or number; optional):
    <Footer /> component.

- fs (a value equal to: 'initial', 'inherit', 'normal', 'italic', 'oblique'; optional):
    Mantine Style System Props.

- fw (number; optional):
    Mantine Style System Props.

- fz (number; optional):
    Mantine Style System Props.

- h (number; optional):
    Mantine Style System Props.

- header (a list of or a singular dash component, string or number; optional):
    <Header /> component.

- hidden (boolean; optional):
    True to hide all AppShell parts and render only children.

- inset (string | number; optional):
    Mantine Style System Props.

- layout (a value equal to: 'default', 'alt'; optional):
    Determines how Navbar and Aside components are positioned relative
    to Header and Footer components.

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

- navbar (a list of or a singular dash component, string or number; optional):
    <Navbar /> component.

- navbarOffsetBreakpoint (number; optional):
    Breakpoint at which Navbar component should no longer be offset
    with padding-left, applicable only for fixed position.

- opacity (number; optional):
    Mantine Style System Props.

- p (number; optional):
    Mantine Style System Props.

- padding (number; optional):
    Content padding.

- pb (number; optional):
    Mantine Style System Props.

- pl (number; optional):
    Mantine Style System Props.

- pos (a value equal to: 'fixed', 'static', 'relative', 'absolute', 'sticky'; optional):
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

- zIndex (number; optional):
    zIndex prop passed to Navbar and Header components."""
    _children_props = ['navbar', 'aside', 'header', 'footer']
    _base_nodes = ['navbar', 'aside', 'header', 'footer', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'AppShell'
    @_explicitize_args
    def __init__(self, children=None, layout=Component.UNDEFINED, navbar=Component.UNDEFINED, aside=Component.UNDEFINED, header=Component.UNDEFINED, footer=Component.UNDEFINED, zIndex=Component.UNDEFINED, fixed=Component.UNDEFINED, hidden=Component.UNDEFINED, padding=Component.UNDEFINED, navbarOffsetBreakpoint=Component.UNDEFINED, asideOffsetBreakpoint=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aside', 'asideOffsetBreakpoint', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'fixed', 'footer', 'fs', 'fw', 'fz', 'h', 'header', 'hidden', 'inset', 'layout', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'navbar', 'navbarOffsetBreakpoint', 'opacity', 'p', 'padding', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'aside', 'asideOffsetBreakpoint', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'fixed', 'footer', 'fs', 'fw', 'fz', 'h', 'header', 'hidden', 'inset', 'layout', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'navbar', 'navbarOffsetBreakpoint', 'opacity', 'p', 'padding', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(AppShell, self).__init__(children=children, **args)
