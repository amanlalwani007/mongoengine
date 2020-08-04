import time
import threading
import concurrent.futures
start=time.perf_counter()
def do_something(seconds):
    print(f'slepping  {seconds} second ....')
    time.sleep(seconds)
    return f'Done Sleeping {seconds}'

'''t1=threading.Thread(target=do_something)
t2=threading.Thread(target=do_something)
t1.start()
t2.start()
t1.join()
t2.join()'''
'''threads=[]
for _ in range(10):
    t=threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()'''

with  concurrent.futures.ThreadPoolExecutor() as executor:
   '''results=[executor.submit(do_something,1) for _ in range(10)]
   for f in concurrent.futures.as_completed(results):
       print(f.result())'''
   secs=[5,4,3,2,1]
   results=executor.map(do_something,secs)
   for result in results:
       print(result)

#it returns a future object

finish=time.perf_counter()
print(f'Finished  in {round(finish-start,2)} seconds')

