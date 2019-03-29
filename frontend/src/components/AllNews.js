import React, { Component } from 'react';


class AllNews extends Component {
  render() {
    return this.props.items.map((item) => (
        <li>{item.name} cost ${item.price}</li>
    ));
  }
}

export default AllNews;