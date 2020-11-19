def get_adjacent_vertexes(current_vertex, tag_coordinates):
    """
    Function to find all possible connections to current vertex
    :param current_vertex: vertex to end at
    :param tag_coordinates: dictionary of symbol-(list of coordinates) dependency
    :return: set of coordinates of the vertexes from which it is possible to come to current
    """
    result = set()
    # taking all vertexes with the same tag that are positioned leftside from the current
    for vertex_coordinate in tag_coordinates[current_vertex.tag]:
        if vertex_coordinate[1] < current_vertex.coordinate[1]:
            result.add(vertex_coordinate)
    # if the column is not at the start we can also get from the left vertex
    if current_vertex.coordinate[1]:
        result.add((current_vertex.coordinate[0], current_vertex.coordinate[1] - 1))
    return result


def get_number_of_ways(current, tag_coordinates, map_of_corridor):
    """
    Main function that finds number of ways to reach current vertex
    :param current: Vertex object, current vertex
    :param tag_coordinates: dictionary: dependency between symbol and a list of coordinates of vertexes with it
    :param map_of_corridor: list of rows of the vertexes
    :return: number of pathways to reach the vertex from the leftmost column
    """
    # we should initialize the paths count before changing it
    if current.paths_count is None:
        current.paths_count = 0
    # getting all vertex coordinates from which it is possible to move to current
    new_vertexes = get_adjacent_vertexes(current, tag_coordinates)
    # we should add the pathways of all variants, whereas it is not stored we should calculate it
    for vertex_coordinate in new_vertexes:
        vertex = map_of_corridor[vertex_coordinate[0]][vertex_coordinate[1]]
        # if we do not know how many ways there are to reach the vertex we should find it
        if vertex.paths_count is None:
            get_number_of_ways(vertex, tag_coordinates, map_of_corridor)
        # for each already stored value we add it to the current one
        current.paths_count += vertex.paths_count
    return current.paths_count
