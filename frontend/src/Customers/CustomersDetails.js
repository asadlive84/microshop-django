import React from 'react'
import { Link } from 'react-router-dom'

const CustomersDetails = ({id,name,phone_number,address,paid_money,unpaid_money,paid_status,customer_credit,customer_debit}) => {
    return (
        <div className="col-sm-3">
            <h3>Name: 
                <Link to={`/customer_details/${id}`}>{name}</Link>
            </h3>
            <p>Phone: {phone_number}</p>
            <p>Address: {address}</p>
            <p>Paid Money: {paid_money} TK</p>
            <p>Unpaid Money: {unpaid_money} TK</p>
            <p>Status: {paid_status} TK</p>
            <p>Credit: {customer_credit} TK</p>
            <p>Debit: {customer_debit} TK</p>
        </div>
    )
}

export default CustomersDetails
