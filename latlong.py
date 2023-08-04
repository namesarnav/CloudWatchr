
import requests

def get_location_metadata(location):

	'''
	This function gives the complete metadata of a location by the name of a location
	output must be retreived through indexing of whatever object is created
	'''

	base_url = "https://nominatim.openstreetmap.org/search"
	params = {
		'q' : location,
		'format' : 'json',
		"addressdetails": 1,  # Include detailed address information
	}
	
	response = requests.get(base_url,params=params).json() #gives the whole output 
	return response[0]









