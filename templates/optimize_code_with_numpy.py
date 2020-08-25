import time
import numpy as np 
py_array=[1,2,3,4,5,6,7,8,9]
np_array=np.array([1,2,3,4,5,6,7,8,9])

print(f"python array :{py_array}")
print(f"numpy array:{np_array}")

number=np.arange(50).reshape(5,10)

###memory fragmentation

def norm_square_list(vector):
    norm=0
    for v in vector:
        norm+=v*v
    return norm
def norm_square_list_comp(vector):
    return sum([v*v for v in vector])

def norm_square_np(vector):
    return np.sum(vector*vector)

def norm_square_np_dot(vector):
    return mp.dot(vector*vector)    

vector=range(1000000)
start_time=time.time()
norm_square_list(vector)
print(time.time()-start_time)
start_time=time.time()
norm_square_list_comp(vector)
print(time.time()-start_time)
start_time=time.time()
vector=np.arange(1000000)
norm_square_np(vector)
print(time.time()-start_time)


