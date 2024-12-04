import AntennaForm from "../components/AntennaForm";
import { useState } from "react";


function Yagi() {
    const [data, setData] = useState(null);

    const updateData = (newData) => {
        setData(newData);
        console.log("Fetched Data:", newData)
    };
    return (
        <>
            <h1>Yagi</h1>

            <AntennaForm onDataFetched={updateData}/>

            <div>
                <p>{data ? `Reflector Length: ${data.reflectorLength} Meters` : "Reflector Length: 0"}</p>
                <p>{data ? `Driver Length: ${data.driverLength} Meters`: "Driver Length: 0"}</p>
                <p>{data ? `Driver Space: ${data.driverSpace} Meters` : "Driver Space: 0"}</p>
                <p>{data ? `Number of Directors: ${data.dirLengths.length}` : "Driver Space: 0"}</p>
            </div>
        </>
    )
}

export default Yagi