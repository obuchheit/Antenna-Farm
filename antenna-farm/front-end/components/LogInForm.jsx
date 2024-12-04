import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Link, useOutletContext } from 'react-router-dom';
import { useState } from 'react';
import { userLogIn } from '../utilities';

function LogInForm() {
    const { setUser } = useOutletContext();
    const [identifier, setIdentifier] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async(e) => {
        e.preventDefault()
        let formData = {
            'identifier': identifier,
            'password': password,
        }
        setUser(await userLogIn(formData));
    }
    return (
        <Form onSubmit={(e) => handleSubmit(e)}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Username</Form.Label>
            <Form.Control 
            value={identifier}
            onChange={(e) => setIdentifier(e.target.value)}
            type="username" 
            placeholder="Enter username or email" 
            />

        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type="password" 
            placeholder="Password" 
            />
        </Form.Group>
        <Button variant="primary" type="submit">
            Submit
        </Button>
        <Button as={Link} to="/register" variant="secondary">
            Sign Up
        </Button>
        </Form>
    );
};

export default LogInForm;