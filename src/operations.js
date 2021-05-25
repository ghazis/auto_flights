export const getFlights = (startDate, endDate, duration, srcAirport, destAirport) => {
	const url = `http://localhost:3000/?start_date=${startDate}&end_date=${endDate}&duration=${duration}&src_airport=${srcAirport}&dest_airport=${destAirport}`
	return fetch(url)
	  .then(response => response.json())
	  .then(data => {
	   return data
	});
}

export const getDepartures = (flights) => {
	const departures = [];

	flights.map(flight => {
		departures.push(flight.departure);
	})

	return departures
}