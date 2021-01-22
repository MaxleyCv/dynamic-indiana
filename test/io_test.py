import unittest
import utils.task_io as io
from contextlib import closing


class IoTest(unittest.TestCase):
    def test_reader(self):
        samples = ["3 3\naaa\nbac\ndef\n", "7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa",
                   "10 1\nabcdefahijk\n"]
        results = [(3, 3), (6, 7), (1, 10)]
        for sample_index in range(len(samples)):
            corridor = []
            io.write_result("../io/test1.in", samples[sample_index])
            sizes = io.get_inputs("../io/test1.in", corridor)
            self.assertEqual(sizes, results[sample_index])
        io.write_result("../io/test1.in", samples[0])

    def test_writer(self):
        samples = ["hello", 5, 41, "finally"]
        for sample in samples:
            io.write_result("../io/test1.out", sample)
            with closing(open("../io/test1.out", "r")) as input_file:
                self.assertEqual(input_file.readline(), str(sample))


if __name__ == '__main__':
    unittest.main()
