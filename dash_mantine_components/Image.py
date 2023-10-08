# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Image(Component):
    """An Image component.
Image with optional placeholder for loading and error state. For more information, see: https://mantine.dev/core/image/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- alt (string; optional):
    Image alt text, used as title for placeholder if image was not
    loaded.

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

- caption (a list of or a singular dash component, string or number; optional):
    Image figcaption, displayed bellow image.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- display (a value equal to: 'initial', 'inherit', 'none', 'inline', 'block', 'contents', 'flex', 'grid', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'run-in', 'table', 'table-caption', 'table-column-group', 'table-header-group', 'table-footer-group', 'table-row-group', 'table-cell', 'table-column', 'table-row'; optional):
    Mantine Style System Props.

- ff (string; optional):
    Mantine Style System Props.

- fit (a value equal to: 'cover', 'contain'; optional):
    Image object-fit property.

- fs (a value equal to: 'initial', 'inherit', 'normal', 'italic', 'oblique'; optional):
    Mantine Style System Props.

- fw (number; optional):
    Mantine Style System Props.

- fz (number; optional):
    Mantine Style System Props.

- h (number; optional):
    Mantine Style System Props.

- height (string | number; optional):
    Image height, defaults to original image height adjusted to given
    width.

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

- pl (number; optional):
    Mantine Style System Props.

- placeholder (a list of or a singular dash component, string or number; optional):
    Customize placeholder content.

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
    Predefined border-radius value from theme.radius or number for
    border-radius in px.

- right (string | number; optional):
    Mantine Style System Props.

- src (string; optional):
    Image src.

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

- width (string | number; optional):
    Image width, defaults to 100%, cannot exceed 100%.

- withPlaceholder (boolean; optional):
    Enable placeholder when image is loading and when image fails to
    load."""
    _children_props = ['placeholder', 'caption']
    _base_nodes = ['placeholder', 'caption', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Image'
    @_explicitize_args
    def __init__(self, src=Component.UNDEFINED, alt=Component.UNDEFINED, fit=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, radius=Component.UNDEFINED, withPlaceholder=Component.UNDEFINED, placeholder=Component.UNDEFINED, caption=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'caption', 'className', 'classNames', 'display', 'ff', 'fit', 'fs', 'fw', 'fz', 'h', 'height', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'src', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'width', 'withPlaceholder']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'caption', 'className', 'classNames', 'display', 'ff', 'fit', 'fs', 'fw', 'fz', 'h', 'height', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'src', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'width', 'withPlaceholder']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Image, self).__init__(**args)
