import time
import multiprocessing
start=time.perf_counter()
import concurrent.futures
def do_something(seconds):
    print(f'Sleeping {seconds} second..')
    time.sleep(seconds)
    return f'Done Sleeping ... {seconds}'


'''p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=do_something)
p1.start()
p2.start()
p1.join()
p2.join()
'''
'''processes=[]
for _ in range(10):
    p=multiprocessing.Process(target=do_something,args=[1.5])
    p.start()
    processes.append(p)
for process in processes:
    process.join()
'''

'''with concurrent.futures .ProcessPoolExecutor() as executor:
    results=[executor.submit(do_something,1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())'''
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    results=executor.map(do_something,secs)
    for result in results:
        print(result)




finish=time.perf_counter()
print(f'Finished in {round(finish-start,2)}')







#IO Bound task don't use cpu that much

#in multithreading func are running concurrently it does
#mean that thry are running in the same time but in multi processing they are runnig at the same time