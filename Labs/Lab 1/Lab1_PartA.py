import random
import timeit
import sys

def sum_array(arr):
    """Calculate the sum of an array."""
    return sum(arr)

def generate_arrays(sizes):
    """
    Generate random arrays of specified sizes.
    Ensures that the size does not exceed the range of numbers.
    """
    return [random.sample(range(1, max(size + 1, 100)), size) for size in sizes]

def measure_execution_time(arrays):
    """Measure execution time for summing arrays."""
    for arr in arrays:
        execution_time = timeit.timeit(lambda: sum_array(arr), number=100)
        print(f"Array size: {len(arr)}, Execution Time: {execution_time:.5f} seconds")

def measure_memory_usage(arrays):
    """Measure memory usage of arrays."""
    for arr in arrays:
        size = sys.getsizeof(arr)
        print(f"Array size: {len(arr)}, Memory Usage: {size} bytes")

if __name__ == "__main__":
    array_sizes = [100, 1000, 10000]
    arrays = generate_arrays(array_sizes)

    print("Execution Time Analysis:")
    measure_execution_time(arrays)

    print("\nMemory Usage Analysis:")
    measure_memory_usage(arrays)
