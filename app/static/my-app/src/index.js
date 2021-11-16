import {useEffect} from 'react';



// import { square, diag } from 'lib';
// var square = require('lib').square;


//   return () => {
//     cleanup
//   }
// }, [input])}



// import React from "react";
// import ReactDOM from "react-dom";
// import './index.css';

// document.body.style.backgroundColor = "red";
// alert("Hello! I am an alert box!!");

// const e = React.createElement;



// no JSX -
// class Hello extends React.Component {
//   render() {
//     return React.createElement('div', null, `Hello ${this.props.toWhat}`);
//   }
// }

// ReactDOM.render(
//   React.createElement(Hello, {toWhat: 'World'}, null),
//   document.getElementById('root')
// );


//JSX

class HelloWorld extends React.Component {
  render() {
      return (
          <h1>Hello, World!</h1>
      );
  }}
// export default HelloWorld;
ReactDOM.render(<HelloWorld />, document.getElementById("root"));





class Square extends React.Component {
    render() {
      return (
        <button className="square">
          {/* TODO */}
        </button>
      );
    }
  }
  
  class Board extends React.Component {
    renderSquare(i) {
      return <Square />;
    }
  
    render() {
      const status = 'Next player: X';
  
      return (
        <div>
          <div className="status">{status}</div>
          <div className="board-row">
            {this.renderSquare(0)}
            {this.renderSquare(1)}
            {this.renderSquare(2)}
          </div>
          <div className="board-row">
            {this.renderSquare(3)}
            {this.renderSquare(4)}
            {this.renderSquare(5)}
          </div>
          <div className="board-row">
            {this.renderSquare(6)}
            {this.renderSquare(7)}
            {this.renderSquare(8)}
          </div>
        </div>
      );
    }
  }
  
  class Game extends React.Component {
    render() {
      return (
        <div className="game">
          <div className="game-board">
            <Board />
          </div>
          <div className="game-info">
            <div>{/* status */}</div>
            <ol>{/* TODO */}</ol>
          </div>
        </div>
      );
    }
  }
  
  // ========================================
  
  ReactDOM.render(
    <Game />,
    document.getElementById('root')
  );
  



  // var useEffect = require('react').useEffect

  function App() {
    useEffect(() => {
      fetch('/users/1').then(response => response.json().then(data => 
        {console.log(data);
        })
      );
    }, []);
    
    return (
    <div className="App">
      </div>
      );
    }
    
    ReactDOM.render(
      <App />,
      document.getElementById('root')
    );
    