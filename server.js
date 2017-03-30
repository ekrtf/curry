'use strict';

const express = require('express');
const path = require('path');
const rp = require('request-promise');

const PORT = 5000;

const server = express();

server.use(express.static(path.join(__dirname, 'public')));

server.get('/codes', function(req, res) {
	rp({
		url: 'http://localhost:5001/currency/codes'
	}).then(function(r) {
		res.send(r);
	});
});

server.listen(PORT, () => {
	console.log('Frontend server running on port ' + PORT)
});
