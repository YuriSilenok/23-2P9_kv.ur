"""Проверка API на квадратное уравнение"""
import unittest
import requests
from fastapi import testclient
from api import app


class TestsAPI(unittest.TestCase):
    """Проверка API на квадратное уравнение"""
    def test_linear_equation(self):
        """Проверка API на квадратное уравнение"""
        a = 0
        b = 3
        c = 6
        x = 2
        string = "Уравнение линейное, один корень"
        count = 2
        url = "http://127.0.0.1:8000/kvur"
        result = requests.get(url+f"?a={a}&b={b}&c={c}", timeout=1111).json()
        self.assertEqual(len(result), count,
                         "incorrect count of values (linear equation)")
        self.assertEqual(result[0], string,
                         "incorrect string (linear equation)")
        self.assertEqual(result[1], x,
                         "incorrect x (linear equation)")

    def test_api_three_is_zero(self):
        """Прямая параллельна оси"""
        HOST = 'localhost:8000'
        URL = "/kvur/"
        client = testclient.TestClient(app=app)

        a_in = 0
        b_in = 0
        c_in = 4
        answer = "Нет решения"
        string = "Линейное уравнение параллельное оси Ох"
        output = client.get(
            f"http://{HOST}{URL}?a={a_in}&b={b_in}&c={c_in}"
            ).json()
        count = 2

        self.assertEqual(len(output), count, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорреткна")
        self.assertEqual(output[1], answer, "Ответ некорректен")
