import sys
import numpy as np


class Solution:
    def read(self, filepath, delimiter=" "):
        result = []
        with open(filepath, "r") as f:
            for line in f:
                cur_line_array = []
                for string in line.split(delimiter):
                    cur_line_array.append(string.strip())
                result.append(cur_line_array)

        return result

    def write(self, filepath, content, delimiter_within_same_line=" "):
        with open(filepath, "w") as f:
            for content_line in content:
                f.write(delimiter_within_same_line.join(content_line) + "\n")

    def compute(self, input_data):
        # Call your class here
        return input_data


if __name__ == "__main__":
    filepath = "../Practice Round - 2020/"

    # Read input file
    execute_from_cmd = False        # Set to true to execute from command line
    if execute_from_cmd:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    else:
        input_filename = "a_example.in"
        output_filename = "a_example.out"

    input_filepath = filepath + input_filename
    output_filepath = filepath + output_filename
    solution = Solution()
    input_delimiter = " "   # CHANGE WITH CORRECT DELIMITER!!
    input_data = solution.read(input_filepath, input_delimiter)

    # Main algorithm
    output_data = solution.compute(input_data)

    # Write Result
    output_delimiter = ";"   # CHANGE WITH CORRECT DELIMITER!!
    solution.write(output_filepath, output_data, output_delimiter)