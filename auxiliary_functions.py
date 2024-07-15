import decimal

import mpmath
from decimal import Decimal
import random

import math


def get_Bellard_term_mpmath(i):
    print(f"Iteration #{i} calculating")
    term = (-1) ** i / mpmath.mpf(2) ** (10 * i) * (
            (-(mpmath.mpf(2) ** 5) / (4 * i + 1)) -
            (mpmath.mpf(1) / (4 * i + 3)) +
            ((mpmath.mpf(2) ** 8) / (10 * i + 1)) -
            ((mpmath.mpf(2) ** 6) / (10 * i + 3)) -

            ((mpmath.mpf(2) ** 2) / (10 * i + 5)) -
            ((mpmath.mpf(2) ** 2) / (10 * i + 7)) +
            (mpmath.mpf(1) / (10 * i + 9))
    )
    print(f"Iteration #{i} done")
    return term


def get_Bellard_term_dec(n):
    print(f"Iteration #{n} calculating")
    term = (-1) ** n / Decimal(2) ** (10 * n) * (
            (-(Decimal(2) ** 5) / (4 * n + 1)) -
            (Decimal(1) / (4 * n + 3)) +
            ((Decimal(2) ** 8) / (10 * n + 1)) -
            ((Decimal(2) ** 6) / (10 * n + 3)) -
            ((Decimal(2) ** 2) / (10 * n + 5)) -
            ((Decimal(2) ** 2) / (10 * n + 7)) +
            (Decimal(1) / (10 * n + 9))
    )
    print(f"Iteration #{n} done")
    return term


def get_Chudnovsky_term_mpmath(k):
    print(f"Iteration #{k} calculating")

    # numerator = (-1) ** k * mpmath.mpf(mpmath.fac(6 * k)) * (545140134 * k + 13591409)
    # denominator = mpmath.mpf(mpmath.fac(k)) ** 3 * mpmath.mpf(mpmath.fac(3 * k)) * mpmath.mpf(640320) ** (3 * k + 3 / 2)
    # term = numerator / denominator

    factorial_6k = math.factorial(6 * k)
    factorial_k3 = math.factorial(k) ** 3
    factorial_3k = math.factorial(3 * k)

    # Convert constants to Decimal
    C3_OVER_2 = mpmath.sqrt(mpmath.mpf(640320) ** (3*k*2 + 3))

    # Use Decimal for the final high precision calculations
    numerator = (-1) ** k * mpmath.mpf(factorial_6k) * (545140134 * k + 13591409)
    denominator = mpmath.mpf(factorial_k3) * mpmath.mpf(factorial_3k) * C3_OVER_2
    term = numerator / denominator

    print(f"Iteration #{k} done")
    return term


def get_Chudnovsky_term_dec(k):
    print(f"Iteration #{k} calculating")

    # Use integers for intermediate calculations where possible
    factorial_6k = math.factorial(6 * k)
    factorial_k3 = math.factorial(k) ** 3
    factorial_3k = math.factorial(3 * k)

    # Convert constants to Decimal
    C3_OVER_2 = Decimal.sqrt(Decimal(640320) ** (3*k*2 + 3))

    # Use Decimal for the final high precision calculations
    numerator = (-1) ** k * Decimal(factorial_6k) * (545140134 * k + 13591409)
    denominator = Decimal(factorial_k3) * Decimal(factorial_3k) * C3_OVER_2

    term = numerator / denominator

    print(f"Iteration #{k} done")
    return term


def compare_pis(calculated_pi, known_pi):
    calculated_str = str(calculated_pi)
    known_str = str(known_pi)

    # print(calculated_str)
    # print(known_str)

    for i in range(len(calculated_str)):
        if calculated_str[i] != known_str[i]:
            return i-2, len(calculated_str)-2

    return len(calculated_str)-2, len(calculated_str)-2


# def get_last_precision(csv_file):
#     if os.path.exists(csv_file):
#         with open(csv_file, 'r') as file:
#             last_line = file.readlines()[-1]
#             if last_line.strip():
#                 return int(last_line.split(',')[1])
#     return 0


def format_time(time_raw):
    hours = int(time_raw // 3600)
    minutes = int((time_raw % 3600) // 60)
    seconds = int(time_raw % 60)
    milliseconds = int((time_raw % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds}"


def monte_carlo_inside_circle():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    return x ** 2 + y ** 2 <= 1
