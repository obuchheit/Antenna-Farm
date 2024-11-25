import AntennaForm from "../components/AntennaForm"

function Dipole() {
    return (
        <>
            <h1>Dipole</h1>
            <AntennaForm />
            <div>
                <div class="mesBorder">
                    <div class="mes">0 in</div>
                    <div class="mes mes1">0 in</div>
                </div>
                
                <div class="antennaBorder">
                    <div class="antenna"></div>
                    <div class="antenna"></div>
                </div>
            </div>

            <div class="connectors">
                <span class="dot"></span>
                <span class="dot"></span>
            </div>
        </>
    )
}

export default Dipole