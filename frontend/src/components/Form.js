import './Form.css';
import React, { useState } from "react";

function Form() {
const [firstname, setfirstName] = useState('');
const [lastname, setlastName] = useState('');
const [email, setEmail] = useState('');
const [phone, setPhone] = useState('');


const onFirstnameChange = e => setfirstName(e.target.value);
const onLastnameChange = e => setlastName(e.target.value);
const onEmail = e => setEmail(e.target.value);
const onPhone = e => setPhone(e.target.value);

const handleSubmit = e => {
    e.preventDefault();

    const data = { firstname, lastname, email, phone };
     const requestOptions = {
      method: "POST",
      headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      "Access-Control-Allow-Origin": "*",    
      "Access-Control-Allow-Methods": "POST" },
      body: JSON.stringify(data)
    };
    fetch('http://localhost:8001/backend/v1.0/posts',{method:"POST",body:JSON.stringify(data)})
      .then(response => response.json())
      .then(res => console.log(res));
  };

return (
    <>
    <form>
        <label>
            First Name:
        </label>
            <input type="text" name="firstname" onChange={onFirstnameChange}/>

        <label>
            Last Name:
        </label>
        <input type="text" name="lastname" onChange={onLastnameChange}/>
        
        <label>
            Email Address:
        </label>
        <input type="text" name="email" onChange={onEmail}/>
        
        <label>
            Mobile Number:
        </label>
        <input type="text" name="phone" onChange={onPhone}/>

        <input type="submit" value="Submit" onClick={handleSubmit}/>
    </form>
    </>
  );
}

export default Form;
