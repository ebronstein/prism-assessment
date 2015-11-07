import sys
import argparse
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

def get_distances(cities, format):
	locator = Nominatim()
	geolocations = [locator.geocode(city) for city in cities]
	distances = []
	for i in range(len(cities)-1):
		if format == "kilometers":
			distances.append(vincenty(get_coordinates(geolocations[i]), get_coordinates(geolocations[i+1])).kilometers)
		else:			
			distances.append(vincenty(get_coordinates(geolocations[i]), get_coordinates(geolocations[i+1])).miles)
	return distances

def print_itinerary(cities, distances, format):
	print("Success! Your vacation itinerary is:\n")
	for i in range(len(distances)):
		print("\t{0} -> {1}: {2} {3}".format(cities[i], cities[i+1], round(distances[i], 2), format))
	print("\nTotal distance covered in your trip: {0} {1}".format(round(sum(distances), 2), format))

def get_coordinates(geolocation):
	return (geolocation.latitude, geolocation.longitude)

def make_itinerary(format):
	cities = []
	for line in sys.stdin:
		cities.append(line.strip())
	distances = get_distances(cities, format)
	print_itinerary(cities, distances, format)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--miles", help="see the output in miles", action="store_true")
	parser.add_argument("-k", "--kilometers", help="see the output in kilometers", action="store_true")
	args = parser.parse_args()
	if args.kilometers:
	    make_itinerary("kilometers")
	else:
		make_itinerary("miles")