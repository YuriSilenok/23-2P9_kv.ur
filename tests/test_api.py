"""Проверка API на квадратное уравнение"""
import unittest
import requests


class TestsAPI(unittest.TestCase):
    """Проверка API на квадратное уравнение"""
    def test_linear_equation(self):
        """Проверка API на квадратное уравнение"""
        a = 0
        b = 2
        c = -4
        x = 2
        string = "Уравнение линейное, один корень"
        count = 2
        url = "http://127.0.0.1:8000/kvur"
        result = requests.get(url+f"?a={a}&b={b}&c={c}", timeout = 1111).json()
        self.assertEqual(len(result), count,
                         "incorrect count of values (linear equation)")
        self.assertEqual(result[0], string,
                         "incorrect string (linear equation)")
        self.assertEqual(result[1], x,
                         "incorrect x (linear equation)")
