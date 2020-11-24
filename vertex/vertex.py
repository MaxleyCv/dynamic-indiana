class Vertex:
    """
    Class for one vertex of the corridor
    tag: symbol of the vertex
    paths_count: number of possible paths to the vertex, if not initialized it is None
    """
    def __init__(self, tag, paths_count):
        self.tag = tag
        self.paths_count = paths_count
