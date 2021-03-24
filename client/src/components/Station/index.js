import './index.css';
import React from 'react';

function Station({x}) {
 
  return (
    <div className='mainStation'>
        <h2>{x.Name}</h2>
        <p>Lat: {x.Lat} | Long: {x.Long}</p>
        <p>Available bikes: {x.AvailableBikes} | Available places: {x.AvailableBikesStands}</p>
    </div>
  );
}

export default Station;
