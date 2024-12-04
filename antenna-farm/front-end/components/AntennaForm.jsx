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

    //Yagi useStates
    const [elements, setElements] = useState('5');
    const [boomDiameter, setBoomDiameter] = useState('20')
    const [boomRelation, setBoomRelation] = useState('center_connected')

    //Other useStates
    const [diameter, setDiameter] = useState('5');
    const [material, setMaterial] = useState('copper');

    const isYagi = antenna.pathname === '/yagi';
    const isMoxon = antenna.pathname === '/moxon';

    const urlMake = () => {
        if (isYagi === true) {
            return `elements=${elements}&boomDiameter=${boomDiameter}&boomRelation=${boomRelation}`
        }
        else {
            return ''
        }
    }

    const handleChange = async() => {

        try{      
            const addEnd = urlMake()
            const url = `http://127.0.0.1:8000/rpc/v1${antenna.pathname}/?freq=${freq}&hertz=${hertz}&waveLength=${waveLength}&diameter=${diameter}&material=${material}&unit=${unit}&${addEnd}`;      
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

    const handleUnitButton = () => {
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

    }, [freq, hertz, waveLength, unit, diameter]);

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

                <div>
                    <label>Materiel Diameter</label>
                    <input 
                    type="number"
                    value={diameter}
                    placeholder="Wire diameter"
                    onChange={(e) => setDiameter(e.target.value)} />
                </div>

                <div>
                    <label>Material</label>
                    <select
                    value={material}
                    placeholder="material"
                    onChange={(e) => setMaterial(e.target.value)}
                    >
                        <option value="copper">Copper</option>
                        <option value="aluminum">Aluminum</option>
                    </select>
                </div>

                <div className="input">
                    <label>Quick Bands: </label>
                    <select 
                    value={freq} 
                    id="quickBands"
                    onChange={(e) => setFreq(e.target.value)}>
                        <option>Select a band</option>
                        <option value="435">70 Centimeter</option>
                        <option value="146">2 Meter</option>
                        <option value="155">2 Meter Ext.</option>
                        <option value="14.175">20 Meter</option>
                        <option value="7.15">40 Meter</option>
                    </select>
                </div>


                {isYagi && (
                    <>
                        <div>
                            <label>Number of Elements: </label>
                            <input 
                            type="number"
                            value={elements}
                            placeholder="Elements"
                            onChange={(e) => setElements(e.target.value)}
                            />
                        </div>

                        <div>
                            <label>Boom Width</label>
                            <input 
                            type="number"
                            value={boomDiameter}
                            placeholder="Boom Diameter"
                            onChange={(e) => setBoomDiameter(e.target.value)} 
                            />
                        </div>

                        <div>
                            <label>Boom Relation</label>
                            <select
                            placeholder="Boom Materiel" 
                            value={boomRelation}
                            onChange={(e) => setBoomRelation(e.target.value)}
                            >
                                <option value="center_connected">Elements are electrically connected to the boom.</option>
                                <option value="insulated">Boom is insulated and elements are isolated and centered from the boom.</option>
                                <option value="isolated_above">Elements are isolated and on top of the boom.</option>
                            </select>
                        </div>
                    </>
                )}
                

                <div className="answer input output">
                    <p className="antLength"></p> 
                    <button onClick={handleUnitButton} className="lenUnit">Metric</button>
                </div>
        </div>
    )
}

export default AntennaForm