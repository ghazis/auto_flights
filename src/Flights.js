import React, { useEffect, useState } from 'react';
import Table from './Table';
import { getDepartures } from './operations';

const Flights = ({ flights }) => {
  const [departures, setDepartures] = useState();
  const [returns, setReturns] = useState();

  const getReturns = (i, init=false) => {
    const returns = flights[i].returns;
    if (!init) setReturns(returns);
    else return returns;
  }

  useEffect(() => {
    const departures = getDepartures(flights);
    const returns = getReturns(0, true);
    setDepartures(departures);
    setReturns(returns);
  }, [flights])

  return (
    <div>
      { departures && returns &&
        <div>
          <h2>Departing Flights</h2>
          <Table data={departures} onClick={getReturns} />

          <h2>Return Flights</h2>
          <Table data={returns} />
        </div>
      }
    </div>
  );
}

export default Flights;