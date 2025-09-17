import time
import pytest_benchmark

def create_list():
    return [i for i in range(1000)]
def create_set():
    return set([i for i in range(1000)])
def find(it, el=50):
    return el in it

# Write the performance test for a list
def test_list(benchmark, it=create_list()):
    benchmark(find, it=create_list())

# Write the performance test for a set
def test_set(benchmark, it=create_set()):
    benchmark(find, it=create_set())

'''
O código acima demonstra como usar o pytest-benchmark para medir o desempenho de operações de busca em diferentes estruturas de dados, como listas e conjuntos. Ele permite que os desenvolvedores identifiquem gargalos de desempenho e otimizem seu código de forma eficaz.
'''