import React, { Component } from 'react';
import basketball from '../Pics/basketball.jpg'
import hdmi from '../Pics/hdmi.jpg'
import vga from '../Pics/vga.jpg'
import game from '../Pics/game.jpg'
import monitor from '../Pics/monitor.jpg'
import speaker from '../Pics/speaker.jpg'
import lightning from '../Pics/lightning.jpg'
import './DisplayItems.css'

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
    "src": basketball,
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
    "src": hdmi,
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
    "src": vga,
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
    "src": monitor,
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
    "src": speaker,
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
    "src": lightning,
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
    "src": game,
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
        <div key={items.id} className="image">
          <img src = {items.src} alt = {items.item_name} height="200px"></img>
          <span className="details">{items.item_name} currently cost ${items.price}</span>
        </div>)}
        {/*implement later {this.state.loading ? <div> loading...</div>:<div>item</div>}*/}
      </div>
      )
  }
}

export default DisplayItems;