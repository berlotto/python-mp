import multiprocessing as mp
import time

def is_prime(n):
    for j in range(2, n - 1):
        if (n % j) == 0:
            return False
    return True

def count_primes(inputs=[]):
    return sum(inputs)


def write_output(n):
    print("Found {0} primes <= 100_000".format(n))


numbers = range(2, 100_000)

start_time = time.time()

pool = mp.Pool()
result = pool.map(is_prime, numbers)
n_primes = count_primes(inputs=result)
write_output(n_primes)

duration = time.time() - start_time
print(f"Duration {duration} seconds")