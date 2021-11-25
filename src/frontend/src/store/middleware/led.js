import axios from 'axios';
import { LED_URL } from '../../urls';
import { Action } from '../actions';
import { EffectsType } from '../../components/EffectSelect/constants';

export const led = store => next => action => {
    switch (action.type) {
        case Action.ChangeColor:
            const {r, g, b} = action.payload;
            axios.post(LED_URL, {
                color: {r, g, b},
                effect: store.getState().effect,
            });
            break;
        case Action.TurnOn:
            const {color, effect} = store.getState();
            axios.post(LED_URL, {
                color: {r: color.r, g: color.g, b: color.b},
                effect: effect,
            });
            break;
        case Action.TurnOff:
            axios.post(LED_URL, {
                color: {r: 0, g: 0, b: 0},
                effect: EffectsType.Instant,
            });
            break;
    }

    return next(action);
};
