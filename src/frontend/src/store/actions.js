export const Action = Object.freeze({
    ChangeColor: 'CHANGE_COLOR',
    ChangeEffect: 'CHANGE_EFFECT',
    TurnOn: 'TURN_ON',
    TurnOff: 'TURN_OFF',
});

export const changeColor = (color) => ({
    type: Action.ChangeColor,
    payload: color,
});

export const changeEffect = (effect) => ({
    type: Action.ChangeEffect,
    payload: effect,
});

export const turnOn = () => ({
    type: Action.TurnOn,
});

export const turnOff = () => ({
    type: Action.TurnOff,
});
