import requests

key = "YOUR-KEY"

def get_rate(source, dest):
	payload = {
		'access_key': key,
		'source': source,
		'currencies': dest
	}
	res = requests.get('http://apilayer.net/api/live', params=payload).json()
	return next(res['quotes'].itervalues())
