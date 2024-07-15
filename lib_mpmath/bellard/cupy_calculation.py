import time
import cupy as cp
import mpmath

# Устанавливаем точность mpmath
# mpmath.mp.dps = int(1e4)


def get_iteration_value(i):
    print(i)
    term = (-1) ** i / mpmath.mpf(2) ** (10 * i) * (
            (-(mpmath.mpf(2) ** 5) / (4 * i + 1)) -
            (mpmath.mpf(1) / (4 * i + 3)) +
            ((mpmath.mpf(2) ** 8) / (10 * i + 1)) -
            ((mpmath.mpf(2) ** 6) / (10 * i + 3)) -
            ((mpmath.mpf(2) ** 2) / (10 * i + 5)) -
            ((mpmath.mpf(2) ** 2) / (10 * i + 7)) +
            (mpmath.mpf(1) / (10 * i + 9))
    )
    return term


def pi_Bellar(precision):
    print("Calculating in multi-threaded mode using GPU")
    value = mpmath.mpf(0)

    start_time = time.time()

    # Перемещаем расчеты на GPU с помощью CuPy
    i_vals = cp.arange(precision)
    terms = cp.array([get_iteration_value(i) for i in range(precision)], dtype=cp.float64)
    value = cp.sum(terms)

    value = value / (2 ** 6)
    print(value)
    exit()
    value = mpmath.mpf(value.get())  # Извлекаем одиночное значение и конвертируем в mpmath.mpf
    end_time = time.time()

    return value, end_time - start_time


# Пример использования функции
if __name__ == '__main__':
    precision = 100  # Установите желаемую точность
    calculated_pi, time_taken = pi_Bellar(precision)

    print(f"Calculated Pi: {calculated_pi}")
    print(f"Total Time Taken: {time_taken} seconds")
