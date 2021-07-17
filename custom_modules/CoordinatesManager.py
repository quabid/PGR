import pickle
from .FileValidator import fileExists, isFile
from .StatusMessenger import error, success, warning


def save_location(grid_location):
    location_file = open('coordinates', 'wb')
    pickle.dump(grid_location, location_file)
    location_file.close()


def get_location():
    if fileExists('coordinates'):
        message = success("Woo Hoo!")
        print("\n\t\t{}\\n\n".format(message))
        location_file = open('coordinates','rb')
        location_coordinates = pickle.load(location_file)
        return location_coordinates
    else:
        message = error("Doh!")
        print("\n\t\t{}\n\n".format(message))
        return None
