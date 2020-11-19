from utils.utils import *


def get_adjacent_vertexes(current_vertex):
    result = set()
    for vertex in tag_coordinates.get(current_vertex.tag):
        if vertex.coordinate[1] < current_vertex.coordinate[1]:
            result.add(vertex)
    if current_vertex.coordinate[1]:
        result.add(matrix[current_vertex.coordinate[0]][current_vertex.coordinate[1] - 1])
    return result


def get_number_of_ways(current):
    if not (current.coordinate in vertex_ways.keys()):
        vertex_ways[current.coordinate] = 0
    new_vertexes = get_adjacent_vertexes(current)
    for vertex in new_vertexes:
        if not (vertex.coordinate in vertex_ways.keys()):
            vertex_ways[vertex.coordinate] = 0
            get_number_of_ways(vertex)
        vertex_ways[current.coordinate] += vertex_ways.get(vertex.coordinate)