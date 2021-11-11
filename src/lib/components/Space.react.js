import React from "react";
import PropTypes from "prop-types";
import { Space as MantineSpace } from "@mantine/core";
import { omit } from "ramda";
import { NumberSizes } from "../propTypes";

/** Add horizontal or vertical spacing from theme. For more information, see: https://mantine.dev/core/space/ */
const Space = (props) => {
    return (
        <MantineSpace {...omit(["setProps", "children"], props)}>
            {props.children}
        </MantineSpace>
    );
};

Space.displayName = "Space";

Space.defaultProps = {};

Space.propTypes = {
    /** The ID of this component, used to identify dash components in callbacks */
    id: PropTypes.string,

    /** Tab content */
    children: PropTypes.node,

    /** Often used with CSS to style elements with common properties */
    className: PropTypes.string,

    /**	Height, set to add vertical spacing */
    h: NumberSizes,

    /**	Width, set to add horizontal spacing */
    w: NumberSizes,
};

export default Space;
