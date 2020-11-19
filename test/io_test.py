import unittest
import utils.task_io as io
from contextlib import closing
from collections import defaultdict


class IoTest(unittest.TestCase):
    def test_reader(self):
        samples = ["3 3\naaa\nbac\ndef\n", "7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa",
                        "10 1\nabcdefahijk\n"]
        results = [[(3, 3), {'a': [(0, 0), (0, 1), (0, 2), (1, 1)], 'b': [(1, 0)], 'c': [(1, 2)], 'd': [(2, 0)], 'e': [(2, 1)], 'f':[(2, 2)]}], [(6, 7)], [(1, 10)]]
        for sample_index in range(len(samples)):
            corridor = []
            tag_coordinates = defaultdict(list)
            io.write_result("../io/test1.in", samples[sample_index])
            sizes = io.get_inputs(tag_coordinates, corridor, "../io/test1.in")
            self.assertEqual(sizes, results[sample_index][0])
        corridor = []
        tag_coordinates = defaultdict(list)
        io.write_result("../io/test1.in", samples[0])
        io.get_inputs(tag_coordinates, corridor, "../io/test1.in")
        self.assertEqual(tag_coordinates, results[0][1])


    def test_writer(self):
        samples = ["hello", 5, 41, "finally"]
        for sample in samples:
            io.write_result("../io/test1.out", sample)
            with closing(open("../io/test1.out", "r")) as input_file:
                self.assertEqual(input_file.readline(), str(sample))


if __name__ == '__main__':
    unittest.main()
