import { useState, useEffect } from "react"
import { Form } from "react-bootstrap"
import axios from "axios";
import { useLocation } from "react-router-dom";


function AntennaForm() {
    const antenna = useLocation(); // antenna.pathname
    const [freq, setFreq] = useState('');
    const [hertz, setHertz] = useState('MHz');
    const [waveLength, setWaveLength] = useState('1/2');
    const [unit, setUnit] = useState('Standard');
    const [result, setResult] = useState(null);


    const handleChange = async() => {
        const response = await fetch(`http:/127.0.0.1:8000/api/v1/`);
        const data = await response.json();
        console.log("API Respnse:", data);
        setResult(data.result);
    };

    useEffect(() => {
        
        //console.log(antenna)
    }, [freq, hertz, waveLength, unit]);

    return(
        <div className="panel">
            <div class="input freqHrtz">
                <input
                    type="number"
                    value={freq}
                    onChange={(e) => setFreq(e.target.value)}
                    placeholder="Enter Frequency"
                />
                <div>
                    <select 
                    value={hertz} 
                    onChange={(e) => setHertz(e.target.value)} 
                    id="hertzSelector">
                        <option value="1">MHz</option>
                        <option value=".001">KHz</option>
                        <option value="1000">GHz</option>
                    </select>
                </div>

                </div>


                <div class="input">
                    <label for="Wavelength">Wavelength:</label>
                    <select 
                    value={waveLength}
                    onChange={(e) => setWaveLength(e.target.value)}
                    id="wavelengthSelector">
                        <option value="half">1/2</option>
                        <option value="quarter">1/4</option>
                        <option value="full">Full</option>
                    </select>
                </div>

                {/* Add useState for Quick Bands */}
                <div class="input">
                    <label for="bands">Quick Bands: </label>
                    <select name="QuickBands" id="quickBands">
                        <option>Select a band</option>
                        <option value="435">70 Centimeter</option>
                        <option value="146">2 Meter</option>
                        <option value="155">2 Meter Ext.</option>
                        <option value="14.175">20 Meter</option>
                        <option value="7.15">40 Meter</option>
                    </select>
                </div>

                <div>
                    <button>Calculate</button>
                </div>

                <div class="answer input output">
                    <p class="antLength"></p> 
                    <button class="lenUnit">Metric</button>
                </div>
        </div>
    )
}

export default AntennaForm