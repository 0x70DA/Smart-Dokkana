import requests


def send_request(params):
    """ Send a GET request to the server. """
    url = "http://192.168.1.157:5000/_face_id"
    r = requests.get(url=url, params=params)
