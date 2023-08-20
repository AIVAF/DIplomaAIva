import data
import configuration
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

response = post_new_order(data.order_body)
#print(response.status_code) раздокументировать, чтобы проверить результат промежуточного шага
track_number = response.json()["track"]
#print(response.json()["track"]) раздокументировать, чтобы проверить результат промежуточного шага


def get_order_tracknumber(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + '?t=' + str(track_number))

response = get_order_tracknumber(track_number)
#print(response.status_code) раздокументировать, чтобы проверить результат промежуточного шага
#print(track_number) раздокументировать, чтобы проверить результат промежуточного шага

