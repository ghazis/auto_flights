import React, { useEffect, useState } from 'react';
import { connect } from "react-redux";
import moment from 'moment';
import Tabs from './Tabs';
import Select from './Select';
import Flights from './Flights';
import Datepicker from './Datepicker';
import { getFlights } from './operations';

const App = ({ flights, setFlights }) => {
  const possibleDurations = [3,4,5,6,7,8,9,10,11,12,13,14,30];
  const possibleSrc = ['ORD'];
  const possibleDest = ['LHR'];

  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();
  const [duration, setDuration] = useState(3);
  const [srcAirport, setSrcAirport] = useState('ORD');
  const [destAirport, setDestAirport] = useState('LHR');

  const [scanDisabled, setScanDisabled] = useState(false);
  const [activeTab, setActiveTab] = useState(0);
  const [tabLabels, setTabLabels] = useState([]);
  const [selectedFlight, setSelectedFlight] = useState([]);

  const handleDateChange = (type, date) => {
    const formattedDate = moment(date).format('YYYY-MM-DD');
    if (type == 'start') setStartDate(formattedDate);
    else setEndDate(formattedDate);
  }

  const handleScan = async () => {
  	setScanDisabled(true);
  	const flights = await getFlights(startDate, endDate, duration, srcAirport, destAirport);
  	setScanDisabled(false);
  	setFlights(flights);
  	setTabLabels(flights.map(flight=>flight.depart_date));
  	setSelectedFlight(flights[0].flights);
  }

  const handleTabClick = (event, i) => {
  	setActiveTab(i);
  	setSelectedFlight(flights[i].flights);
  }

  const handleSrcChange = (event) => {
  	setSrcAirport(event.currentTarget.value);
  }

  const handleDestChange = (event) => {
  	setDestAirport(event.currentTarget.value);
  }

  const handleDurationChange = (event) => {
  	setDuration(event.currentTarget.value);
  }

  return (
    <div className='app-container'>
    	<div className="flex top-controls">
    		<Datepicker id="start" label="Start Date" className="date-picker" dateChangeFn={handleDateChange} />
    		<Datepicker id="end" label="End Date" className="date-picker" dateChangeFn={handleDateChange} />
    		<Select className="select selectAirport" label="Source" data={possibleSrc} onChange={handleSrcChange} />
    		<Select className="select selectAirport" label="Destination" data={possibleDest} onChange={handleDestChange} />
    		<Select className="select selectDur" label="Duration" data={possibleDurations} onChange={handleDurationChange} />
    		<button
    			type="button"
    			className="btn btn-outline-secondary button"
    			onClick={handleScan}
    			disabled={scanDisabled}>
    			{
    				!scanDisabled ?
    				"Scan" : <img src={require('./images/spinner.gif')} width="36" height="24" />
    			}
    		</button>
    	</div>

    	<Tabs
    		className="tabs"
    		activeTab={activeTab}
    		onClick={handleTabClick}
    		data={tabLabels}
    	/>

    	{ selectedFlight.length &&
    		<div>
		    	<Flights flights={selectedFlight} />
		    </div>
    	}
    </div>

  )
}

const mapStateToProps = (state) => {
  return {
  	flights: state.flights
  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    setFlights: (flights) => dispatch({ type: 'SET_FLIGHTS', flights:flights })
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);
