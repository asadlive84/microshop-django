import React from 'react'

const OrderedAll = ({id,product_name,product_price,customer_paid,unpaid_money,created_at,paid_status}) => {
    return (
        <tr>
            <td >{product_name}</td>
            <td>{product_price}</td>
            <td>{customer_paid}</td>
            <td>{paid_status ? 'paid':'du'}</td>
            <td>{unpaid_money}</td>
            <td>{created_at}</td>
        </tr>
    )
}

export default OrderedAll
