from utils.vertex import Vertex
from contextlib import closing


def get_inputs(tag_coordinates, map_of_vertexes, input_file_path):
    """
    Function to read statement from a file
    :parameter tag_coordinates: defaultdict containing symbol-(list of coordinates with this symbol)
    :parameter map_of_vertexes: list of rows of vertexes
    :parameter input_file_path: way to input file
    :return: count of rows and count of columns
    """
    with closing(open(input_file_path, "r")) as input_file:
        input_data = input_file.readlines()
    (column_count, row_count) = tuple(map(int, input_data.pop(0).rstrip('\n').split(' ')))
    # taking a new row of steps, we should use an index instead of taking each element because we need a coordinate
    for row_index in range(row_count):
        row = []
        # adding each symbol-vertex to the map_of_vertexes of vertexes
        for symbol in input_data.pop(0).rstrip('\n'):
            # only when the vertex is in the first column, we can start from it
            paths_count = None
            if len(row) == 0:
                paths_count = 1
            new_vertex = Vertex(row_index, len(row), symbol, paths_count)
            tag_coordinates[symbol].append(new_vertex.coordinate)
            row.append(new_vertex)
        map_of_vertexes.append(row)

    return row_count, column_count


def write_result(output_file_path: str, result):
    """
    Function to write a result to file
    :param output_file_path: path to an output file
    :param result: value to write
    """
    with closing(open(output_file_path, "w")) as output_file:
        output_file.write(str(result))
