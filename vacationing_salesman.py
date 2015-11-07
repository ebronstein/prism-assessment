import sys
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

def get_distances(cities):
	locator = Nominatim()
	geolocations = [locator.geocode(city) for city in cities]
	distances = []
	for i in range(len(cities)-1):
		distances.append(vincenty(get_coordinates(geolocations[i]), get_coordinates(geolocations[i+1])).miles)
	print_itinerary(cities, distances)

def print_itinerary(cities, distances):
	print("Success! Your vacation itinerary is:\n")
	for i in range(len(distances)):
		print("\t{0} -> {1}: {2} miles".format(cities[i], cities[i+1], round(distances[i], 2)))
	print("\nTotal distance covered in your trip: {0} miles".format(round(sum(distances), 2)))

def get_coordinates(geolocation):
	return (geolocation.latitude, geolocation.longitude)

cities = []
for line in sys.stdin:
	cities.append(line.strip())
get_distances(cities)