import './App.css';
import { ConnectedColorPicker } from '../ColorPicker';
import { ConnectedEffects } from '../EffectSelect';
import { ConnectedPowerSwitch } from '../PowerSwitch';

const App = () => {
    return (
        <div className="App">
            <header className="content">
                <div>
                    <ConnectedPowerSwitch />
                </div>
                <div className="colorPicker">
                    <ConnectedColorPicker />
                </div>
                <div className="effects">
                    <ConnectedEffects />
                </div>
            </header>
        </div>
    );
};

export default App;
