const cors = require('cors')
const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

app.use(cors());
app.get('/', (req, res) => {
	params = req.query;
	start_date = params.start_date;
	end_date = params.end_date;
	duration = params.duration;
	src_airport = params.src_airport;
	dest_airport = params.dest_airport;

	var flight_data = [];

	// spawn new child process to call the python script
	const python = spawn('/Users/ashhadghazi/react/auto_flights/backend/flight_scraper/auto_flights.py',
						[start_date, end_date, duration, src_airport, dest_airport]);

	// collect data
	python.stdout.on('data', function (data) {
		flight_data.push(data);
	});

	python.stderr.on('data', function (data) {
		flight_data.push(data);
		console.log(flight_data.join(""));
	});

	python.on('close', (code) => {
		// send data to browser
		res.send(flight_data.join(""))
	});
 
})

app.listen(port, () => console.log(`Listening on port ${port}...`))