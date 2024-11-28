import { useState, useEffect } from "react"
import { Form } from "react-bootstrap"
import axios from "axios";
import { useLocation } from "react-router-dom";


function AntennaForm({ onDataFetched }) {
    const antenna = useLocation(); // antenna.pathname
    const [freq, setFreq] = useState('');
    const [hertz, setHertz] = useState('1');
    const [waveLength, setWaveLength] = useState('half');
    const [unit, setUnit] = useState('standard');    

    const handleChange = async() => {

        try{      
            const url = `http://127.0.0.1:8000/api/v1${antenna.pathname}/?freq=${freq}&hertz=${hertz}&waveLength=${waveLength}&unit=${unit}`;      
            const response = await axios.get(url);
            console.log("API Respnse:", response.data);
            onDataFetched(response.data);

        }
        catch (error) {
            console.error("Error fetching data:", error.message);
            console.error("Error response:", error.response);
            console.error("Request URL:", error.config.url);
        }
    };

    const handleButton = () => {
        if (unit === 'metric') {
            setUnit('standard')
        }
        else {
            setUnit('metric')
        }
    }

    useEffect(() => {
        if (freq && hertz && waveLength && unit) {
            handleChange();
        }

    }, [freq, hertz, waveLength, unit]);

    return(
        <div className="panel">
            <div className="input freqHrtz">
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


                <div className="input">
                    <label>Wavelength:</label>
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
                <div className="input">
                    <label>Quick Bands: </label>
                    <select name="QuickBands" id="quickBands">
                        <option>Select a band</option>
                        <option value="435">70 Centimeter</option>
                        <option value="146">2 Meter</option>
                        <option value="155">2 Meter Ext.</option>
                        <option value="14.175">20 Meter</option>
                        <option value="7.15">40 Meter</option>
                    </select>
                </div>

                <div className="answer input output">
                    <p className="antLength"></p> 
                    <button onClick={handleButton} className="lenUnit">Metric</button>
                </div>
        </div>
    )
}

export default AntennaForm