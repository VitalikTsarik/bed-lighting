import { changeColor } from '../../store/actions';
import { connect } from 'react-redux';
import ColorPicker from './ColorPicker';

const mapStateToProps = state => ({
    color: state.color,
    disabled: !state.isEnable,
});

const mapDispatchToProps = dispatch => ({
    onChangeColor: (color) => dispatch(changeColor(color)),
});

export const ConnectedColorPicker = connect(
    mapStateToProps,
    mapDispatchToProps,
)(ColorPicker);
