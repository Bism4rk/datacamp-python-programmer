import time
import pytest_benchmark

def test_list(benchmark):
	# Add decorator here
    @benchmark
    def iterate_list():
		# Complete the loop here
        for i in [i for i in range(1000)]:
            pass

def test_set(benchmark):
	# Add decorator here
    @benchmark
    def iterate_set():
        # Complete the loop here
        for i in {i for i in range(1000)}:
            pass

'''
O código acima demonstra como criar testes de desempenho para iterações em listas e conjuntos usando o pytest-benchmark. Isso permite que os desenvolvedores comparem o desempenho de diferentes estruturas de dados em suas aplicações. Ele ajuda a identificar qual estrutura de dados é mais eficiente para um determinado caso de uso.
'''