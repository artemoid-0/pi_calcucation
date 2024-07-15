import time
from decimal import Decimal
from concurrent.futures import ThreadPoolExecutor
from auxiliary_functions import get_Chudnovsky_term_dec


def pi_Chudnovsky_MT_decimal_with_factorial(precision):
    print("Calculating with Chudnovsky formula (decimal) (factorial) in multi-threaded mode")
    value = Decimal(0)

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_Chudnovsky_term_dec, i) for i in range(precision)]

        for future in futures:
            value += future.result()

    value *= 12
    value = 1/value
    end_time = time.time()

    return (value, end_time - start_time,
            {"algorithm": "Chudnovsky formula (factorial)",
             "mode": "multi-threaded",
             "lib": "decimal"})
