import time

#Primes - no concurrency
def is_prime(n):
    for j in range(2, n - 1):
        if (n % j) == 0:
            return False
    return True

def count_primes(inputs=[]):
    return sum(inputs)



def write_output(n):
    print("Found {0} primes <= 100_000.\n".format(n))


start_time = time.time()

prime_tasks = [is_prime(n) for n in range(2, 100_000)]
n_primes = count_primes(inputs=prime_tasks)
write_output(n_primes)

duration = time.time() - start_time
print(f"Duration {duration} seconds")