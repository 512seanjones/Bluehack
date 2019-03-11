from gmplot import gmplot
import googlemaps
from pymongo import MongoClient

gmaps = googlemaps.Client(key='')
def client():
    """
    Connects to the mongoDB client
    """
    client = MongoClient('localhost',27017)
    return client.bluehack

db = client()
location_db = db.locations

def insert_location(street, city, state):
    """
    Inserts a street, city, and state into our database i.e. '530 Hudson Street, Hoboken, New Jersey'
    """
    db.locations.insert_one({"state": state, "city": city, "street":street})

def get_all_lngs_and_lats(state, city):
    """
    This function finds the longitudes and latitudes of all marked spots in an area by searching for any spots in the same city and state.
    It searches our database for matching results and then obtain's their longitutdes and latitudes in using geocode and gmaps.
    Params:
        state: A string representing the state we are searching in
        city: A string representing the city we are searching in
    Returns:
        lats: a list of ints representing latitutdes
        lngs: a list of ints representing longitudes
    """
    lngs = []
    lats = []
    for location in db.locations.find({"state":state,"city": city}):
        geocode_result = gmaps.geocode(location['street']+',' + location['city']+ ',' +location['state'])
        latitude = geocode_result[0]["geometry"]["location"]['lat']
        longitude = geocode_result[0]["geometry"]["location"]['lng']
        lngs.append(longitude)
        lats.append(latitude)
    return lats, lngs

def insert_and_show_map(street,city,state):
    geocode_result = gmaps.geocode(street+',' + city+ ',' +state)#get geocode for desired address including longitudes and latitudes
    latitude = geocode_result[0]["geometry"]["location"]['lat']
    longitude = geocode_result[0]["geometry"]["location"]['lng']

    gmap = gmplot.GoogleMapPlotter(latitude, longitude, 13)#set the location and size of the google map
    insert_location(street,city,state)
    lats, lngs = get_all_lngs_and_lats(state,city)
    gmap.heatmap(lats, lngs)
    gmap.draw("templates/my_map.html")

def just_show_map(street,city,state):
    geocode_result = gmaps.geocode(street+',' + city+ ',' +state)#get geocode for desired address including longitudes and latitudes
    latitude = geocode_result[0]["geometry"]["location"]['lat']
    longitude = geocode_result[0]["geometry"]["location"]['lng']

    gmap = gmplot.GoogleMapPlotter(latitude, longitude, 13)#set the location and size of the google map
    lats, lngs = get_all_lngs_and_lats(state,city)
    gmap.heatmap(lats, lngs)
    gmap.draw("templates/my_map.html")

if __name__ == '__main__':
    insert_and_show_map("530 Hudson Street", "Hoboken", "New Jersey")
