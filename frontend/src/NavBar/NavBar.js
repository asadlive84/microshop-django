import React from 'react';
import {
  Link
} from "react-router-dom";


const NavBar = ({setKeywords}) => {

  const HandleChange = e => {
    setKeywords(e.target.value)
  }

  return(
    <nav className="navbar navbar-expand-sm bg-dark navbar-dark sticky-top">
      <Link to="/" className="navbar navbar-expand-sm bg-dark navbar-dark sticky-top">Home</Link>
      {/* <a className="navbar-brand" href="">Microshop</a> */}
      <ul className="navbar-nav">
        <li className="nav-item">
          {/* <a className="nav-link" href="">Link</a> */}
        </li>
        <li className="nav-item">
          {/* <a className="nav-link" href="">Link</a> */}
        </li>
      </ul>
      <input onChange={HandleChange} className="form-control mr-sm-2" type="text" placeholder="Search"/>
    </nav>
  )
}

export default NavBar;
