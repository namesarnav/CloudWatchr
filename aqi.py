import requests

token = '7c7329fda8525ce7ff3c39efd958eab2091e9cef'

def get_aqi_data(location):

	data = requests.get(f'https://api.waqi.info/feed/{location}/?token={token}').json()
	return data

def get_aqi(location):
	aqi = get_aqi_data(location=location)
	return aqi['data']['aqi']
