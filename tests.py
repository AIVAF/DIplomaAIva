import data
import request

# Анна Иванченко, 7-й  поток — Финальный проект. Инженер по тестированию плюс

def test_status_code():
    assert request.response.status_code == 200

