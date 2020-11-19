from utils.utils import vertex_ways, tag_coordinates, matrix
from utils.vertex import Vertex


def get_inputs():
    (N, M) = tuple(map(int, input().split(' ')))
    for i in range(M):
        row = []
        for item in input():
            paths_count = None
            if len(row) == 0:
                paths_count = 1
                vertex_ways[(i, len(row))] = 1
            new_vertex = Vertex(i, len(row), item, paths_count)
            if not (item in tag_coordinates):
                tag_coordinates[item] = []
            tag_coordinates[item].append(new_vertex)
            row.append(new_vertex)
        matrix.append(row)
    return M, N
