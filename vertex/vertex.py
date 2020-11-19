class Vertex:
    """
    Class for one vertex of the corridor
    coordinate: tuple of (row, column)
    tag: symbol of the vertex
    paths_count: number of possible paths to the vertex, if not initialized it is None
    """
    def __init__(self, row, column, tag, paths_count):
        self.coordinate = (row, column)
        self.tag = tag
        self.paths_count = paths_count
