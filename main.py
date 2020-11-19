import algorithm.calculations as dynamic
import utils.task_io as io
from collections import defaultdict
import utils.utils as utils

if __name__ == '__main__':
    corridor = []
    tag_coordinates = defaultdict(list)
    row_count, column_count = io.get_inputs(tag_coordinates, corridor, utils.INPUT_FILE)
    # if row count is greater than 0 there is definitely a right top cell
    dynamic.get_number_of_ways(corridor[0][-1], tag_coordinates, corridor)
    if row_count != 1:
        dynamic.get_number_of_ways(corridor[-1][-1], tag_coordinates, corridor)
        io.write_result(utils.OUTPUT_FILE, corridor[0][-1].paths_count + corridor[-1][-1].paths_count)
    else:
        io.write_result(utils.OUTPUT_FILE, corridor[0][-1].paths_count)
