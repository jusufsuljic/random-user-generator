import axios from 'axios'
import React, { useEffect, useState } from 'react'
import JSONPretty from 'react-json-pretty'
import './App.css';

function App() {

  const [randomUser, setRandomUser] = useState('')
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    loadUser()
  }, [])

  const loadUser = () => {
    axios.get('http://localhost:80/random-user').then(res => {
      console.log("Random user generated successfully!.", res.data);
      setRandomUser(res.data);
      setCopied(false)
    }).catch(error => {
      console.log(error);
    })
  }

  const copyToCB = () => {
    navigator.clipboard.writeText(JSON.stringify(randomUser))
    setCopied(true);
  }

  return (
    <div className="App">
      <div className="container">
        <h1 className="title">random-user-generator</h1>
        <div className="card">
          {/* <img className="avatarImg" src={`https://avatars.dicebear.com/api/adventurer/${randomUser.firstName}.svg`} alt="Avatar" style={{'width':'60%'}} /> */}
          <div className="card-container">
            <JSONPretty id="json-pretty" data={randomUser}></JSONPretty>
          </div>
        </div>
        <br />
        <div className="btnContainer">
          <button className="generate" onClick={() => loadUser()}>Generate</button>
          <button className="copy" onClick={() => copyToCB()}>Copy</button>
        </div>
        {copied && <p style={{'color': 'white'}}>Copied to clipboard.</p>}
        {/* <p className="user">{JSON.stringify(randomUser, null, 2)}</p> */}
      </div>
    </div>
  );
}

export default App;
