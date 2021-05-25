import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import thunk from "redux-thunk";
import { Provider } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import reducer from './reducer';
import App from './App';
import './index.scss';

const store = createStore(reducer, applyMiddleware(thunk));

ReactDOM.render(
	<Provider store={store}>
		<App />
	</Provider>,
	document.getElementById('app')
);