import asyncio
import time

async def is_prime(n):
    for j in range(2, n - 1):
        if (n % j) == 0:
            return False
    return True


async def count_primes(inputs=[]):
    return sum(inputs)


def write_output(n):
    print("Found {0} primes <= 100_000".format(n))


async def calc_primes(inputs=[]):
	results = []
	for number in inputs:
		results.append(await asyncio.ensure_future(is_prime(number)))

	# result = [await is_prime(n) for n in inputs]
	n_primes = await count_primes(inputs=results)
	# write_output(n_primes)
	# await asyncio.gather(*tasks)


numbers = range(2, 100_000)

start_time = time.time()

asyncio.run(calc_primes(numbers))

duration = time.time() - start_time
print(f"Duration {duration} seconds")