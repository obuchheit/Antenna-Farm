import { Outlet } from 'react-router-dom';
import PageNavBar from '../components/PageNavBar';
import './index.css'

function App() {

  return (
    <>
      <PageNavBar/>
      <Outlet />
    </>
  );
};

export default App

