import algorithm.calculations as dynamic
import utils.task_io as io
from collections import defaultdict
import utils.utils as utils

if __name__ == '__main__':
    corridor = []
    tag_coordinates = defaultdict(list)
    dict_of_tagpaths = defaultdict(list)
    row_count, column_count = io.get_inputs(utils.INPUT_FILE, corridor)
    # if row count is greater than 0 there is definitely a right top cell and it is the same as down right
    dynamic.initialize_paths(corridor, column_count, row_count)
    if row_count != 1:
        io.write_result(utils.OUTPUT_FILE, corridor[0][-1].paths_count + corridor[-1][-1].paths_count)
    else:
        io.write_result(utils.OUTPUT_FILE, corridor[0][-1].paths_count)
