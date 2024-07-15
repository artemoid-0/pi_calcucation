import time

from decimal import Decimal
from multiprocessing import Pool, cpu_count
from auxiliary_functions import get_Bellard_term_dec



def pi_Bellard_MP_decimal(precision):
    print("Calculating with Bellard formula (decimal) in multi-processed mode")

    start_time = time.time()

    with Pool(processes=cpu_count()) as pool:
        terms = pool.map(get_Bellard_term_dec, range(precision))
        value = sum(terms)

    value /= Decimal(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula",
             "mode": "multi-processed",
             "lib": "decimal"})
