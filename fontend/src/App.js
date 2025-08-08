import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    ph: '',
    turbidity: '',
    chlorine: '',
    temp: '',
    do: '',
    tds: '',
    hardness: '',
    sulfate: '',
    conductivity: ''
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          ph: parseFloat(formData.ph),
          turbidity: parseFloat(formData.turbidity),
          chlorine: parseFloat(formData.chlorine),
          temp: parseFloat(formData.temp),
          do: parseFloat(formData.do),
          tds: parseFloat(formData.tds),
          hardness: parseFloat(formData.hardness),
          sulfate: parseFloat(formData.sulfate),
          conductivity: parseFloat(formData.conductivity)
        })
      });

      const data = await response.json();
      setPrediction(data.prediction);
      setError(null);
    } catch (err) {
      setError('❌ Error: ' + err.message);
      setPrediction(null);
    }
  };

  return (
    <div className="App">
      <h2>💧 Smart Water Quality Predictor</h2>

      {Object.keys(formData).map((key) => (
        <div key={key}>
          <label>{key.toUpperCase()}: </label>
          <input
            type="number"
            name={key}
            value={formData[key]}
            onChange={handleChange}
            step="any"
          />
        </div>
      ))}

      <button onClick={handleSubmit}>Predict</button>

      {prediction && <h3>✅ Prediction: {prediction}</h3>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
