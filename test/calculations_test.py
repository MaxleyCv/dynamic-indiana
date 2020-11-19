import unittest
from vertex.vertex import Vertex
import algorithm.calculations as dynamic
from collections import defaultdict
import utils.task_io as io


class TestPathwayAlgorithms(unittest.TestCase):

    def test_adjacent(self):
        sample_vertex = Vertex(0, 0, 'a', None)
        sample_tag_coordinates = {'a': {(1, 2), (2, 3)}}
        self.assertEqual(
            dynamic.get_adjacent_vertexes(current_vertex=sample_vertex, tag_coordinates=sample_tag_coordinates),
            set())
        sample_vertex.coordinate = (1, 3)
        self.assertEqual(
            dynamic.get_adjacent_vertexes(current_vertex=sample_vertex, tag_coordinates=sample_tag_coordinates),
            {(1, 2)})
        sample_vertex.coordinate = (4, 4)
        self.assertEqual(
            dynamic.get_adjacent_vertexes(current_vertex=sample_vertex, tag_coordinates=sample_tag_coordinates),
            {(1, 2), (2, 3), (4, 3)})


    def test_findall(self):
        self.samples = ["3 3\naaa\nbac\ndef\n", "7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa",
                        "10 1\nabcdefahijk\n"]
        self.results = [5, 201684, 2]
        for sample_index in range(len(self.samples)):
            corridor = []
            tag_coordinates = defaultdict(list)
            io.write_result("../io/test1.in", self.samples[sample_index])
            row_count, column_count = io.get_inputs(tag_coordinates, corridor, "../io/test1.in")
            dynamic.get_number_of_ways(corridor[0][-1], tag_coordinates, corridor)
            if row_count != 1:
                dynamic.get_number_of_ways(corridor[-1][-1], tag_coordinates, corridor)
                result = corridor[0][-1].paths_count + corridor[-1][-1].paths_count
            else:
                result = corridor[0][-1].paths_count
            self.assertEqual(self.results[sample_index], result)


if __name__ == '__main__':
    unittest.main()
