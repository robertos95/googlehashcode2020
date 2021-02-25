class Car:
    def __init__(self, id, nr_of_streets_to_travel, streets_in_sequence):
        self.id = id
        self.nr_of_streets_to_travel = nr_of_streets_to_travel
        self.streets_in_sequence = streets_in_sequence

    # Custom print
    def __str__(self):
        return str(self.__class__) + ';ID: ' + str(self.id) + ';Nr of Streets to Travel: ' + str(self.nr_of_streets_to_travel) + ';Streets in Sequence: ' + str(self.streets_in_sequence)
