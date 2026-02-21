import numpy as np

#Task 1: Create an Array and Basic Math

temp_celsius = np.array([22, 25, 28, 24, 26])
temp_f = temp_celsius * 1.8 + 32
average_temp = temp_f.mean()

print(f"Celsius: {temp_celsius}")
print(f"Fahrenheit: {temp_f}")
print(f"Average Fahrenheit: {average_temp: .1f}")

print("\n\n")

#Task-2: Array Shape and Statistics

test_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print(f"Shape : {test_scores.shape}")
print(f"Total elements: {test_scores.size}")
print(f"Highesht Score: {test_scores.max()}")
print(f"Lowest Score: {test_scores.min()}")
print(f"Range: {test_scores.ptp()}")

#Task 3: Performance Comparison
import time

arr = np.arange(1,50001, dtype=np.int64)
list = list(range(1,50001))

start_time = time.time()
np_sum = np.sum(arr)
end_time = time.time()
np_time = end_time - start_time

start_time = time.time()
list_sum = sum(list)
end_time = time.time()
list_time = end_time - start_time

print(f"NumPy sum: {np_sum}")
print(f"Python sum: {list_sum}")
print(f"NumPy time: {np_time:.4f} seconds")
print(f"Python time: {list_time:.4f} seconds")
print(f"NumPy is {list_time/np_time:.1f}x faster")

