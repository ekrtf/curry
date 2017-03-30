import json
from flask import Flask, jsonify
from country_adapter import get_country_currencies, get_currency_country
from rate_adapter import get_rate

app = Flask(__name__)

@app.route('/country/<name>')
def country_to_currency(name):
	currencies = get_country_currencies(name)
	return jsonify(currencies)

@app.route('/currency/<country>')
def currency_to_country(country):
	countries = get_currency_country(country)
	return jsonify(countries)

@app.route('/convert/<source>/<dest>/<amount>')
def convert(source, dest, amount):
	rate = get_rate(source, dest)
	result = float(amount) * float(rate)
	return jsonify(result)

if __name__ == '__main__':
	app.run()