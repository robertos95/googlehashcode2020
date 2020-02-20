import sys
import numpy as np

from dp import *
from recursive_dp import *


class Solution:
    def read(self, filepath):
        with open(filepath, "r") as f:
            firstline = f.readline()
            requirements = np.fromstring(firstline, dtype = np.int,  sep = ' ')

            otherlines = ""
            for line in f:
                otherlines = otherlines + line 
            
            data = np.fromstring(otherlines, dtype = np.int, sep = ' ')
            
        return requirements, data

    def write():
        pass

    def compute(self, requirements, data):
        # dp = Dp()
        dp = RecursiveDp()
        dp.main(requirements[0], requirements[1], data)
        dp.find_best_pizza_combination()

if __name__ == "__main__":
    filepath = "../Practice Round - 2020/"
    # filename = sys.argv[1]
    filename = "d_quite_big.in"
    # filename = "e_also_big.in"
    filepath = filepath + filename

    solution = Solution()
    requirements, data = solution.read(filepath)
    print(requirements, data)
    solution.compute(requirements, data)