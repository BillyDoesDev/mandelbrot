from functools import lru_cache

MAX_ITER = 1e2


@lru_cache
def mandelbrot(c, display=False):
    z = iterations = 0
    while z.imag <= 2 and iterations <= MAX_ITER:
        z = z * z + c
        if display:
            print(z.real, z.imag)
        iterations += 1
    return iterations


if __name__ == "__main__":
    mandelbrot(0.5j, display=True)
