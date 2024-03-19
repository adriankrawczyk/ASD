# This code compares sorting algorithms and prints out their evaluation time
import random
import time
def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def generate_array_of_arrays(num_arrays,n):
    array_of_arrays = []
    for _ in range(num_arrays):
        length = random.randint(1, n)
        sub_array = [random.randint(1, n) for _ in range(length)]
        array_of_arrays.append(sub_array)
    return array_of_arrays


def sort_1(T):
    n = len(T)
    for i in range(n):
        for j in range(0, n-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T

def sort_2(T):
    n = len(T) 
    if n < 2:
        return T
    pivot = T[n-2]
    m = [x for x in T if x == pivot]
    r = [x for x in T if x > pivot]
    l = [x for x in T if x < pivot]
    return sort_2(l) + m + sort_2(r)

def test_1(n):
    for i in n:
        sort_1(i)

def test_2(n):
    for i in n:
        sort_2(i)

n = generate_array_of_arrays(100, 1000)
for_loop_result, for_loop_time = measure_execution_time(test_1, n)
while_loop_result, while_loop_time = measure_execution_time(test_2, n)

print("Execution time for test_1:", for_loop_time, "seconds")
print("Execution time for test_2:", while_loop_time, "seconds")