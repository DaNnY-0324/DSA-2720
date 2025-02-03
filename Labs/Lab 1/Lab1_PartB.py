import random
import timeit
import sys

# Function to perform matrix addition
def add_matrices(mat1, mat2):
    """
    Add two matrices element-wise.
    Each element of the result is the sum of corresponding elements in the input matrices.
    Time complexity is O(n²) for an n x n matrix because we iterate through all elements.
    """
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Function to generate a random matrix
def generate_matrix(size):
    """
    Generate a random square matrix of the specified size.
    Each matrix element is a random integer within a defined range.
    This is used to test the performance of matrix addition with different input sizes.
    """
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Function to measure execution time of matrix addition
def measure_execution_time(matrices):
    """
    Measure the execution time for adding two matrices.
    Uses the `timeit` module to repeat the operation and provide accurate timing results.
    Helps analyze the time complexity of the add_matrices function.
    """
    for mat1, mat2 in matrices:
        execution_time = timeit.timeit(lambda: add_matrices(mat1, mat2), number=10)
        print(f"Matrix size: {len(mat1)}x{len(mat1[0])}, Execution Time: {execution_time:.5f} seconds")

# Function to measure memory usage of matrices
def measure_memory_usage(matrices):
    """
    Measure the memory usage of two matrices using `sys.getsizeof`.
    Includes the size of both matrices and any additional memory overhead.
    Helps analyze the space complexity of the data structures.
    """
    for mat1, mat2 in matrices:
        size1 = sys.getsizeof(mat1)
        size2 = sys.getsizeof(mat2)
        print(f"Matrix size: {len(mat1)}x{len(mat1[0])}, Memory Usage: {size1 + size2} bytes")

if __name__ == "__main__":
    # Define test matrix sizes
    matrix_sizes = [10, 50, 100]

    # Generate random matrices for testing
    matrices = [(generate_matrix(size), generate_matrix(size)) for size in matrix_sizes]

    # Measure and print execution time
    print("Execution Time Analysis:")
    measure_execution_time(matrices)

    # Measure and print memory usage
    print("\nMemory Usage Analysis:")
    measure_memory_usage(matrices)
