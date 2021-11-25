import Switch from 'react-switch';
import { useCallback } from 'react';

const PowerSwitch = ({isEnable, turnOn, turnOff}) => {
    const handleChange = useCallback((checked) => {
        if (checked) {
            turnOn();
        } else {
            turnOff();
        }
    }, [turnOn, turnOff]);

    return <Switch
        checked={isEnable}
        onChange={handleChange}
        checkedIcon={false}
        uncheckedIcon={false}
    />;
};

export default PowerSwitch;
