// Importa React y Axios
import React from 'react';
import axios from 'axios';

// Define tu componente de React
const CreatePadEnEtherpad = () => {
  // Función para crear un pad en Etherpad a través de Django
  const crearPadEnEtherpad = async (padName) => {
    try {
      // Envía una solicitud POST a Django
      const response = await axios.post('http://127.0.0.1:8000/api/create_pad/', {
        padName: padName,
      });
      
      // Maneja la respuesta de Django
      console.log('Respuesta de Django:', response.data);
      // Aquí puedes actualizar el estado de tu componente o realizar otras acciones con la respuesta recibida

    } catch (error) {
      // Maneja errores de comunicación
      console.error('Error al comunicarse con Django:', error);
      // Aquí puedes manejar el error de acuerdo a tus necesidades
    }
  };

  // Llama a la función para crear un pad al montar el componente (ejemplo)
  React.useEffect(() => {
    crearPadEnEtherpad('kl');
  }, []);

  return (
    <div>
      <h1>Crear Pad en Etherpad</h1>
      {/* Puedes agregar más contenido o componentes aquí */}
    </div>
  );
};

// Exporta el componente para ser utilizado en otras partes de tu aplicación
export default CreatePadEnEtherpad;
