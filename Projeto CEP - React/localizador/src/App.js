import { FaSearchLocation } from "react-icons/fa";
import { useState } from "react";
import './style.css'
import api from "./services/api";

function App() {

  const [input, setInput] = useState('')
  const [cep, setCep] = useState({})

  async function searchButton(){
    if(input === ''){
      alert("Digite um CEP!")
      return
    }
    try {
      const response = await api.get(`${input}/json`)
      setCep(response.data)
      setInput("")

    } 
    catch {
      alert("Ops! Algo deu errado")
      setInput("")
    }
  }

  return (
    <div className="container">
      
      <h1 className="title">Localizador CEP</h1>

      <div className="containerInput">
        <input
        type="text"
        placeholder="Digite seu cep..."
        value={input}
        onChange={(event) => setInput(event.target.value)}
        />

        <button className="searchLocation" onClick={searchButton}>
          <FaSearchLocation size={25} color="#FFF" />
        </button>

      </div>
      {Object.keys(cep).length > 0 &&(
        <main className='mainContent'>
        <h2>CEP: {cep.cep}</h2>
        <p>{cep.logradouro}</p>
        <p>Complemento: {cep.complemento}</p>
        <p>{cep.bairro}</p>
        <p>{cep.localidade} - {cep.uf}</p>
      </main>
      )}
      
    </div>
  );
}

export default App;
