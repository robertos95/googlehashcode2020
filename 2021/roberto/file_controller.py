# DO NOT CHANGE THIS CODE

class FileController:
    def read(self, filepath, delimiter):
        result = []
        with open(filepath, "r") as f:
            for line in f:
                cur_line_array = []
                for string in line.split(delimiter):
                    cur_line_array.append(string.strip())
                result.append(cur_line_array)

        return result

    def write(self, filepath, content, delimiter_within_same_line):
        with open(filepath, "w") as f:
            for content_line in content:
                f.write(delimiter_within_same_line.join(str(x) for x in content_line) + "\n")

if __name__ == "__main__":
    # Test read file
    pass