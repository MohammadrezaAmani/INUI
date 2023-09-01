import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <div className="App">

      <header className="App-header">
        <p>
          This is your First <i>INUI REACT app</i>
        </p>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://inui.readthedocs.io/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn INUI
        </a>
      </header>
    </div>
  </React.StrictMode>
);