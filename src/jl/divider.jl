# AUTO GENERATED FILE - DO NOT EDIT

export divider

"""
    divider(;kwargs...)

A Divider component.
Horizontal line with optional label or vertical divider. For more information, see: https://mantine.dev/core/divider/
Keyword arguments:
- `id` (String; optional): The ID of this component, used to identify dash components in callbacks
- `className` (String; optional): Often used with CSS to style elements with common properties
- `color` (optional): Line color from theme, defaults to gray in light color scheme and to dark in dark color scheme
- `label` (String; optional): Adds text after line in horizontal orientation
- `labelPosition` (a value equal to: "right", "left", "center"; optional): Label position
- `orientation` (optional): Line orientation
- `size` (optional): Sets height in horizontal orientation and width in vertical
- `variant` (a value equal to: "dashed", "dotted", "solid"; optional): Divider borderStyle
"""
function divider(; kwargs...)
        available_props = Symbol[:id, :className, :color, :label, :labelPosition, :orientation, :size, :variant]
        wild_props = Symbol[]
        return Component("divider", "Divider", "dash_mantine_components", available_props, wild_props; kwargs...)
end

