import './index.css';
import Map from '../Map/index.js'
import Selecter from '../Selecter/index.js'
import Infodisplayer from '../Info_displayer/index.js'
import React from 'react';
import {withGoogleMap,withScriptjs} from "react-google-maps";


const MapWrapped = withScriptjs(withGoogleMap(Map));

function App(){
  
   const [stations, set_stations] = React.useState([]);
   const [center, set_center] = React.useState({lat:48.87397217237368, lng:2.348388757504776});

  return (
    <div className='mainApp'>
      <div className='left'>  
        <Selecter className='selecter' stations={stations} set_stations={set_stations} set_center={set_center} />
        <Infodisplayer className='info_displayer' stations={stations}/>
      </div>
      <div className='right'>

      <MapWrapped
        googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=${process.env.REACT_APP_GOOGLE_KEY}`}
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={<div style={{ height: `100%` }} />}
        mapElement={<div style={{ height: `100%` }} />}
        stations={stations}
        center={center}
      />
      </div>
      
    </div>
  );
}

export default App;
