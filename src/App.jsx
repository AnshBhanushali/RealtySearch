import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import SignIn from './pages/signin'
import SignUp from './pages/signup'
import About from './pages/about'
import Profile from './pages/profile'
import Home from './pages/home'

export default function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />}/>
      <Route path="/sign-in" element={<SignIn />}/>
      <Route path="/sign-up" element={<SignUp/>}/>
      <Route path="/about" element={<About />}/>
      <Route path="/profile" element={<Profile />}/>
    </Routes>
    </BrowserRouter>
  )
}
