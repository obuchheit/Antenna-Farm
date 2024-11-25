import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "../pages/HomePage.jsx";
import Calculator from "../pages/Calculator.jsx";
import Dipole from "../pages/Dipole.jsx";
import Moxon from "../pages/Moxon.jsx";
import Yagi from "../pages/Yagi.jsx";
import AntennaForm from "../components/AntennaForm.jsx";
import Error404Page from "../pages/Error404Page.jsx"


const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true, 
                element: <HomePage />
            },
            {
                path: "/dipole",
                element: <Dipole />
            },
            {
                path: "/calculator",
                element: <Calculator />
            },
            {
                path: "/moxon",
                element: <Moxon />
            },
            {
                path: "/yagi",
                element: <Yagi />
            }
        ],
        errorElement: <Error404Page />
    }
]);

export default router
