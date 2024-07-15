import csv
import math
import time
import mpmath

from auxiliary_functions import compare_pis

CSV_FILE = 'results/chudnovsky_single_mpmath'


def pi_Chudnovsky_ST_mpmath_no_factorial(precision):
    print("Calculating with Chudnovsky formula (mpmath) (no factorial) in single threaded mode (no iteration time measurement)")

    start_time = time.time()

    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, precision):
        print(f"Iteration #{k} calculating")
        M = (K ** 3 - (K << 4)) * M // k ** 3
        L += 545140134
        X *= -262537412640768000
        S += mpmath.mpf(M * L) / X
        K += 12
    pi = 426880 * mpmath.sqrt(10005) / S

    end_time = time.time()

    return (pi, end_time - start_time,
            {"algorithm": "Chudnovsky formula (no factorial), (no iteration time measurement)",
             "mode": "single-threaded",
             "lib": "mpmath"})


def pi_Chudnovsky_ST_mpmath_no_factorial_with_info(precision):
    print(
        "Calculating with Chudnovsky formula (mpmath) (no factorial) in single threaded mode (with iteration time measurement)")

    with open(CSV_FILE + f"_no_factorial_{str(precision)}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Precision", "Accuracy", "Time for iteration"])

        start_time = time.time()

        K, M, L, X, S = 6, 1, 13591409, 1, 13591409
        for k in range(1, precision):
            print(f"Iteration #{k - 1} calculating")
            iteration_start_time = time.time()

            M = (K ** 3 - (K << 4)) * M // k ** 3
            L += 545140134
            X *= -262537412640768000
            S += mpmath.mpf(M * L) / X
            K += 12

            iteration_end_time = time.time()
            print(f"Iteration #{k - 1} done")

            writer.writerow([k, compare_pis(426880 * mpmath.sqrt(10005) / S, mpmath.pi)[0],
                             iteration_end_time - iteration_start_time])

    pi = 426880 * mpmath.sqrt(10005) / S
    end_time = time.time()

    return (pi, end_time - start_time,
            {"algorithm": "Chudnovsky formula (no factorial), (with iteration time measurement)",
             "mode": "single-threaded",
             "lib": "mpmath"})


def pi_Chudnovsky_ST_mpmath_with_factorial(precision):
    print("Calculating with Chudnovsky formula (mpmath) (factorial) in single threaded mode (no iteration time measurement)")
    start_time = time.time()
    value = mpmath.mpf(0)

    for k in range(precision):
        print(f"Iteration #{k} calculating")
        # numerator = (-1) ** k * mpmath.mpf(mpmath.fac(6 * k)) * (545140134 * k + 13591409)
        # denominator = mpmath.mpf(mpmath.fac(k)) ** 3 * mpmath.mpf(mpmath.fac(3 * k)) * mpmath.mpf(640320) ** (
        #         3 * k + 3 / 2)
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
        value += term
        print(f"Iteration #{k} done")

    value *= 12
    value = 1 / value
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Chudnovsky formula (factorial), (no iteration time measurement)",
             "mode": "single-threaded",
             "lib": "mpmath"})


def pi_Chudnovsky_ST_mpmath_with_factorial_with_info(precision):
    print("Calculating with Chudnovsky formula (mpmath) (factorial) in single threaded mode (with iteration time measurement)")
    value = mpmath.mpf(0)

    with open(CSV_FILE + f"_factorial_{str(precision)}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Precision", "Accuracy", "Time for iteration"])

        start_time = time.time()

        for k in range(precision):
            print(f"Iteration #{k} calculating")
            iteration_start_time = time.time()

            # numerator = (-1) ** k * mpmath.mpf(mpmath.fac(6 * k)) * (545140134 * k + 13591409)
            # denominator = mpmath.mpf(mpmath.fac(k)) ** 3 * mpmath.mpf(mpmath.fac(3 * k)) * mpmath.mpf(640320) ** (
            #         3 * k + 3 / 2)
            # term = numerator / denominator
            # value += term

            factorial_6k = math.factorial(6 * k)
            factorial_k3 = math.factorial(k) ** 3
            factorial_3k = math.factorial(3 * k)

            # Convert constants to Decimal
            C3_OVER_2 = mpmath.sqrt(mpmath.mpf(640320) ** (3 * k * 2 + 3))

            # Use Decimal for the final high precision calculations
            numerator = (-1) ** k * mpmath.mpf(factorial_6k) * (545140134 * k + 13591409)
            denominator = mpmath.mpf(factorial_k3) * mpmath.mpf(factorial_3k) * C3_OVER_2
            term = numerator / denominator
            value += term

            iteration_end_time = time.time()
            print(f"Iteration #{k} done")
            writer.writerow([k, compare_pis(1 / (value * 12), mpmath.pi)[0], iteration_end_time - iteration_start_time])

    value *= 12
    value = 1 / value
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Chudnovsky formula (factorial), (with iteration time measurement)",
             "mode": "single-threaded",
             "lib": "mpmath"})
