import threading, time



def test(i):
    tm = time.time()
    try:
        for itr in range(1_00_000_000):
            pass
    finally:
        print(f'{i} - tm took {time.time() - tm}')
def with_threading():

    threads = []
    for i in range(5):
        t = threading.Thread(target = test, args = (i, ))
        t.daemon = True
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

tm = time.time()
with_threading()
print(round(time.time() - tm, 2))

[print('-' * 10) for i in range(5)]


import concurrent.futures
tm = time.time()
with concurrent.futures.ThreadPoolExecutor(8) as pool:
    futures = [pool.submit(test, (i)) for i in range(5)]

    for future in concurrent.futures.as_completed(futures):
        pass

print(round(time.time() - tm, 2))

'''
    threading:
        Threading:What Is the Python Global Interpreter Lock (GIL)?
    Multiprocessing:

    asyncio:


    What are differences between threading, multiprocessing and asyncio
'''

