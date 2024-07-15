from lib_mpmath.bellard.single_threaded import pi_Bellard_ST_mpmath, pi_Bellard_ST_mpmath_with_info
from lib_mpmath.bellard.multi_threaded import pi_Bellard_MT_mpmath
from lib_mpmath.bellard.multi_processed import pi_Bellard_MP_mpmath
from lib_mpmath.bellard.mpi_using import pi_Bellard_MPI_mpmath, pi_Bellard_MPI_mpmath_dynamic

from lib_mpmath.chudnovsky.single_threaded import pi_Chudnovsky_ST_mpmath_no_factorial, pi_Chudnovsky_ST_mpmath_no_factorial_with_info, pi_Chudnovsky_ST_mpmath_with_factorial, pi_Chudnovsky_ST_mpmath_with_factorial_with_info
from lib_mpmath.chudnovsky.multi_threaded import pi_Chudnovsky_MT_mpmath_with_factorial
from lib_mpmath.chudnovsky.multi_processed import pi_Chudnovsky_MP_mpmath_with_factorial
from lib_mpmath.chudnovsky.mpi_using import pi_Chudnovsky_MPI_mpmath_with_factorial, pi_Chudnovsky_MPI_mpmath_dynamic

from lib_decimal.bellard.single_threaded import pi_Bellard_ST_decimal, pi_Bellard_ST_decimal_with_info
from lib_decimal.bellard.multi_threaded import pi_Bellard_MT_decimal
from lib_decimal.bellard.multi_processed import pi_Bellard_MP_decimal
from lib_decimal.bellard.mpi_using import pi_Bellard_MPI_decimal, pi_Bellard_MPI_decimal_dynamic

from lib_decimal.chudnovsky.single_threaded import pi_Chudnovsky_ST_decimal_no_factorial, pi_Chudnovsky_ST_decimal_no_factorial_with_info, pi_Chudnovsky_ST_decimal_with_factorial, pi_Chudnovsky_ST_decimal_with_factorial_with_info
from lib_decimal.chudnovsky.multi_threaded import pi_Chudnovsky_MT_decimal_with_factorial
from lib_decimal.chudnovsky.multi_processed import pi_Chudnovsky_MP_decimal_with_factorial
from lib_decimal.chudnovsky.mpi_using import pi_Chudnovsky_MPI_decimal_with_factorial, pi_Chudnovsky_MPI_decimal_dynamic

# for 1e3 digits
# DPS = int(1e3)
# MAX_PRECISION_BELLARD = int(331)

# for 1e4 digits
# DPS = int(1e4)+1
# MAX_PRECISION_BELLARD = int(3321)
# MAX_PRECISION_CHUDNOVSKY = int(706)
# MAX_PRECISION_MONTECARLO = int(1e6)

# for 5e4 digits
# DPS = int(5e4)+1
# MAX_PRECISION_BELLARD = int(16609)
# MAX_PRECISION_CHUDNOVSKY = int(3526)
# MAX_PRECISION_MONTECARLO = int(1e6)

# for 1e5 digits
DPS = int(1e5)+1
MAX_PRECISION_BELLARD = int(33217)
MAX_PRECISION_CHUDNOVSKY = int(7052)
MAX_PRECISION_MONTECARLO = int(1e6)




function_precision_dict = {
    "mpmath": {
        "Bellard": {
            "precision": MAX_PRECISION_BELLARD,
            "function": {
                "ST": pi_Bellard_ST_mpmath,
                "ST_info": pi_Bellard_ST_mpmath_with_info,
                "MT": pi_Bellard_MT_mpmath,
                "MP": pi_Bellard_MP_mpmath,
                "MPI": pi_Bellard_MPI_mpmath,
                "MPI dynamic": pi_Bellard_MPI_mpmath_dynamic,
            }
        },
        "Chudnovsky": {
            "precision": MAX_PRECISION_CHUDNOVSKY,
            "function": {
                "ST_no_factorial": pi_Chudnovsky_ST_mpmath_no_factorial,
                "ST_no_factorial_info": pi_Chudnovsky_ST_mpmath_no_factorial_with_info,
                "ST_factorial": pi_Chudnovsky_ST_mpmath_with_factorial,
                "ST_factorial_info": pi_Chudnovsky_ST_mpmath_with_factorial_with_info,
                "MT": pi_Chudnovsky_MT_mpmath_with_factorial,
                "MP": pi_Chudnovsky_MP_mpmath_with_factorial,
                "MPI": pi_Chudnovsky_MPI_mpmath_with_factorial,
                "MPI dynamic": pi_Chudnovsky_MPI_mpmath_dynamic,
            }
        }
    },
    "decimal": {
        "Bellard": {
            "precision": MAX_PRECISION_BELLARD,
            "function": {
                "ST": pi_Bellard_ST_decimal,
                "ST_info": pi_Bellard_ST_decimal_with_info,
                "MT": pi_Bellard_MT_decimal,
                "MP": pi_Bellard_MP_decimal,
                "MPI": pi_Bellard_MPI_decimal,
                "MPI dynamic": pi_Bellard_MPI_decimal_dynamic,
            }
        },
        "Chudnovsky": {
            "precision": MAX_PRECISION_CHUDNOVSKY,
            "function": {
                "ST_no_factorial": pi_Chudnovsky_ST_decimal_no_factorial,
                "ST_no_factorial_info": pi_Chudnovsky_ST_decimal_no_factorial_with_info,
                "ST_factorial": pi_Chudnovsky_ST_decimal_with_factorial,
                "ST_factorial_info": pi_Chudnovsky_ST_decimal_with_factorial_with_info,
                "MT": pi_Chudnovsky_MT_decimal_with_factorial,
                "MP": pi_Chudnovsky_MP_decimal_with_factorial,
                "MPI": pi_Chudnovsky_MPI_decimal_with_factorial,
                "MPI dynamic": pi_Chudnovsky_MPI_decimal_dynamic,
            }
        }
    }
}