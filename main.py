"""Решение квадратного уравнения"""

coef1 = float(input("Введите коэффициент а:"))

coef2 = float(input("Введите коэффициент b:"))

coef3 = float(input("Введите коэффициент c:"))


def solve_root(a, b, c):

    """Решение квадратного уравнения"""
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:

        x1 = (-b + discriminant**0.5) / 2 * a
        x2 = (-b - discriminant**0.5) / 2 * a
        return f"Корни:{x1}, {x2}"
    elif discriminant == 0:

        x = (-b) / 2*a

        return f"Корень: {x}"
    else:

        return "Нет корней"


print(solve_root(coef1, coef2, coef3))
