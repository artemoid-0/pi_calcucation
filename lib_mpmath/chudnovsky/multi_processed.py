import time
from multiprocessing import Pool, cpu_count
from auxiliary_functions import get_Chudnovsky_term_mpmath


def pi_Chudnovsky_MP_mpmath_with_factorial(precision):
    print("Calculating with Chudnovsky formula (mpmath) (factorial) in multi-processed mode")

    start_time = time.time()

    with Pool(processes=cpu_count()) as pool:
        terms = pool.map(get_Chudnovsky_term_mpmath, range(precision))
        value = sum(terms)

    value *= 12
    value = 1 / value
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Chudnovsky formula (factorial)",
             "mode": "multi-processed",
             "lib": "mpmath"})
