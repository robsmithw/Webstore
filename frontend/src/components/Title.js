import React, { Component } from 'react';
import './Title.css'


class Title extends Component {
  render() {
    return (    //Header needs Home, buy,rent,return,sell and login in this order and a cart button
      <header>
        <ul>
            <a href ="/" className="HomePage"><b>Home</b></a>
            <a href ="index.html" className="LoginPage">Login</a>   {/*all hrefs set to index.html will need to be changed when other pages are done*/}
            <a href ="index.html" className="SellPage">Sell</a>
            <a href ="index.html" className="ReturnPage">Return</a>
            <a href ="index.html" className="RentPage">Rent</a>
            <a href ="index.html" className="BuyPage">Buy</a>
        </ul>
      </header>
    );
  }
}

export default Title;