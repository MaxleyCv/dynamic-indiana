class Vertex:
    def __init__(self, row, column, tag, paths_count):
        self.coordinate = (row, column)
        self.tag = tag
        self.paths_count = paths_count
