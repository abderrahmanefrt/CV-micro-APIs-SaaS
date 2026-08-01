import { useState } from "react";
import axios from "axios";

interface RegisterResponse {
  email: string;
  api_key: string;
}

function Register() {
  const [email, setEmail]= useState("");
  const [password, setPassword]= useState("");
  const [apikey, setApikey]= useState<string | null>(null);

  const handleSubmit = async ()=> {
    try{
      const response= await axios.post<RegisterResponse>("http://localhost:8000/api/register",{
        email,
        password
      })
      setApikey(response.data.api_key);
    }catch(error){
      console.error("Erreur lors de l'inscription:", error);
    }
  }


return (
  <div>
    <input type="email" value={email} onChange={(e)=>setEmail(e.target.value)} placeholder="Email" />
    <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)} placeholder="Mot de passe" />
    <button onClick={handleSubmit}>S'inscrire</button>
    {apikey && <p>Votre clé API: {apikey}</p>}
  </div>
)
}

export default Register;