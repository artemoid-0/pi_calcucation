import random
import time

import mpmath


def pi_Monte_Carlo_ST(num_experiments):
    print("Calculating with Monte Carlo method in single threaded mode")

    inside_circle = mpmath.mpf(0)
    total_points = mpmath.mpf(0)

    start_time = time.time()

    for _ in range(num_experiments):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

        total_points += 1

    pi_estimate = (inside_circle / total_points) * 4
    end_time = time.time()

    return (pi_estimate, end_time - start_time,
            {"algorithm": "Monte Carlo method",
             "mode": "single-threaded"})


if __name__ == '__main__':
    # Пример использования функции
    num_experiments = 1000000
    pi_estimate, execution_time = pi_monte_carlo(num_experiments)
    print(f"Вычисленное значение π: {pi_estimate}")
    print(f"Время выполнения: {execution_time} секунд")
