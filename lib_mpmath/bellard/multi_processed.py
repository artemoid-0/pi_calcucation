import time

import mpmath
from multiprocessing import Pool, cpu_count
from auxiliary_functions import get_Bellard_term_mpmath



def pi_Bellard_MP_mpmath(precision):
    print("Calculating with Bellard formula (mpmath) in multi-processed mode")
    value = mpmath.mpf(0)

    start_time = time.time()

    with Pool(processes=cpu_count()) as pool:
        terms = pool.map(get_Bellard_term_mpmath, range(precision))
        value = sum(terms)

    value /= mpmath.mpf(2) ** 6

    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula",
             "mode": "multi-processed",
             "lib": "mpmath"})
