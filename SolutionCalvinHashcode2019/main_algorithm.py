import sys
import random
import copy

from file_controller import *
from photo import *

file_controller = FileController()

def main(sysargv):
    filepath = "../SolutionCalvinHashcode2019/"

    # Settings
    execute_from_cmd = False    # TODO: Set to true to execute from command line
    input_delimiter = " "       # TODO: CHANGE WITH CORRECT DELIMITER!!
    output_delimiter = ";"      # TODO: CHANGE WITH CORRECT DELIMITER!!
    nr_iteration = 1000            # TODO: CHANGE THIS

    # Read input file
    if execute_from_cmd:
        input_filename = sysargv[1]
        output_filename = sysargv[2]
    else:
        # input_filename = "a_example.txt"
        input_filename = "c_memorable_moments.txt"         # TODO: Modify input_filename if executing from pycharm  #1709 # 1512
        # input_filename = "b_lovely_landscapes.txt"         # TODO: Modify input_filename if executing from pycharm #204k #206136
        output_filename = "a_example_out.txt"       # TODO: Modify input_filename if executing from pycharm
    input_filepath = filepath + input_filename
    output_filepath = filepath + output_filename
    input_data = file_controller.read(input_filepath, input_delimiter)
    nr_of_photos = int(input_data[0][0])
    photos = []
    for i in range(nr_of_photos):
        photo = input_data[i+1]
        orientation = photo[0]
        nr_of_tags = photo[1]
        tags = photo[2:]

        photos.append(Photo(str(i), orientation, int(nr_of_tags), tags))
        # print('i: ', i+1, ', o: ', orientation, ', nr_of_tags: ', nr_of_tags, ', tags: ', tags)
    # print(photos)

    # Main algorithm & Write Output
    algo = MainAlgorithm(output_filepath, output_delimiter, photos)
    algo.execute(nr_iteration)      # Result is outputted whenever best possible solution is found


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
            self.iteration_nr = nr_iteration
            print("IterationNr", cur_iteration_nr)      # Default debuginfo
            cur_score, cur_solution = self.execute_iteration()
            # print(cur_score)

            if cur_score > best_solution_score or nr_iteration == 1:        # always output if nr iteration is 1
                best_solution_score = cur_score
                best_solution = cur_solution
                print("New Best Score:", best_solution_score, "Best Solution:", cur_solution)       # Default debuginfo
                array_to_write = [[2,3,4],[5,6,7]]        # TODO: Change this to correct way to output nested array to a file

                # Write Result
                file_controller.write(self.output_filepath, array_to_write, self.output_delimiter)

    def execute_iteration(self):        # TODO: Modify this code to your algorithm
        # Write your algorithm that is going to be executed every iteration here
        all_photos = copy.deepcopy(self.input_data)

        # for i in all_photos:
        #     print(i)

        # print("LEN", len(all_photos))
        ready_to_use_photos = [p for p in all_photos if p.orientation == 'H']
        ver_photos = [p for p in all_photos if p.orientation == 'V']

        # ver_photos = self.combine_vertical_photos(ver_photos)
        ver_photos = self.random_combine_vertical_photos(ver_photos)
        ready_to_use_photos += ver_photos
        # print("LEN2", len(ready_to_use_photos))


        score, result = self.combine_slides(ready_to_use_photos)
        # pass
        return score, result    # return solution score

    def combine_vertical_photos(self, ver_photos):
        # Combine with the least common nr of tags
        result = []
        ver_photos.sort(key=lambda x: x.nr_of_tags, reverse=True)
        for i in range(len(ver_photos) // 2):
            result.append(ver_photos.pop().combineVertical(ver_photos.pop(0)))

        return result

    def random_combine_vertical_photos(self, ver_photos):
        result = []
        while len(ver_photos) > 1:
            int1 = random.randint(0, len(ver_photos)-1)
            photo1 = ver_photos.pop(int1)
            int2 = random.randint(0, len(ver_photos)-1)
            photo2 = ver_photos.pop(int2)
            result.append(photo1.combineVertical(photo2))

        return result

    def combine_slides(self, photos):
        result = []
        score = 0
        # print(photos)
        photos.sort(key=lambda x: x.nr_of_tags, reverse=True)
        # add the first photo
        result.append(photos.pop(0))
        for i in range(len(photos)):
            best_local_score = 0
            best_photo_index = None
            local_friend_found = False
            for j in range(len(photos)):
                p2 = photos[j]
                cur_score = self.calculate_score(result[-1], p2)
                if cur_score > best_local_score:
                    best_local_score = cur_score
                    best_photo_index = j
                    if best_local_score == p2.nr_of_tags // 2:
                    # if best_local_score == 3:
                        local_friend_found = True
                        result.append(photos.pop(j))
                        break
            if not local_friend_found:
                if best_photo_index is None:
                    result.append(photos.pop(0))
                else:
                    result.append(photos.pop(best_photo_index))

            score += best_local_score
            # print(score)

        return score, result

    def calculate_score(self, photo1, photo2):
        common_tags_len = len(photo1.tags & photo2.tags)
        score = min(photo1.nr_of_tags - common_tags_len, photo2.nr_of_tags - common_tags_len, common_tags_len)

        return score




if __name__ == '__main__':
    main(sys.argv)