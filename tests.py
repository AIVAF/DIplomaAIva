import data
import request

# Анна Иванченко, 7-й  поток — Финальный проект. Инженер по тестированию плюс

# Функция проверки успешного создания заказа
def positive_assert_new_order(body):
    response = request.post_new_order(body)
    
    assert response.status_code == 201

# Проверяем успешность создания заказа с телом из файла data
def test_success_response():
    positive_assert_new_order(data.order_body)

# Функция проверки кода ответа
def positive_assert_track_number(number):
    response_order = request.get_order_tracknumber(number)

    assert response_order.status_code == 200

# Вытаскиваем трек-номер при создании заказа и проверяем код ответа
def test_success_response_number():
    response_order = request.post_new_order(data.order_body)
    track_number = response_order.json()["track"]
    positive_assert_track_number(track_number)




