from mpi4py import MPI
from decimal import Decimal
import time

from auxiliary_functions import get_Bellard_term_dec


def pi_Bellard_MPI_decimal(precision):
    print("Calculating with Bellard formula (decimal) in MPI mode")

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print(f"Size: {size}")

    sum_value = Decimal(0)

    start_time = time.time()

    # Calculate the range of k values for each process
    for k in range(rank, precision, size):
        sum_value += get_Bellard_term_dec(k)

    # Reduce the sum to the root process
    global_sum = MPI.COMM_WORLD.reduce(sum_value, op=MPI.SUM, root=0)

    if rank == 0:
        pi_value = global_sum / Decimal(2) ** 6
        end_time = time.time()
        return (pi_value, end_time - start_time,
                {"algorithm": "Bellard formula",
                 "mode": "MPI",
                 "lib": "decimal"})
    else:
        return None, None, None


def pi_Bellard_MPI_decimal_dynamic(precision):
    print("Calculating with Bellard formula (decimal) in MPI mode (dynamic)")

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Главный процесс
        print(f"Size: {size}")
        sum_value = Decimal(0)
        task_index = 0
        start_time = time.time()

        # Отправляем задачи вспомогательным процессам
        for i in range(1, size):
            if task_index < precision:
                comm.send(task_index, dest=i, tag=1)
                task_index += 1

        # Получаем результаты от вспомогательных процессов и отправляем новые задачи
        for _ in range(precision):
            result = comm.recv(source=MPI.ANY_SOURCE, tag=2)
            sum_value += result[0]
            sender = result[1]
            if task_index < precision:
                comm.send(task_index, dest=sender, tag=1)
                task_index += 1
            else:
                comm.send(None, dest=sender, tag=0)  # Отправляем None, чтобы остановить вспомогательные процессы

        pi_value = sum_value / Decimal(2) ** 6
        end_time = time.time()
        return (pi_value, end_time - start_time,
                {"algorithm": "Bellard formula",
                 "mode": "MPI dynamic",
                 "lib": "decimal"})

    else:
        # Вспомогательные процессы
        sum_value = Decimal(0)
        while True:
            task_index = comm.recv(source=0, tag=MPI.ANY_TAG)
            if task_index is None:
                break
            term = get_Bellard_term_dec(task_index)
            comm.send((term, rank), dest=0, tag=2)
        return None, None, None

