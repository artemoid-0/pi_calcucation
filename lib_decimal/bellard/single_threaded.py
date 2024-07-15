import csv
import time

from decimal import Decimal
from auxiliary_functions import compare_pis
from mpmath import pi as known_pi


CSV_FILE = 'results/bellard_single_decimal'


def pi_Bellard_ST_decimal(precision):
    print("Calculating with Bellard formula (decimal) in single threaded mode (no iteration time measurement)")
    value = Decimal(0)

    start_time = time.time()
    for i in range(precision):
        print(f"Iteration #{i} calculating")

        value += (-1) ** i / Decimal(2) ** (10 * i) * (
                (-(Decimal(2) ** 5) / (4 * i + 1)) -
                (Decimal(1) / (4 * i + 3)) +
                ((Decimal(2) ** 8) / (10 * i + 1)) -
                ((Decimal(2) ** 6) / (10 * i + 3)) -
                ((Decimal(2) ** 2) / (10 * i + 5)) -
                ((Decimal(2) ** 2) / (10 * i + 7)) +
                (Decimal(1) / (10 * i + 9))
        )
        print(f"Iteration #{i} done")

    value /= Decimal(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula, (no iteration time measurement)",
             "mode": "single-threaded",
             "lib": "decimal"})


def pi_Bellard_ST_decimal_with_info(precision):
    print("Calculating with Bellard formula (decimal) in single threaded mode (with iteration time measurement)")
    value = Decimal(0)

    with open(CSV_FILE + f"_{str(precision)}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Precision", "Accuracy", "Time for iteration"])

        start_time = time.time()
        for i in range(precision):
            print(f"Iteration #{i} calculating")
            iteration_start_time = time.time()

            value += (-1) ** i / Decimal(2) ** (10 * i) * (
                    (-(Decimal(2) ** 5) / (4 * i + 1)) -
                    (Decimal(1) / (4 * i + 3)) +
                    ((Decimal(2) ** 8) / (10 * i + 1)) -
                    ((Decimal(2) ** 6) / (10 * i + 3)) -
                    ((Decimal(2) ** 2) / (10 * i + 5)) -
                    ((Decimal(2) ** 2) / (10 * i + 7)) +
                    (Decimal(1) / (10 * i + 9))
            )
            iteration_end_time = time.time()
            print(f"Iteration #{i} done")

            writer.writerow([i, compare_pis(value / Decimal(2) ** 6, known_pi)[0], iteration_end_time - iteration_start_time])

    value /= Decimal(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula, (with iteration time measurement)",
             "mode": "single-threaded",
             "lib": "decimal"})
