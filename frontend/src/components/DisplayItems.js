import React, { Component } from 'react';

class DisplayItems extends Component {

  state = {
    "for_sell":[
    {
    "id" : 1,       
    "item_name": "Basketball",
    "price": 30,
    "quantity":1,
    "status":"new",
    "instock": true,
    "Type" : [{
        "Sell": true,
        "rent": false
    }]
    }, 
    {
    "id" : 2,       
    "item_name": "HDMI Cable",
    "price": 5,
    "quantity":0,
    "status":"used",
    "instock": false,
    "Type" : [{
        "Sell": true,
        "rent": false
    }]
    }, 
    {
    "id" : 3,       
    "item_name": "VGA Cable",
    "price": 3,
    "quantity":0,
    "status":"new",
    "instock": false,
    "Type" : [{
        "Sell": true,
        "rent": false
    }]
    }, 
    {
    "id" : 4,       
    "item_name": "24 inch monitor",
    "price": 200,
    "quantity":1,
    "status":"new",
    "instock": true,
    "Type" : [{
        "Sell": true,
        "rent": false
    }]
    }, 
    {
    "id" : 5,       
    "item_name": "Speaker",
    "price": 50,
    "quantity":1,
    "status":"used",
    "instock": true,
    "Type" : [{
        "Sell": true,
        "rent": false
    }]
    }, 
    {
    "id" : 6,       
    "item_name": "Lightning Cable",
    "price": 10,
    "quantity":1,
    "status":"new",
    "instock": true,
    "Type" : [{
        "Sell": true,
        "rent": false
    }]
    }, 
    {
    "id" : 7,       
    "item_name": "A game",
    "price": 60,
    "quantity":1,
    "status":"new",
    "instock": true,
    "Type" : [{
        "Sell": true,
        "rent": true
    }]
    }
    ]
}

  /*state = {
    loading: true
  }

  Will be implemented later async componentDidMount(){
    const url = "http://127.0.0.1:5000/items";
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }*/

  render() {
    return(
      <div className="App">
        {this.state.for_sell.map(items=> 
        <li>{items.item_name} cost {items.price} and there are {items.instock} </li>)}
        {/*implement later {this.state.loading ? <div> loading...</div>:<div>item</div>}*/}
      </div>
      )
  }
}

export default DisplayItems;