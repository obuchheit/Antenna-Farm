import { useState } from "react"
import AntennaForm from "../components/AntennaForm"

function Dipole() {
    const [data, setData] = useState(null);

    const updateData = (newData) => {
        setData(newData);
        console.log("Fetched Data:", newData)
    };

    return (
        <>
            <h1>Dipole</h1>
            <AntennaForm onDataFetched={updateData}/>
            <div>
                <div className="mesBorder">
                    <div className="mes">{data ? `${data.elementLength}` : "0 in"}</div>
                    <div className="mes mes1">{data ? `${data.elementLength}` : "0 in"}</div>
                </div>
                
                <div className="antennaBorder">
                    <div className="antenna"></div>
                    <div className="antenna"></div>
                </div>
            </div>

            <div className="connectors">
                <span className="dot"></span>
                <span className="dot"></span>
            </div>
        </>
    )
}

export default Dipole