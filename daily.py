from latlong import get_location_metadata
import requests

token = 'fcbce1667338efc93136ba2b43c558c9' #Put your API key here

'''
Comments are test codes for when you have to access the JSON Output
'''
# loc = 'delhi'
# lat = get_location_metadata(loc)['lat']
# lon = get_location_metadata(loc)['lon']

def get_weather_data(lat,lon):
	'''
	This function uses the `get_location_metadata` function to retrieve the lattitude and longitude
	which is then parsed into params to get the final output
	'''
	base_url = 'https://api.openweathermap.org/data/2.5/weather?'
	params = {
		'lat'   : lat,
		'lon'   : lon,
		'appid' : token,
		'units' : 'metric',
	}

	weather_response = requests.get(base_url,params).json()
	return weather_response

# print(get_weather_data(lat,lon))

