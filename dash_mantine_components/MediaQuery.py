# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MediaQuery(Component):
    """A MediaQuery component.
Apply styles to children if media query matches. For more information, see: https://mantine.dev/core/media-query/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Child that should be shown at given breakpoint, it must accept
    className prop.

- innerBoxStyle (boolean | number | string | dict | list; optional):
    props for inner box.

- largerThan (number; optional):
    Styles applied to child when viewport is larger than given
    breakpoint.

- query (string; optional):
    Any other media query.

- smallerThan (number; optional):
    Styles applied to child when viewport is smaller than given
    breakpoint.

- styles (dict; required):
    Styles applied to child when breakpoint matches.

    `styles` is a dict with keys:
"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'MediaQuery'
    @_explicitize_args
    def __init__(self, children=None, smallerThan=Component.UNDEFINED, largerThan=Component.UNDEFINED, query=Component.UNDEFINED, styles=Component.REQUIRED, innerBoxStyle=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'innerBoxStyle', 'largerThan', 'query', 'smallerThan', 'styles']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'innerBoxStyle', 'largerThan', 'query', 'smallerThan', 'styles']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['styles']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(MediaQuery, self).__init__(children=children, **args)
