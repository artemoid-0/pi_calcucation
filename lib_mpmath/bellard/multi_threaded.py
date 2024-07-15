import time
import mpmath
from concurrent.futures import ThreadPoolExecutor
from auxiliary_functions import get_Bellard_term_mpmath


def pi_Bellard_MT_mpmath(precision):
    print("Calculating with Bellard formula (mpmath) in multi-threaded mode")
    value = mpmath.mpf(0)

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_Bellard_term_mpmath, i) for i in range(precision)]

        for future in futures:
            value += future.result()

    value /= mpmath.mpf(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula",
             "mode": "multi-threaded",
             "lib": "mpmath"})
