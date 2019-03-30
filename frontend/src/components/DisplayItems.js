import React, { Component } from 'react';


class DisplayItems extends Component {

  
  state = {
    loading: true
  }

  async componentDidMount(){
    const url = "http://127.0.0.1:5000/items";
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  render() {
    return(
      <div className="App">
        {this.state.loading ? <div> loading...</div>:<div>item</div>}
      </div>
      )
  }
}

export default DisplayItems;