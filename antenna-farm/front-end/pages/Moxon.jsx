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

            <div>
                <img src="../images/moxon.png" alt="" />

                <p>A: {data ? `${data.a}` : '0'}</p>
                <p>B: {data ? `${data.b}` : '0'}</p>
                <p>C: {data ? `${data.c}` : '0'}</p>
                <p>D: {data ? `${data.d}` : '0'}</p>
                <p>E:</p>
            </div>
        </>
    );
};

export default Moxon