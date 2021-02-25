import sys
import os
import random
import copy
from file_controller import *
from street import *
from car import *

file_controller = FileController()


def main(sysargv):
    # Settings
    # TODO: Set this to the filepath of input and output
    input_filepath = os.path.join(os.path.dirname(os.getcwd()), 'files/')
    # TODO: Set this to the filepath of input and output
    output_filepath = os.getcwd() + '/'
    # TODO: Set to true to execute from command line
    execute_from_cmd = False
    input_delimiter = " "                       # TODO: CHANGE WITH CORRECT DELIMITER!!
    output_delimiter = ""                      # TODO: CHANGE WITH CORRECT DELIMITER!!
    # nr_iteration = 1000                            # TODO: CHANGE THIS

    # Read input file
    if execute_from_cmd:
        input_filename = sysargv[1]
        output_filename = sysargv[2]
    else:
        input_filename = "a.txt"
        output_filename = "a_an_example_out.txt"

        # input_filename = "b.txt"
        # output_filename = "b_by_the_ocean_out.txt"

        # input_filename = "c.txt"
        # output_filename = "c_checkmate.txt"

        # input_filename = "d.txt"
        # output_filename = "d_daily_commute.txt"

        # input_filename = "e.txt"
        # output_filename = "e_Etoile.txt"

        # input_filename = "f.txt"
        # output_filename = "f_forever_jammed.txt"
    input_filepath = input_filepath + input_filename
    output_filepath = output_filepath + output_filename
    input_data = file_controller.read(input_filepath, input_delimiter)

    line0 = input_data[0]
    simulation_duration = int(line0[0])
    nr_of_intersections = int(line0[1])
    nr_of_streets = int(line0[2])
    nr_of_cars = int(line0[3])
    bonus_point_per_car_within_time = int(line0[4])

    streets = []
    for i in range(nr_of_streets):
        street_info = input_data[i+1]
        intersection_start = street_info[0]
        intersection_end = street_info[1]
        street_name = street_info[2]
        travel_duration_in_sec = street_info[3]
        streets.append(Street(int(intersection_start), int(
            intersection_end), street_name, int(travel_duration_in_sec)))

    for s in streets:
        print(s)

    cars = []
    for i in range(nr_of_cars):
        car_info = input_data[i+nr_of_streets+1]
        car_id = 'Car_' + str(i + 1)
        nr_of_streets_to_travel = car_info[0]
        streets_in_sequence = car_info[1:]
        cars.append(
            Car(car_id, int(nr_of_streets_to_travel), streets_in_sequence))

    for c in cars:
        print(c)
    # Debuginfo to test if input data works
    # TODO: Uncomment this to test if input are read correctly
    # print(input_data)
    #
    # Main algorithm & Write Output
    # algo = MainAlgorithm(output_filepath, output_delimiter, libraries)
    # TODO: Uncomment this to make algorithm execute
    # algo.execute(nr_of_days, books_score, nr_iteration)      # Result is outputted whenever best possible solution is found


class MainAlgorithm:
    def __init__(self, output_filepath, output_delimiter, input_data):
        self.output_filepath = output_filepath
        self.output_delimiter = output_delimiter
        self.input_data = input_data
        pass
        # Establish your input_data here
        # Input data is an array of array
        # E.g., self.nr_string = input_data[0][0]

    def execute(self,  nr_of_days, books_score, nr_iteration=1):
        best_solution_score = 0
        best_solution = []
        for cur_iteration_nr in range(0, nr_iteration):
            print("IterationNr", cur_iteration_nr)      # Default debuginfo
            cur_score, cur_solution = self.execute_iteration(
                nr_of_days, books_score)

            if cur_score > best_solution_score or nr_iteration == 1:        # always output if nr iteration is 1
                best_solution_score = cur_score
                best_solution = cur_solution
                print("New Best Score:", best_solution_score,
                      "Best Solution:", cur_solution)       # Default debuginfo
                array_to_write = []
                array_to_write.append(str(len(best_solution)))
                for l in best_solution:
                    scanned_books = l.scanned_books
                    array_to_write.append(str(
                        l.id) + ' ' + str(len(scanned_books)) + '\n' + ' '.join(str(x) for x in scanned_books))

                # Write Result
                file_controller.write(
                    self.output_filepath, array_to_write, self.output_delimiter)

    # TODO: Modify this code to your algorithm
    def execute_iteration(self, nr_of_days, books_score):
        # self.input_data = sorted(sorted(self.input_data, key=lambda x: (x.signup_dur * x.nr_of_books/x.max_score)),
        #                          key=lambda x: x.max_score, reverse=True)
        libraries = copy.deepcopy(self.input_data)
        sorter = random.randint(1, 12)
        if sorter < 3:
            libraries = sorted(libraries, key=lambda x: x.max_score /
                               (x.signup_dur + x.shippable_books_per_day), reverse=True)
        elif sorter < 6:
            libraries = sorted(
                libraries, key=lambda x: x.shippable_books_per_day, reverse=True)
        elif sorter < 9:
            libraries = sorted(
                libraries, key=lambda x: x.signup_dur, reverse=True)
        else:
            libraries = sorted(
                libraries, key=lambda x: x.max_score, reverse=True)
        processed_books = {}
        remaining_days = nr_of_days
        best_score = 0
        out_libraries = []
        i = 0
        nr_of_libs = len(libraries)
        while libraries and i < nr_of_libs:
            i += 1
            is_random = random.randint(1, 10) >= 8
            if is_random:
                library = libraries.pop(random.randint(0, len(libraries) - 1))
            else:
                library = libraries.pop(0)
            max_books_daily = library.shippable_books_per_day
            remaining_days = remaining_days - library.signup_dur
            if(remaining_days < 0):
                remaining_days += library.signup_dur
                continue
            books = library.books.copy()
            k = 0
            while books and k < remaining_days * max_books_daily:
                book = books.pop()
                # print('mm', book)
                # print(3 in processed_books)
                if book not in processed_books:
                    processed_books[book] = True
                    library.scanned_books.append(book)
                    best_score += books_score[book]
                    # print('qqqqq', best_score)
                k += 1
            if library.scanned_books:
                out_libraries.append(library)
            else:
                remaining_days += library.signup_dur

        return best_score, out_libraries    # return solution score


if __name__ == '__main__':
    main(sys.argv)
