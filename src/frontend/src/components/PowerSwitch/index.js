import { connect } from 'react-redux';
import PowerSwitch from './PowerSwitch';
import { turnOff, turnOn } from '../../store/actions';

const mapStateToProps = state => ({
    isEnable: state.isEnable,
});

const mapDispatchToProps = dispatch => ({
    turnOn: () => dispatch(turnOn()),
    turnOff: () => dispatch(turnOff()),
});

export const ConnectedPowerSwitch = connect(
    mapStateToProps,
    mapDispatchToProps,
)(PowerSwitch);
