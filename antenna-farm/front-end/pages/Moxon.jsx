import AntennaForm from "../components/AntennaForm"
import { useState } from "react";

function Moxon() {
    const [data, setData] = useState(null);

    const updateData = (newData) => {
        setData(newData);
        console.log("Fetched Data:", newData)
    };

    return (
        <>
            <h1>Moxon</h1>

            <AntennaForm onDataFetched={updateData}/>

            <div className="antennaDisplay">
                <div className="connectors">
                    <span className="dot"></span>
                    <span className="dot"></span>
                </div>
                
                <div className="antennaBorder">
                    <div className="antenna leftEl"></div>
                    <div className="antenna rightEl"></div>
                </div>
                
                <div className="reflectorContainer">
                    <div className="reflector"></div>
                </div>
            </div>

            <div>
                <p>{data ? `${data.a}` : '0'}</p>
                <p>{data ? `${data.b}` : '0'}</p>
                <p>{data ? `${data.c}` : '0'}</p>
                <p>{data ? `${data.d}` : '0'}</p>
            </div>
        </>
    );
};

export default Moxon