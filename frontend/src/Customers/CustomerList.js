import React from 'react'

import CustomersDetails from './CustomersDetails'

const CustomerList = ({customers}) => {
    return (
        <div className="row">
            {customers.map( customer => <CustomersDetails {...customer}/> )}
        </div>
    )
}

export default CustomerList
