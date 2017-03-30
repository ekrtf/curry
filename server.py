import json
from flask import Flask, jsonify
from country_adapter import get_country_currencies

app = Flask(__name__)

@app.route('/country/<name>')
def country_currency(name):
	curr = get_country_currencies(name)
	return jsonify(curr)

if __name__ == '__main__':
	app.run()