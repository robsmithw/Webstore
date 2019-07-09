import React, { Component } from 'react';
import './DisplayItems.css'

class DisplayItems extends Component {

  state = {
    loading: true,
    for_sell: []
  }

  async componentDidMount(){
    const url = "http://127.0.0.1:5000/items";
    fetch(url).then(response => response.json())
    .then(for_sell => this.setState({for_sell}));
    this.state.loading = false;
    console.log(this.state.for_sell);
  }

  render() {
    return(
      <div className="App">
        {this.state.loading ? <div> loading...</div>:<div>We Loaded</div>}
        {this.state.for_sell.map(item =>
        <div key={item.id} className="image">
          <img src = {item.src} alt = {item.item_name} height="200px"></img>
          <span className="details">{item.item_name} currently cost ${item.price}</span>
        </div>)}
      </div>
      )
  }
}

export default DisplayItems;