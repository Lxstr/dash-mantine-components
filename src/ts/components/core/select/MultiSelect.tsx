import React, { useState } from "react";
import {
    DefaultProps,
    PersistenceProps,
    SelectSharedProps,
} from "../../../props";
import { MultiSelect as MantineMultiSelect } from "@mantine/core";
import { useDidUpdate } from "@mantine/hooks";

type Props = {
    /** Clear search value when item is selected */
    clearSearchOnChange?: boolean;
    /** Clear search field value on blur */
    clearSearchOnBlur?: boolean;
    /** Limit amount of items selected */
    maxSelectedValues?: number;
    /** Controlled input value */
    value?: string[];
} & SelectSharedProps &
    PersistenceProps &
    DefaultProps;

/**
 * Custom searchable MultiSelect. For more information, see: https://mantine.dev/core/multi-select/
 */
const MultiSelect = (props: Props) => {
    const {
        setProps,
        data,
        value,
        initiallyOpened,
        persistence,
        persisted_props,
        persistence_type,
        searchValue,
        ...other
    } = props;

    const [options, setOptions] = useState(data);
    const [selections, setSelections] = useState(value);
    const [searchVal, onSearchValChange] = useState(searchValue);
    const [dropdownOpened, setDropdownOpened] = useState(initiallyOpened);

    useDidUpdate(() => {
        setOptions(data);
    }, [data]);

    const onClose = () => {
        console.log("change");
        console.log(selections);
        setProps({ value: selections });
        setDropdownOpened(false);
    };

    const onOpen = () => {
        setDropdownOpened(true);
    };

    const onChange = (value: string[]) => {
        if (!dropdownOpened) {
            setProps({ value });
        }
        setSelections(value);
    };

    const onSearchChange = (value: string) => {
        setProps({ searchValue: value });
        onSearchValChange(value);
    };

    return (
        <MantineMultiSelect
            onChange={onChange}
            onDropdownClose={onClose}
            onDropdownOpen={onOpen}
            getCreateLabel={(query) => `includes:${query}`}
            onCreate={(query) => {
                const item = { value: `includes:${query}`, label: query };
                const newOptions = [...options, item];
                setProps({ data: newOptions });
                return item;
            }}
            data={options}
            wrapperProps={{ autoComplete: "off" }}
            searchValue={searchVal}
            onSearchChange={onSearchChange}
            {...other}
        />
    );
};

MultiSelect.defaultProps = {
    data: [],
    persisted_props: ["value"],
    persistence_type: "local",
};

export default MultiSelect;
