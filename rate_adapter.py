import requests

key = "8ee81402f0f1373c35aac807d814325d"

def get_rate(source, dest):
	payload = {
		'access_key': key,
		'source': source,
		'currencies': dest
	}
	res = requests.get('http://apilayer.net/api/live', params=payload).json()
	return next(res['quotes'].itervalues())
