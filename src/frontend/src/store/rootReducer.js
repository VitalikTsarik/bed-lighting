import { EffectsType } from '../components/EffectSelect/constants';
import { Action } from './actions';

const defaultState = {
    isEnable: true,
    color: {
        r: 0,
        g: 0,
        b: 0,
    },
    effect: EffectsType.ScrollOut,
};

export const rootReducer = (state = defaultState, action) => {
    switch (action.type) {
        case Action.ChangeColor:
            return {...state, color: action.payload};
        case Action.ChangeEffect:
            return {...state, effect: action.payload};
        case Action.TurnOn:
            if (!state.isEnable) {
                return {...state, isEnable: true};
            } else {
                return state;
            }
        case Action.TurnOff:
            if (state.isEnable) {
                return {...state, isEnable: false};
            } else {
                return state;
            }
        default:
            return state;
    }
};
