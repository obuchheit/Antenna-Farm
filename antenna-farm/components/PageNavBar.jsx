import { Container, Nav, Navbar, NavDropdown } from "react-bootstrap"
import { Link } from "react-router-dom"

function PageNavBar() {
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
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    )
}

export default PageNavBar