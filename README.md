# python-mp

Multiprocessing cpu_bound performance testing with a simple calc of number of primes found from 2 to 100k.

* primes.py -> Simples, no multiprocessing
* primes_futures.py -> Uses concurrent.futures.ThreadPoolExecutor
* primes_futures_proc.py -> Uses concurrent.futures.ProcessPoolExecutor
* primes_mp -> Uses multiprocessing.Pool

Using some information and codes from:

https://medium.com/@edytarcio/async-await-introdu%C3%A7%C3%A3o-%C3%A0-programa%C3%A7%C3%A3o-ass%C3%ADncrona-em-python-fa30d077018e

https://github.com/realpython/materials/tree/master/concurrency-overview
