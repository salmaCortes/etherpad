import React, { useState } from 'react';
import axios from 'axios';

const ETHERPAD_API_URL = 'http://localhost:9001/api/1';
const API_KEY = '88cd01a8205f9dd910125770de87f274365cc21d52bf0709d56f80c171350d05';

const Etherpad = () => {
  const [crearPad, setcrearPad] = useState('');
  
  const handleCrearPad = async () => {
    try {
      const url = `${ETHERPAD_API_URL}/createPad?padID=${crearPad}&apikey=${API_KEY}`;
      await axios.post(url);
      setcrearPad('');
    } catch (error) {
      console.error('Error al crear el archivo:', error);
    }
  };

  return (
    <div>
      <h1>Bienvenido a Etherpad!</h1>
      <div>
        <h2>Crear un nuevo archivo (pad)</h2>
        <input
          type="text"
          value={crearPad}
          onChange={(event) => setcrearPad(event.target.value)}
          placeholder="Ingresa el nombre del archivo"
        />
        <button onClick={handleCrearPad}>Create Pad</button>
      </div>
    </div>
  );
};

export default Etherpad;
