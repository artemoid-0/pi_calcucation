import time
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal

from auxiliary_functions import get_Bellard_term_dec


def pi_Bellard_MT_decimal(precision):
    print("Calculating with Bellard formula (decimal) in multi-threaded mode")
    value = Decimal(0)

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_Bellard_term_dec, i) for i in range(precision)]

        for future in futures:
            value += future.result()

    value /= Decimal(2) ** 6
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Bellard formula",
             "mode": "multi-threaded",
             "lib": "decimal"})
