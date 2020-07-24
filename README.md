# python-mp

Multiprocessing preformance testing with a simple calc of nbr of primes found from 2 to 100k.

* primes.py -> Simples, no multiprocessing
* primes_futures.py -> Uses concurrent.futures.ThreadPoolExecutor
* primes_futures_proc.py -> Uses concurrent.futures.ProcessPoolExecutor
* primes_mp -> Uses multiprocessing.Pool

