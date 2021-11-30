import React from "react";
import ReactDOM from "react-dom";
import {useEffect} from 'react';
import App from './App';

// import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
// import './App.css';

// import App from './app';


// var obj;
// fetch(' http://127.0.0.1:5000/users/3')
//   .then(response => response.json())
//   .then(data => obj=data)
//   // .then(() => console.log(obj))

  
// alert(obj)
// alert(obj.username)

async function fetchExam() {
  try {
      const response = await fetch("http://127.0.0.1:5000/users/3", {
          method: 'GET',
          credentials: 'same-origin'
      });
      const exam = await response.json();
      return exam;
  } catch (error) {
      console.error(error);
  }
}
var item;

async function renderExam() {
  exam = await fetchExam();
  alert(exam.username);
  item=exam.username
  
}
//not able to access variable outside of async function 
renderExam()
// alert(exam.username)



class HelloWorld extends React.Component {
  render() {
      return (
          <h1>Hello, {item} </h1>
      );
  }}

  ReactDOM.render(<HelloWorld />, document.getElementById("root"));




// async function fetchJSON() {
//   const response = await fetch('http://127.0.0.1:5000/users/3');
//   const data = await response.json();
//   return data;
// }


// let obj;
// fetchJSON().then(data => {
//   obj=data; // fetched movies
// });

// console.log(obj)











// function App() {
//   const [currentTime, setCurrentTime] = useState(0);

//   useEffect(() => {
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     });
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">

//         ... no changes in this part ...

//         <p>The current time is {currentTime}.</p>
//       </header>
//     </div>
//   );
// }

// export default App;