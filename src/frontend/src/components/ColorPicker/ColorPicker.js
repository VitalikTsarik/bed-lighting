import TwitterPicker from 'react-color/es/Twitter';
import { useCallback, useRef, useState } from 'react';
import { useOnClickOutside } from './useClickOutside';
import './ColorPicker.css';

const ColorPicker = ({color, disabled, onChangeColor}) => {
    const [isOpen, setIsOpen] = useState(false);

    const handleClick = useCallback(() => {
        if (!disabled) {
            setIsOpen(true);
        }
    }, [disabled]);

    const handleChangeComplete = useCallback((color) => {
        setIsOpen(false);
        onChangeColor(color.rgb);
    }, [onChangeColor]);

    const ref = useRef(null);
    const handleClickOutside = useCallback(() => setIsOpen(false), []);
    useOnClickOutside(ref, handleClickOutside);

    return (
        <div className={`ColorPicker ${disabled ? 'disabled' : ''}`}>
            <div onClick={handleClick}>
                <div style={{backgroundColor: `rgb(${color.r},${color.g},${color.b})`}} className="color" />
            </div>
            {isOpen && (
                <div className="picker" ref={ref}>
                    <TwitterPicker onChangeComplete={handleChangeComplete} triangle="hide" />
                </div>
            )}
        </div>
    );
};

export default ColorPicker;
