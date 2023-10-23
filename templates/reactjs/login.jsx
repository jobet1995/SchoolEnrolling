import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Login(){
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const containerClass = isLoggedIn ? 'container logged-in' : 'container';
  
  const handleLogin = () => {
    if(username === 'admin' && password === 'admin1234'){
      setIsLoggedIn(true);
    }
    else{
      setIsLoggedIn(false);
      alert('Invalid username or password. Please try again');
    }
  };

  return(
    <div className={containerClass}>
      <h2>LoginPage</h2>
      {isLoggedIn ? (
      <div>
        <p>You are logged in as {username}</p>
      </div>
      ) : (
      <form>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Username"
            value={username}
            onchange={(e) => setUsername(e.target.value)}
          />
        </div>
      </form>
      )}
    </div>
  )
}