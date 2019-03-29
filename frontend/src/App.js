import React, { Component } from 'react';
import Title from './components/Title';
import AllNews from './components/AllNews';
import './App.css';

class App extends Component {
  state = {
    items:[
      {
        id: 1,
        name: 'Ball',
        status: 'New',
        price: 12.00 //Price is in dollars
      },
      {
        id: 2,
        name: 'Cord',
        status: 'Used',
        price: 3.00
      },
      {
        id: 3,
        name: 'Site',
        status: 'New',
        price: 100.00
      }
    ]
  }
  render() {
    return (
      <div className="App">
        <Title />
        <AllNews items={this.state.items} />
      </div>
    );
  }
}

export default App;
