import React, { Component }  from 'react';
import { Products } from "./components/Product";
import { BrowserRouter, Routes, Route } from "react-router-dom"

function App() {
  return <BrowserRouter>
    <Routes>
      <Route path="/" element={<Products />} />
    </Routes>
  </BrowserRouter>;
}

export default App;
