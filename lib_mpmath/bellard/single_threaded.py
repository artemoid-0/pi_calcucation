import csv
import mpmath
import time

from auxiliary_functions import compare_pis

CSV_FILE = 'results/bellard_single_mpmath'


def pi_Bellard_ST_mpmath(precision):
    print("Calculating with Bellard formula (mpmath) in single threaded mode (no iteration time measurement)")
    value = mpmath.mpf(0)

    start_time = time.time()
    for i in range(precision):
        print(f"Iteration #{i} calculating")

        value += (-1) ** i / mpmath.mpf(2) ** (10 * i) * (
                (-(mpmath.mpf(2) ** 5) / (4 * i + 1)) -
                (mpmath.mpf(1) / (4 * i + 3)) +
                ((mpmath.mpf(2) ** 8) / (10 * i + 1)) -
                ((mpmath.mpf(2) ** 6) / (10 * i + 3)) -
                ((mpmath.mpf(2) ** 2) / (10 * i + 5)) -
                ((mpmath.mpf(2) ** 2) / (10 * i + 7)) +
                (mpmath.mpf(1) / (10 * i + 9))
        )
        print(f"Iteration #{i} done")

    value /= mpmath.mpf(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula, (no iteration time measurement)",
             "mode": "single-threaded",
             "lib": "mpmath"})


def pi_Bellard_ST_mpmath_with_info(precision):
    print("Calculating with Bellard formula (mpmath) in single threaded mode (with iteration time measurement)")
    value = mpmath.mpf(0)

    with open(CSV_FILE + f"_{str(precision)}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Precision", "Accuracy", "Time for iteration"])

        start_time = time.time()
        for i in range(precision):
            print(f"Iteration #{i} calculating")
            iteration_start_time = time.time()

            value += (-1) ** i / mpmath.mpf(2) ** (10 * i) * (
                    (-(mpmath.mpf(2) ** 5) / (4 * i + 1)) -
                    (mpmath.mpf(1) / (4 * i + 3)) +
                    ((mpmath.mpf(2) ** 8) / (10 * i + 1)) -
                    ((mpmath.mpf(2) ** 6) / (10 * i + 3)) -
                    ((mpmath.mpf(2) ** 2) / (10 * i + 5)) -
                    ((mpmath.mpf(2) ** 2) / (10 * i + 7)) +
                    (mpmath.mpf(1) / (10 * i + 9))
            )
            iteration_end_time = time.time()
            print(f"Iteration #{i} done")

            writer.writerow([i, compare_pis(value / mpmath.mpf(2) ** 6, mpmath.pi)[0], iteration_end_time - iteration_start_time])

    value /= mpmath.mpf(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula, (with iteration time measurement)",
             "mode": "single-threaded",
             "lib": "mpmath"})
