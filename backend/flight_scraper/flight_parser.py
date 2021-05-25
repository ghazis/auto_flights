from __init__ import USE_FF
from __init__ import c_index_map, ff_index_map


def create_flight_map(flight_type, flight):
    flight_map = {'type': flight_type}
    index_map = ff_index_map if USE_FF else c_index_map

    for attr in index_map:
        index = index_map[attr][flight_type]
        flight_map[attr] = flight[index].split(' – ')[1] if attr == 'arrival_time' and USE_FF\
            else flight[index]

    return flight_map


def get_flight_type(flight):
    flight_type = 'has_stops'
    separate_index = 2 if USE_FF else 3
    nonstop_index = 6 if USE_FF else 7
    if 'Separate' in flight[separate_index]:
        flight_type = 'has_separate'
    elif 'Nonstop' in flight[nonstop_index]:
        flight_type = 'nonstop'

    return flight_type


def get_parsed_flights(flights):
    all_flights = []

    for flight in flights:
        parsed_flight = {}
        return_flights = []
        return_info_chunks_list = []
        departure_flight_raw = flight['departure']
        return_flights_raw = flight['return_flights']
        depart_info_chunks = departure_flight_raw.split('\n')
        for return_flight in return_flights_raw:
            return_info_chunks_list.append(return_flight.split('\n'))

        flight_type = get_flight_type(depart_info_chunks)
        flight_map = create_flight_map(flight_type, depart_info_chunks)
        parsed_flight['departure'] = flight_map

        for return_info_chunks in return_info_chunks_list:
            flight_type = get_flight_type(return_info_chunks)
            flight_map = create_flight_map(flight_type, return_info_chunks)
            return_flights.append(flight_map)

        parsed_flight['returns'] = return_flights
        all_flights.append(parsed_flight)

    return all_flights
