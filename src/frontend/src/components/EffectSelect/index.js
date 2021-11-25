import { connect } from 'react-redux';
import Effects from './Effects';
import { changeEffect } from '../../store/actions';

const mapStateToProps = state => ({
    effect: state.effect,
    disabled: !state.isEnable,
});

const mapDispatchToProps = dispatch => ({
    onSelect: (effect) => dispatch(changeEffect(effect)),
});

export const ConnectedEffects = connect(
    mapStateToProps,
    mapDispatchToProps,
)(Effects);
