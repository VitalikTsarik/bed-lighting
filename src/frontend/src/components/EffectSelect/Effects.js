import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';
import { EffectsType } from './constants';
import { useCallback } from 'react';

const Effects = ({effect, disabled, onSelect}) => {
    const handleChange = useCallback((value) => onSelect(value), [onSelect]);

    return (
        <ToggleButtonGroup type="radio" name="effect" value={effect} onChange={handleChange}>
            {Object.entries(EffectsType).map(([key, value]) => (
                <ToggleButton
                    key={value}
                    id={value}
                    value={value}
                    disabled={disabled}
                    variant="outline-primary"
                >
                    {key}
                </ToggleButton>
            ))}
        </ToggleButtonGroup>
    );
};

export default Effects;
