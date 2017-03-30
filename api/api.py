import json
from flask import Flask, jsonify
from country_adapter import get_country_currencies, get_currency_countries, get_all_currency_codes
from rate_adapter import get_rate

app = Flask(__name__)

@app.route('/country/<name>')
def country_to_currency(name):
	currencies = get_country_currencies(name)
	return jsonify(currencies)

@app.route('/currency/codes')
def all_codes():
	currencies = get_all_currency_codes()
	return jsonify(currencies)

@app.route('/currency/<currency_code>')
def currency_to_country(currency_code):
	countries = get_currency_countries(currency_code)
	response = {
		'currency_code': currency_code,
		'countries': countries
	}
	return jsonify(response)

@app.route('/convert/<source>/<dest>/<amount>')
def convert(source, dest, amount):
	rate = get_rate(source, dest)
	result = float(amount) * float(rate)
	response = {
		'source': source,
		'dest': dest,
		'rate': rate,
		'result': result
	}
	return jsonify(response)

if __name__ == '__main__':
	app.run(port=5001)