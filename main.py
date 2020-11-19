from utils.calculations import *
from utils.access import get_inputs

if __name__ == '__main__':
    M, N = get_inputs()
    get_number_of_ways(matrix[0][-1])
    if M != 1:
        get_number_of_ways(matrix[-1][-1])
        print(vertex_ways.get((0, N - 1)) + vertex_ways.get((M - 1, N - 1)))
    else:
        print(vertex_ways[(0, N - 1)])