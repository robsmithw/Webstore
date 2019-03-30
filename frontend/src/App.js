import React, { Component } from 'react';
import Title from './components/Title';
import DisplayItems from './components/DisplayItems';
import './App.css';

class App extends Component {
  constructor(){
    super();
    this.state = {
      items: [],
      loaded: false,
    }
  }

  /*componentDidMount(){
    fetch('http://localhost:5000/items')
    .then( results => {return results.json();
    }).then(data =>{
      let items = data.results.map((item) => {
        return(
          <div key={item.id}>{item.name}</div>
        )
      })
      this.setState({
        items: items,
        loaded: true,
      });
    })
  }*/

  render() {
  var {items,loaded} = this.state;
    return (
      <div className="App">
        <Title />
        <ul>
          cost
          {items.map(item => (
            <li key={item.id}>
              {item.name} cost {item.price}
            </li>
          ))};
        </ul>
        <DisplayItems />
      </div>
    );
  }
}

export default App;
