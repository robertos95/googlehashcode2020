import sys, os, random, copy
from file_controller import *
from library import *

file_controller = FileController()

def main(sysargv):
    # Settings
    filepath = os.getcwd() + '\\'      # TODO: Set this to the filepath of input and output
    execute_from_cmd = False                    # TODO: Set to true to execute from command line
    input_delimiter = " "                       # TODO: CHANGE WITH CORRECT DELIMITER!!
    output_delimiter = ""                      # TODO: CHANGE WITH CORRECT DELIMITER!!
    nr_iteration = 100                            # TODO: CHANGE THIS

    # Read input file
    if execute_from_cmd:
        input_filename = sysargv[1]
        output_filename = sysargv[2]
    else:
        # input_filename = "a_example.txt"         # TODO: Modify input_filename if executing from pycharm
        # output_filename = "a_example_out.txt"       # TODO: Modify input_filename if executing from pycharm

        # input_filename = "b_read_on.txt"
        # output_filename = "b_read_on_out.txt"

        # input_filename = "c_incunabula.txt"
        # output_filename = "c_incunabula_out.txt"

        # input_filename = "d_tough_choices.txt"
        # output_filename = "d_tough_choices_out.txt"

        # input_filename = "e_so_many_books.txt"
        # output_filename = "e_so_many_books_out.txt"

        input_filename = "f_libraries_of_the_world.txt"
        output_filename = "f_libraries_of_the_world_out.txt"
    input_filepath = filepath + input_filename
    output_filepath = filepath + output_filename
    input_data = file_controller.read(input_filepath, input_delimiter)

    line0 = input_data[0]
    nr_of_books = int(line0[0])
    nr_of_libraries = int(line0[1])
    nr_of_days = int(line0[2])

    books_score = [int(i) for i in input_data[1]]
    libraries = []
    for i in range(nr_of_libraries):
        library_info = input_data[2*(i+1)]
        nr_of_books = library_info[0]
        signup_dur = library_info[1]
        shippable_books_per_day = library_info[2]
        books = [int(x) for x in input_data[2*(i+1)+1]]
        books = sorted(books, key=lambda x: books_score[x])
        max_score = 0
        for book in books:
            max_score += int(books_score[book])
        libraries.append(Library(int(i), int(nr_of_books), int(signup_dur), int(shippable_books_per_day), books, max_score))

    # for l in libraries:
    #     print(l)
    # Debuginfo to test if input data works
    # print(input_data)                         # TODO: Uncomment this to test if input are read correctly
    #
    # Main algorithm & Write Output
    algo = MainAlgorithm(output_filepath, output_delimiter, libraries)
    # TODO: Uncomment this to make algorithm execute
    algo.execute(nr_of_days, books_score, nr_iteration)      # Result is outputted whenever best possible solution is found


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
            cur_score, cur_solution = self.execute_iteration(nr_of_days, books_score)

            if cur_score > best_solution_score or nr_iteration == 1:        # always output if nr iteration is 1
                best_solution_score = cur_score
                best_solution = cur_solution
                print("New Best Score:", best_solution_score, "Best Solution:", cur_solution)       # Default debuginfo
                array_to_write = []
                array_to_write.append(str(len(best_solution)))
                for l in best_solution:
                    scanned_books = l.scanned_books
                    array_to_write.append(str(l.id) + ' ' + str(len(scanned_books)) + '\n' + ' '.join(str(x) for x in scanned_books))

                # Write Result
                file_controller.write(self.output_filepath, array_to_write, self.output_delimiter)

    def execute_iteration(self, nr_of_days, books_score):        # TODO: Modify this code to your algorithm
        # self.input_data = sorted(sorted(self.input_data, key=lambda x: (x.signup_dur * x.nr_of_books/x.max_score)),
        #                          key=lambda x: x.max_score, reverse=True)
        libraries = copy.deepcopy(self.input_data)
        libraries = sorted(libraries, key=lambda x: x.max_score / (x.signup_dur + x.shippable_books_per_day), reverse=True)
        processed_books = {}
        remaining_days = nr_of_days
        best_score = 0
        out_libraries = []
        i = 0
        nr_of_libs = len(libraries)
        while libraries and i < nr_of_libs:
            i += 1
            is_random = random.randint(1,10) >= 8
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