import csv
import time
import decimal

import mpmath
from mpi4py import MPI

from auxiliary_functions import *
from function_config import function_precision_dict, DPS

import os
import psutil

LOG_FILENAME = 'results/log.csv'

mpmath.mp.dps = DPS
decimal.getcontext().prec = DPS

if __name__ == '__main__':

    known_pi = mpmath.pi

    library = "decimal"
    algorithm = "Chudnovsky"
    #function_name = "ST_factorial"

    for function_name in ["ST_factorial_info",]:

        precision = function_precision_dict[library][algorithm]["precision"]
        function = function_precision_dict[library][algorithm]["function"][function_name]

        calculated_pi, time_taken, info = function(precision)
        if calculated_pi is None:
            exit()
        # MPI.Finalize()

        print(f"Calculated Pi: {calculated_pi}")
        print(f"Known Pi:      {known_pi}")
        print(f"Execution Time: {time_taken} seconds")

        start_time = time.time()
        correct_digits, all_digits = compare_pis(calculated_pi, known_pi)
        print(f"Correct digits: {correct_digits} / {all_digits}")
        print(f"Comparing Time: {time.time() - start_time} seconds")

        number_of_recording = None
        if not os.path.exists(LOG_FILENAME):
            number_of_recording = 1
            with open(LOG_FILENAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(
                    ['#', 'Algorithm', 'Mode', 'Lib', 'DPS', 'Precision', 'Correct digits', 'Calculation time',
                     'Description'])
        else:
            with open(LOG_FILENAME, 'r', newline='') as f:
                reader = csv.reader(f)
                number_of_recording = sum(1 for _ in reader)

        with open(LOG_FILENAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([number_of_recording, info["algorithm"], info["mode"], info["lib"], DPS, precision,
                             f"{correct_digits} / {all_digits}", format_time(time_taken), ""])

        battery = psutil.sensors_battery()
        now = time.localtime()
        current_time = time.strftime("%H:%M:%S", now)
        print("Calculation ended at", current_time)
        print("At the end of calculation battery was power plugged:", battery.power_plugged)
        if not battery.power_plugged:
            exit()
