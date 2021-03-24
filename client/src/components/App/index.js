import './index.css';
import Map from '../Map/index.js'
import Selecter from '../Selecter/index.js'
import Infodisplayer from '../Info_displayer/index.js'
import React from 'react';

function App(){
  
   const [stations, set_stations] = React.useState([]);



  return (
    <div className='mainApp'>
      <div className='left'>  
        <Selecter className='selecter' stations={stations} set_stations={set_stations} />
        <Infodisplayer className='info_displayer' stations={stations}/>
      </div>
      <div className='right'>
        <Map className='map'/>
      </div>
      
    </div>
  );
}

export default App;
