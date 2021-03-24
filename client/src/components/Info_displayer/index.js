import './index.css';
import React from 'react';
import Station from '../Station/index.js'
function Infodisplayer({stations}) {
 
  return (
    <div className='mainDisplayer'>
      {stations.map((x,i)=>( <Station key={i} x={x}/>))}
      
    </div>
  );
}

export default Infodisplayer;
