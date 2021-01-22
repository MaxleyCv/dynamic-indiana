import unittest
from vertex.vertex import Vertex
import algorithm.calculations as dynamic
from collections import defaultdict
import utils.task_io as io


class TestPathwayAlgorithms(unittest.TestCase):

    def test_findall(self):
        self.samples = ["3 3\naaa\nbac\ndef\n", "7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa",
                        "10 1\nabcdefahij\n"]
        self.results = [5, 201684, 4]
        for sample_index in range(len(self.samples)):
            corridor = []
            io.write_result("../io/test1.in", self.samples[sample_index])
            row_count, column_count = io.get_inputs("../io/test1.in", corridor)
            dynamic.initialize_paths(corridor, column_count, row_count)
            result = corridor[0][-1].paths_count + corridor[-1][-1].paths_count
            self.assertEqual(self.results[sample_index], result)


if __name__ == '__main__':
    unittest.main()
