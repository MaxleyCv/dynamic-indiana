from  collections import defaultdict


def initialize_paths(map_of_corridor, columns_count, rows_count):
    """
    Function to initialize all the paths to each vertex in map of corridor
    :param map_of_corridor: matrix with Vertex objects
    :param columns_count: number of columns
    :param rows_count: number of rows
    >>> initialize_paths([], 0, 0)
    """
    # dictionary to store all connections to the left
    same_tags_paths_leftside = defaultdict(int)

    # literally running through each column
    for column in range(columns_count):
        # dictionary to store all values that should be added to next tags
        additional = defaultdict(int)
        for row in range(rows_count):
            # adding of left adjacent element
            if column > 0:
                # we should add the adjacent element only whereas it has another tag
                # otherwise it will be counted in the next section
                if map_of_corridor[row][column - 1].tag != map_of_corridor[row][column].tag:
                    map_of_corridor[row][column].paths_count += map_of_corridor[row][column - 1].paths_count
            # initializing basic value of tag paths (leftmost appearance of the tag)
            if not map_of_corridor[row][column].tag in same_tags_paths_leftside:
                same_tags_paths_leftside[map_of_corridor[row][column].tag] = 0
            # adding all the paths from the tags to the left (we can come from each of them)
            map_of_corridor[row][column].paths_count += same_tags_paths_leftside.get(map_of_corridor[row][column].tag)
            # adding to the tags every vertex for next generations
            additional[map_of_corridor[row][column].tag] += map_of_corridor[row][column].paths_count
        # updating the tags' paths
        for key in additional:
            same_tags_paths_leftside[key] += additional[key]
