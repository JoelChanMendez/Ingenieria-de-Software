import random

def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

import time

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time() 
    return end_time - start_time

import matplotlib.pyplot as plt

def plot_comparison(algorithms, sizes):
    for algorithm in algorithms:
        times = []
        for size in sizes:
            data = generate_random_data(size)
            time_taken = measure_time(algorithm, data.copy())
            times.append(time_taken)
        plt.plot(sizes, times, label=algorithm.__name__)

    plt.xlabel('Tamaño del conjunto de datos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    algorithms = [bubble_sort,]  # Agrega otros algoritmos de ordenamiento aquí
    dataset_sizes = [100, 500, 1000, 5000]  # Puedes ajustar según sea necesario
    plot_comparison(algorithms, dataset_sizes)
