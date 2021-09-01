"""
1) Use given 8 addresses from input.json
2) Convert addresses into geo-locations
3) Calculate each geo-location's distance from Adchieve HQ
4) Sort the distance
5) Output in csv
"""
import argparse
import haversine as hs
import http.client
import json
import pandas as pd
import urllib.parse

from dotenv import dotenv_values
from json import JSONDecodeError

config = dotenv_values(".env")


def get_all_geolocations(addresses):
    """
    This function will generate list of all
    geolocations- latitude and longitude. It
    will try to fetch again if there is any internal error.

    param json addresses: Addresses whose geolocations needs to be generated
    return: List of Geolocation details with latitude, longitude and status
    rtype: json
    """
    geolocations = []
    for address in addresses:
        geolocation = get_geolocation(address)
        if geolocation['status']:
            geolocations.append(geolocation)
        else:
            internal_error = geolocation.get('error_data', None)
            if internal_error:
                geolocation = get_geolocation(address)
                if geolocation['status']:
                    geolocations.append(geolocation)

    return geolocations


def get_geolocation(address):
    """
    This function will generate geolocation (latitude & longitude)
    of single address

    param dict address: Single Address whose geolocations
                        needs to be generated
    return: Geolocation detail of single address with
            latitude, longitude and status
    rtype: dict
    """
    conn = http.client.HTTPConnection('api.positionstack.com')
    params = urllib.parse.urlencode({
        'access_key': config.get('SECRET_KEY'),
        'query': address.get('address'),
        'limit': 1,
    })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    response_data = json.loads(data)
    error = response_data.get('error', None)
    if error is None:
        if response_data.get('data') and address.get('name'):
            geolocation = {'Name': address.get('name'),
                           'latitude': response_data['data'][0]['latitude'],
                           'longitude': response_data['data'][0]['longitude'],
                           'Address': address.get('address'),
                           'status': True}

            return geolocation
        else:
            return {'status': False,
                    'message': "Address/Name not found"}
    else:
        return {'status': False,
                'message': "Could not get geolocation",
                'error_data': error}


def calculate_distance(geolocations):
    """
    This function will calculate distance between
    Adchieve HQ and other address

    param json geolocations: Geolocations whose address
                            distance needs to be calculated
    return: Distance detail of all addresses
    rtype: dict
    """
    for geolocation in geolocations:
        if geolocation.get('status'):
            adchieve_address = get_headquarter_address()
            adchieve_location = (adchieve_address.get('latitude'),
                                 adchieve_address.get('longitude'))
            user_location = (geolocation.get('latitude'),
                             geolocation.get('longitude'))
            distance = hs.haversine(adchieve_location, user_location)
            distance = round(distance, 2)
            geolocation['Distance'] = distance
            del geolocation['latitude'], geolocation['longitude'], \
                geolocation['status']

    return geolocations


def create_csv(geo_data):
    """
    This function will create and store data in CSV file & sort them

    param json geolocations: Geolocations whose address
                            distance needs to be calculated
    """
    distance_df = pd.DataFrame(geo_data,
                               columns=['Distance', 'Name', 'Address'])
    sorted_df = distance_df.sort_values(by=["Distance"],
                                        ascending=True)
    sorted_df['Distance'] = sorted_df['Distance'].astype(str) + ' km'
    sorted_df.reset_index(drop=True, inplace=True)
    sorted_df.index.names = ['Sortnumber']
    sorted_df.to_csv('distances.csv')
    return sorted_df


def get_headquarter_address():
    """
    This function will get geolocation of Adchieve HQ

    return: Geolocation of HQ
    rtype: dict
    """
    return get_geolocation({
        "name": "Adchieve HQ",
        "address":
            "Sint Janssingel 92, 5211 DA 's-Hertogenbosch, The Netherlands"
    })


def get_distances(addresses):
    """
    This function will call all functions- get all
    geolocation, calculate distance and create CSV.

    param json addressed: Addresses received in POST method
    """
    if addresses:
        geolocations = get_all_geolocations(addresses)
        distance = calculate_distance(geolocations)
        distances = create_csv(distance)
        print("Distance of Addresses from Adchieve HQ:\n")
        print(distances)
        return distances
    else:
        print("Data is empty")


parser = argparse.ArgumentParser()
parser.add_argument('--infile', nargs=1,
                    help="JSON file to be processed",
                    type=argparse.FileType('r'))
arguments = parser.parse_args()
try:
    address_data = json.load(arguments.infile[0])
    dataframe = get_distances(address_data)
except JSONDecodeError:
    print("Data is not in json format")
