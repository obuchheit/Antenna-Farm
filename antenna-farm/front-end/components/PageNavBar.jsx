import { Container, Nav, Navbar, NavDropdown, Button } from "react-bootstrap"
import { Link } from "react-router-dom"
import { signOut } from "../utilities";

function PageNavBar({ user, setUser }) {
    const logOut = async() => {
        setUser(await signOut(user))
    }
    return (
        <>
            <Navbar expand="lg" className="bg-body-tertiary">
                <Container>
                    
                    <Navbar.Brand as={Link} to="/">Antenna Farm</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link href="#link">About</Nav.Link>
                        <NavDropdown title="Antenna Calculators" id="basic-nav-dropdown">
                        <NavDropdown.Item as={Link} to="/dipole">
                            Dipole
                        </NavDropdown.Item>

                        <NavDropdown.Item as={Link} to="/moxon">
                            Moxon
                        </NavDropdown.Item>

                        <NavDropdown.Item as={Link} to="/yagi">
                            Yagi
                        </NavDropdown.Item>

                        
                        <NavDropdown.Divider />
                        <NavDropdown.Item as={Link} to="/calculator">
                            Simple Calculator
                        </NavDropdown.Item>
                        </NavDropdown>
                    </Nav>

                    {user ? (
                        <>
                            <Nav>
                                <Nav.Link>Saved Antennas</Nav.Link>
                            </Nav>
                            <Button onClick={logOut}>Logout</Button>
                        </>
                    ) : (
                        <>
                            <Nav>
                                <Nav.Link as={Link} to='/login'>Login/Signup</Nav.Link>
                            </Nav>
                        </>
                    )

                    }
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
};

export default PageNavBar