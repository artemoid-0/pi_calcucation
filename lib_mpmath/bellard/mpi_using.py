from mpi4py import MPI
import mpmath
import time

from auxiliary_functions import get_Bellard_term_mpmath


def pi_Bellard_MPI_mpmath(precision):
    print("Calculating with Bellard formula (mpmath) in MPI mode")

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print(f"Size: {size}")

    sum_value = mpmath.mpf(0)

    start_time = time.time()

    # Calculate the range of k values for each process
    for k in range(rank, precision, size):
        sum_value += get_Bellard_term_mpmath(k)

    # Reduce the sum to the root process
    global_sum = MPI.COMM_WORLD.reduce(sum_value, op=MPI.SUM, root=0)

    if rank == 0:
        pi_value = global_sum / mpmath.mpf(2) ** 6
        end_time = time.time()
        return (pi_value, end_time - start_time,
                {"algorithm": "Bellard formula",
                 "mode": "MPI",
                 "lib": "mpmath"})
    else:
        return None, None, None


def pi_Bellard_MPI_mpmath_dynamic(precision):
    print("Calculating with Bellard formula (mpmath) in MPI mode (dynamic)")

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Main process
        print(f"Size: {size}")
        sum_value = mpmath.mpf(0)
        task_index = 0
        start_time = time.time()

        # Sending tasks to auxiliary processes
        for i in range(1, size):
            if task_index < precision:
                comm.send(task_index, dest=i, tag=1)
                task_index += 1

        # Receiving results from auxiliary processes and sending new tasks
        for _ in range(precision):
            result = comm.recv(source=MPI.ANY_SOURCE, tag=2)
            sum_value += result[0]
            sender = result[1]
            if task_index < precision:
                comm.send(task_index, dest=sender, tag=1)
                task_index += 1
            else:
                comm.send(None, dest=sender, tag=0)  # Sending None to stop auxiliary processes

        pi_value = sum_value / mpmath.mpf(2) ** 6
        end_time = time.time()
        return (pi_value, end_time - start_time,
                {"algorithm": "Bellard formula",
                 "mode": "MPI dynamic",
                 "lib": "mpmath"})

    else:
        # Auxiliary processes
        sum_value = mpmath.mpf(0)
        while True:
            task_index = comm.recv(source=0, tag=MPI.ANY_TAG)
            if task_index is None:
                break
            term = get_Bellard_term_mpmath(task_index)
            comm.send((term, rank), dest=0, tag=2)
        return None, None, None


# if __name__ == '__main__':
#     precision = int(1e4)  # Пример значения precision
#     calculated_pi, elapsed_time, info = pi_Bellard_MPI_dynamic(precision)
#
#     if MPI.COMM_WORLD.Get_rank() == 0:
#         print(f"Calculated value of pi: {calculated_pi}")
#         print(f"Elapsed time: {elapsed_time} seconds")
#         correct_digits, all_digits = compare_pis(calculated_pi, mpmath.pi)
#         print(f"Correct digits: {correct_digits} / {all_digits}")
