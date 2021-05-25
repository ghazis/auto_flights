USE_FF = True

ff_index_map = {
    'departure_time': {
        'nonstop': 0,
        'has_stops': 0,
        'has_separate': 0
    },
    'arrival_time': {
        'nonstop': 1,
        'has_stops': 1,
        'has_separate': 1
    },
    'airline': {
        'nonstop': 2,
        'has_stops': 2,
        'has_separate': 3
    },
    'duration': {
        'nonstop': 3,
        'has_stops': 3,
        'has_separate': 4
    },
    'stops': {
        'nonstop': 6,
        'has_stops': 6,
        'has_separate': 7
    },
    'stop_duration': {
        'nonstop': -3,
        'has_stops': -3,
        'has_separate': -3
    },
    'cost': {
        'nonstop': -2,
        'has_stops': -2,
        'has_separate': -2
    }
}

c_index_map = {
    'departure_time': {
        'nonstop': 0,
        'has_stops': 0,
        'has_separate': 0
    },
    'arrival_time': {
        'nonstop': 2,
        'has_stops': 2,
        'has_separate': 2
    },
    'airline': {
        'nonstop': 3,
        'has_stops': 3,
        'has_separate': 4
    },
    'duration': {
        'nonstop': 4,
        'has_stops': 4,
        'has_separate': 5
    },
    'stops': {
        'nonstop': 7,
        'has_stops': 7,
        'has_separate': 8
    },
    'stop_duration': {
        'nonstop': -3,
        'has_stops': -3,
        'has_separate': -3
    },
    'cost': {
        'nonstop': -2,
        'has_stops': -2,
        'has_separate': -2
    }
}
