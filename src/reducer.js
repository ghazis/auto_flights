const initialAppState = {
  flights: []
};

const reducer = (state = initialAppState, action) => {
  switch (action.type) {
    case 'SET_FLIGHTS':
      return {
        ...state,
        flights: action.flights
      }
    default:
      return state;
  }
};

export default reducer;