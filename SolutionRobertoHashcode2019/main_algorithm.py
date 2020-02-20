import sys, os
from file_controller import *
from library import *

file_controller = FileController()

def main(sysargv):
    # Settings
    filepath = os.getcwd() + '\\'      # TODO: Set this to the filepath of input and output
    execute_from_cmd = False                    # TODO: Set to true to execute from command line
    input_delimiter = " "                       # TODO: CHANGE WITH CORRECT DELIMITER!!
    output_delimiter = ";"                      # TODO: CHANGE WITH CORRECT DELIMITER!!
    nr_iteration = 1                            # TODO: CHANGE THIS

    # Read input file
    if execute_from_cmd:
        input_filename = sysargv[1]
        output_filename = sysargv[2]
    else:
        input_filename = "a_example.txt"         # TODO: Modify input_filename if executing from pycharm
        output_filename = "a_example_out.txt"       # TODO: Modify input_filename if executing from pycharm
    input_filepath = filepath + input_filename
    output_filepath = filepath + output_filename
    input_data = file_controller.read(input_filepath, input_delimiter)

    line0 = input_data[0]
    nr_of_books = int(line0[0])
    nr_of_libraries = int(line0[1])
    nr_of_days = int(line0[2])

    books_score = input_data[1]

    libraries = []
    for i in range(nr_of_libraries):
        library_info = input_data[2*(i+1)]
        nr_of_books = library_info[0]
        signup_dur = library_info[1]
        shippable_books_per_day = library_info[1]
        books = input_data[2*(i+1)+1]

        libraries.append(Library(int(nr_of_books), int(signup_dur), int(shippable_books_per_day), books))

    # Debuginfo to test if input data works
    # print(input_data)                         # TODO: Uncomment this to test if input are read correctly
    #
    # Main algorithm & Write Output
    algo = MainAlgorithm(output_filepath, output_delimiter, libraries)
    # TODO: Uncomment this to make algorithm execute
    # algo.execute(nr_iteration)      # Result is outputted whenever best possible solution is found


class MainAlgorithm:
    def __init__(self, output_filepath, output_delimiter, input_data):
        self.output_filepath = output_filepath
        self.output_delimiter = output_delimiter
        self.input_data = input_data
        pass
        # Establish your input_data here
        # Input data is an array of array
        # E.g., self.nr_string = input_data[0][0]

    def execute(self, nr_iteration=1):
        best_solution_score = 0
        best_solution = []
        for cur_iteration_nr in range(0, nr_iteration):
            print("IterationNr", cur_iteration_nr)      # Default debuginfo
            cur_score, cur_solution = self.execute_iteration()

            if cur_score > best_solution_score or nr_iteration == 1:        # always output if nr iteration is 1
                best_solution_score = cur_score
                best_solution = cur_solution
                print("New Best Score:", best_solution_score, "Best Solution:", cur_solution)       # Default debuginfo
                array_to_write = [[2,3,4],[5,6,7]]        # TODO: Change this to correct way to output nested array to a file

                # Write Result
                file_controller.write(self.output_filepath, array_to_write, self.output_delimiter)

    def execute_iteration(self):        # TODO: Modify this code to your algorithm
        # Write your algorithm that is going to be executed every iteration here
        solution = self.input_data

        return 0, solution    # return solution score


if __name__ == '__main__':
    main(sys.argv)