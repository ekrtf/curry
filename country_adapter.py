import requests

def get_all_countries():
	res = requests.get("https://restcountries.eu/rest/v2/all")
	return res.json()

def get_all_currency_codes():
	"""
	This function returns a list of tuples (country_name, currency_code[])
	"""
	codes = []
	countries = get_all_countries()
	for country in countries:
		currs = [ currency["code"] for currency in country["currencies"]]
		codes.append((country["name"], currs))
	return codes

def get_country_currency(name):
	res = requests.get("https://restcountries.eu/rest/v2/name/{}".format(name))
	res.content.decode('utf-8')
	country = res.json()[0]
	return country["currencies"]


