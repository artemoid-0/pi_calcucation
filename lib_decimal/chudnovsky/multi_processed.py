import decimal
import time
from multiprocessing import Pool, cpu_count
from auxiliary_functions import get_Chudnovsky_term_dec


def pi_Chudnovsky_MP_decimal_with_factorial(precision):
    print("Calculating with Chudnovsky formula (decimal) (factorial) in multi-processed mode")
    start_time = time.time()

    with Pool(processes=cpu_count()) as pool:
        terms = pool.map(get_Chudnovsky_term_dec, range(precision))
        value = sum(terms)

    value *= 12
    value = 1 / value
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Chudnovsky formula (factorial)",
             "mode": "multi-processed",
             "lib": "decimal"})
