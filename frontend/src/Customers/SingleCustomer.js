import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import getItem from './getItem'
import OrderedAll from './OrderedAll'

const SingleCustomer = () => {
   
    const {customerId} = useParams()
    const [singleCustomer, setSingleCustomer] = useState([])

    async function fetchData(){
        const res = await fetch(`http://127.0.0.1:8000/api/v1/customer_list/${parseInt(customerId)}`);
        res.json().then(res=>setSingleCustomer(res))

    }

    useEffect(()=>{
        fetchData();
    },[])

    
   
   const{
    name,
    phone_number,
    address,
    created_at,
    paid_money,
    unpaid_money,
    paid_status,
    customer_credit,
    customer_debit,
    ac_last_updated,
    ordered_set,
   } = singleCustomer;
   const totaProductPrice = ordered_set && ordered_set.reduce((sum, cur) => sum + parseFloat(cur.product_price),0 )
   const totatCustomerPaid = ordered_set && ordered_set.reduce((sum, cur) => sum + parseFloat(cur.customer_paid),0 )
   const totatCustomerUnPaid = ordered_set && ordered_set.reduce((sum, cur) => sum + parseFloat(cur.unpaid_money),0 )

   
   
   
return (
        
        <React.Fragment>
           <div>
               <h1>Name: {name}</h1>
               <p>Phone Number: {phone_number}</p>
               <p>Address: {address}</p>
               <p>Created: {created_at}</p>
               <p>Paid: {paid_money}</p>
               <p>Unpaid: {unpaid_money}</p>
               <p>Credit: {customer_credit}</p>
               <p>Debit: {customer_debit}</p>
               <p>Status: {paid_status ? 'Paid':'Due'}</p>
               <p>Updated: {ac_last_updated}</p>
               <table class="table">
                    <thead>
                    <tr>
                        <th>Product Name</th>
                        <th>Price</th>
                        <th>Customer Paid</th>
                        
                        <th>Status</th>
                        <th>Customer UnPaid</th>
                        <th>Date</th>
                    </tr>
                    </thead>
                    
                    {ordered_set && (
                   <tbody>
                        
                       {ordered_set.map(order=> <OrderedAll {...order} />  )}
                       <tr>
                           <th></th>
                           <th>{totaProductPrice}</th>
                           <th>{totatCustomerPaid}</th>
                           <th></th>
                           
                           <th>{totatCustomerUnPaid}</th>
                       </tr>
                    </tbody>
               )}
                    
                </table>

               
           </div>
        </React.Fragment>
    )
}

export default SingleCustomer
