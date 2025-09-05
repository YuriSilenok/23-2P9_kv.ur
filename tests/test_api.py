"""Module for all unittests api"""

import unittest
from fastapi import testclient
from api import app

HOST = 'localhost:8000'
URL = "/kvur/"

client = testclient.TestClient(app=app)


class TestsKvUrAPI(unittest.TestCase):
    """Class for unittests API"""

    def test_api_three_is_zero(self):
        """Прямая параллельна оси"""

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

    def test_api_all_is_zero(self):
        """Прямая совпадает с осью"""

        a_in = 0
        b_in = 0
        c_in = 0
        answer = "Уравнение линейное"
        string = "Всё множество значений Ох"
        output = client.get(
            f"http://{HOST}{URL}?a={a_in}&b={b_in}&c={c_in}"
            ).json()
        count = 2

        self.assertEqual(len(output), count, "Некорректное число элементов")
        self.assertEqual(output[0], string, "Строка некорреткна")
        self.assertEqual(output[1], answer, "Ответ некорректен")
