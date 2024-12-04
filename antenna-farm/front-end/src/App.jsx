import { Outlet, useLoaderData, useLocation, useNavigate } from 'react-router-dom';
import PageNavBar from '../components/PageNavBar';
import './index.css'
import { useEffect, useState } from 'react';
import { getInfo } from '../utilities';

function App() {
  const [user, setUser] = useState(useLoaderData());
  // const navigate = useNavigate()
  // const location = useLocation()

  return (
    <>
      <PageNavBar user={user} setUser={setUser}/>
      <Outlet context={{user, setUser}}/>
    </>
  );
};

export default App

