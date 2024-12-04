import { useState } from "react";
import Form from 'react-bootstrap/Form';
import { Button } from "react-bootstrap";
import { userRegistration } from "../utilities";
import { useOutletContext } from "react-router-dom";

function RegistrationForm() {
    const { setUser }  = useOutletContext();
    const [email, setEmail] = useState(''); 
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState(''); 
    const [isReady, setIsReady] = useState(false);

    const handleSubmit = async(e) => {
        e.preventDefault()
        if (isReady) {
            let formData = {
                'email': email,
                'username': username,
                'password': password
            }
            setUser(await userLogIn(formData));
        }
        else {
            alert("You must check the box before submitting.")
        }    
    }

    return (
        <Form onSubmit={(e) => handleSubmit(e)}>
            <Form.Group className="mb-3" controlId="formGroupEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control 
                value={email}
                onChange={(e)=> setEmail(e.target.value)}
                type="email" 
                placeholder="Enter email" 
                />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formGroupEmail">
                <Form.Label>Username</Form.Label>
                <Form.Control 
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                type="username" 
                placeholder="Enter username" 
                />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formGroupPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                type="password" 
                placeholder="Password" />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicCheckbox">
                <Form.Check 
                value={isReady}
                onChange={(e) => setIsReady(e.target.checked)}
                type="checkbox" 
                label="All the info is correct" />
            </Form.Group>
            <Button variant="primary" type="submit">
                Submit
            </Button>
        </Form>
    );
}

export default RegistrationForm;