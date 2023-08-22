import data
import configuration
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)


def get_order_tracknumber(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + '?t=' + str(track_number))



