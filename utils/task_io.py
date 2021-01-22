from vertex.vertex import Vertex
from contextlib import closing
from collections import defaultdict
from copy import copy


def get_inputs(input_file_path, map_of_vertexes):
    """
    Function to read statement from a file
    :parameter tag_coordinates: defaultdict containing symbol-(list of coordinates with this symbol)
    :parameter map_of_vertexes: list of rows_count of vertexes
    :parameter input_file_path: way to input file
    :parameter dict_of_tagpaths: a dictionary that corresponds tag and appearance of tag in a column
    :return: count of rows_count and count of columns_count
    >>> get_inputs(defaultdict(list), [], "io/test1.in")
    (2, 2)
    """
    with closing(open(input_file_path, "r")) as input_file:
        input_data = input_file.readlines()
    column_count, row_count = map(int, input_data.pop(0).rstrip('\n').split(' '))
    # taking a new row of steps, we should use an index instead of taking each element because we need a coordinate
    for row_index in range(row_count):
        row = []
        # adding each symbol-vertex to the map_of_vertexes of vertexes
        for symbol in input_data.pop(0).rstrip('\n'):
            paths_count = 0
            # only when the vertex is in the first column, we can start from it
            if len(row) == 0:
                paths_count = 1
            # initialize vertex object here
            new_vertex = Vertex(symbol, paths_count)
            row.append(new_vertex)
        map_of_vertexes.append(row)

    return row_count, column_count


def write_result(output_file_path: str, result):
    """
    Function to write a result to file
    :param output_file_path: path to an output file
    :param result: value to write
    >>> write_result("../io/test1.out", 5)
    >>> open("../io/test1.out", 'r').read()
    '5'
    """
    with closing(open(output_file_path, "w")) as output_file:
        output_file.write(str(result))
