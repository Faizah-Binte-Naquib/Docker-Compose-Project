import './Table.css';
import React, { useState,useEffect } from 'react';

function Table() {

  const [userData, setuserData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8001/backend/v1.0/users',{ headers : { 
      'Content-Type': 'application/json',
      'Accept': 'application/json'
     }})
    .then(response => response.json()
    .then(data => setuserData(data))
  )}, []);





  return (
    <>
      <table className="table">
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Mobile</th>
          </tr>
        </thead>
        {userData.map(user => {
            return(
        <tbody>
            <td>{user.firstname}</td>
            <td>{user.lastname}</td>
            <td>{user.email}</td>
            <td>{user.phone}</td>
            
        </tbody>
           );
          })}
      </table>
    </>
  );
}

export default Table;
