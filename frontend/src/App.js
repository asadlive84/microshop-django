import React, {useState, useEffect} from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import axios from 'axios'
import './App.css';
import CustomerList from './Customers/CustomerList'
import NavBar from './NavBar/NavBar'

import SingleCustomer from './Customers/SingleCustomer'



const App = () => {

  const [getCustomers, setGetCustomers] = useState([])
  const [customers, setCustomers] = useState([...getCustomers])
  const [keywords, setKeywords] = useState("")
  const [individualCustomer, setIndividualCustomer] = useState([])

 

  

  useEffect( () => {
    axios
    .get("http://127.0.0.1:8000/api/v1/customer_list/")
    .then(response => setGetCustomers(response.data))

    const cus = getCustomers.filter(customer=>customer.name.includes(keywords) || customer.phone_number.includes(keywords))
    setCustomers(cus)

    
    
    
  },[keywords])
  

  
 
  
  return (
   
    <div className="App">
      <Router>
        <NavBar setKeywords={setKeywords}/>
        <Switch>
          <Route exact path="/">
            <CustomerList customers={customers} />
          </Route>
            <Route exact path="/customer_details/:customerId" component={()=><SingleCustomer  />} />
        </Switch>
        
      </Router>
      
    </div>
  );
}

export default App;
