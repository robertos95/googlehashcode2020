import sys
import numpy as np

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
        pass




if __name__ == "__main__":
    filepath = "../Practice Round - 2020/"
    filename = sys.argv[1]
    filepath = filepath + filename
    

    solution = Solution()
    requirements, data = solution.read(filepath)
    solution.compute(requirements, data)