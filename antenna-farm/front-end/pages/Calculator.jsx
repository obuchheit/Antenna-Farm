import { useState } from 'react';
import axios from 'axios';

function Calculator() {
    const [num1, setNum1] = useState('');
    const [num2, setNum2] = useState('');
    const [operation, setOperation] = useState('+');
    const [result, setResult] = useState(null);

    const handleCalculate = async () => {
        const response = await fetch(`http://127.0.0.1:8000/api/v1/calculate/?num1=${num1}&num2=${num2}&operation=${operation}`);
        const data = await response.json();
        console.log("API response:", data);
        setResult(data.result);
    };
    return (
        <div>
            <h1>Calculator</h1>
            <input
                type="number"
                value={num1}
                onChange={(e) => setNum1(e.target.value)}
                placeholder="Enter first number"
            />
            <input
                type="number"
                value={num2}
                onChange={(e) => setNum2(e.target.value)}
                placeholder="Enter second number"
            />
            <select value={operation} onChange={(e) => setOperation(e.target.value)}>
                <option value="plus">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select>
            <button onClick={handleCalculate}>Calculate</button>

            {result !== null && <div>Result: {result}</div>}
        </div>
    );
};

export default Calculator;