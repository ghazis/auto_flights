#!/Users/ashhadghazi/react/auto_flights/backend/flight_scraper/venv/bin/python

import sys, json, base64, argparse
from datetime import datetime, timedelta
from AutoWeb import AutoWeb
from flight_parser import get_parsed_flights
from __init__ import USE_FF


def get_url(src_airport, dest_airport, depart_date, return_date):
    bytes = b'\x08\x1c\x10\x02\x1a\x1ej\x07\x08\x01\x12\x03%b\x12\n%br\x07\x08\x01\x12\x03%b\x1a\x1ej\x07\x08' \
            b'\x01\x12\x03%b\x12\n%br\x07\x08\x01\x12\x03%bp\x01\x82\x01\x0b\x08\xfc\x05\x00\x05 \x06`\x04\x04' \
            % (src_airport, depart_date, dest_airport, dest_airport, return_date, src_airport)
    url_add = base64.b64encode(bytes).decode("utf-8")
    url = f"https://www.google.com/travel/flights/search?tfs={url_add}"

    return url

def get_session(src_airport, dest_airport, depart_date, return_date):
    url = get_url(src_airport, dest_airport, depart_date, return_date)
    session = AutoWeb(url, headless=USE_FF, ff=USE_FF)
    session.start_session()

    return session


def get_flight_data(session):
    flight_data = []
    elems = session.get_elements('xpath', "//div[contains(@aria-label, 'Select flight')]")
    for elem in range(0, len(elems)):
        flight = {}
        return_flights = []
        elem = elems[elem]
        if elem.text:
            flight['departure'] = elem.text
            elem.click()
            session.get_element('xpath', "//*[contains(text(), 'eturning flights')]")
            elems = session.get_elements('xpath', "//div[contains(@aria-label, 'Select flight')]")
        for elem in elems:
            if elem.text:
                return_flights.append(elem.text)
        flight['return_flights'] = return_flights
        flight_data.append(flight)
        session.go_back()
        session.get_element('xpath', "//*[contains(text(), 'departing flights')]")
        elems = session.get_elements('xpath', "//div[contains(@aria-label, 'Select flight')]")

    return flight_data


def get_all_flights(src_airport, dest_airport, depart_date, return_date):
    session = get_session(src_airport, dest_airport, depart_date, return_date)
    flight_data = get_flight_data(session)
    parsed_flights = get_parsed_flights(flight_data)

    session.stop_session()
    return parsed_flights


def generate_flights_maps(src_airport, dest_airport, depart_date, return_date, duration):
    flight_maps = []
    start_date = datetime.strptime(depart_date, '%Y-%m-%d')
    end_date = datetime.strptime(return_date, '%Y-%m-%d')
    days = (end_date - start_date).days
    for iter in range(0, days-(duration-1)):
        flight_map = {}
        depart = start_date + timedelta(days=iter)
        ret = depart + timedelta(days=duration)
        depart_string = datetime.strftime(depart, '%Y-%m-%d')
        ret_string = datetime.strftime(ret, '%Y-%m-%d')

        flights = get_all_flights(src_airport, dest_airport, bytes(depart_string, 'utf-8'), bytes(ret_string, 'utf-8'))
        flight_map['depart_date'] = depart_string
        flight_map['return_date'] = ret_string
        flight_map['flights'] = flights

        flight_maps.append(flight_map)

    return flight_maps


def main():
    description = 'Flight Scanning Utility'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('scan_info', type=str, nargs='*',
                    help='startdate, enddate, duration, src airport code, dest airport code')

    if len(sys.argv) != 6:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    depart_date = args.scan_info[0]
    return_date = args.scan_info[1]
    duration = int(args.scan_info[2])
    src_airport = bytes(args.scan_info[3], 'utf-8')
    dest_airport = bytes(args.scan_info[4], 'utf-8')

    flight_maps = generate_flights_maps(src_airport, dest_airport, depart_date, return_date, duration)
    print(json.dumps(flight_maps))

if __name__ == '__main__':
    main()
