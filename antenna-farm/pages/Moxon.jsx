import AntennaForm from "../components/AntennaForm"

function Moxon() {
    return (
        <>
            <h1>Moxon</h1>

            <AntennaForm />

            <div class="antennaDisplay">
                <div class="connectors">
                    <span class="dot"></span>
                    <span class="dot"></span>
                </div>
                
                <div class="antennaBorder">
                    <div class="antenna leftEl"></div>
                    <div class="antenna rightEl"></div>
                </div>
                
                <div class="reflectorContainer">
                    <div class="reflector"></div>
                </div>
            </div>
        </>
    );
};

export default Moxon