
module DashMantineComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/affix.jl")
include("jl/alert.jl")
include("jl/button.jl")
include("jl/center.jl")
include("jl/checkbox.jl")
include("jl/chips.jl")
include("jl/col.jl")
include("jl/container.jl")
include("jl/datepicker.jl")
include("jl/daterangepicker.jl")
include("jl/divider.jl")
include("jl/drawer.jl")
include("jl/grid.jl")
include("jl/group.jl")
include("jl/mediaquery.jl")
include("jl/modal.jl")
include("jl/multiselect.jl")
include("jl/notification.jl")
include("jl/prism.jl")
include("jl/radiogroup.jl")
include("jl/rangeslider.jl")
include("jl/segmentedcontrol.jl")
include("jl/select.jl")
include("jl/simplegrid.jl")
include("jl/slider.jl")
include("jl/space.jl")
include("jl/switch.jl")
include("jl/tab.jl")
include("jl/table.jl")
include("jl/tabs.jl")
include("jl/text.jl")
include("jl/textinput.jl")
include("jl/title.jl")
include("jl/tooltip.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_mantine_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_mantine_components.min.js",
    external_url = "https://unpkg.com/dash_mantine_components@0.0.1/dash_mantine_components/dash_mantine_components.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_mantine_components.min.js.map",
    external_url = "https://unpkg.com/dash_mantine_components@0.0.1/dash_mantine_components/dash_mantine_components.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
