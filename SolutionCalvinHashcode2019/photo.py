class Photo:
    def __init__(self, index, orientation, nr_of_tags, tags):
        self.index = index
        self.orientation = orientation
        self.nr_of_tags = nr_of_tags
        self.tags = set(tags)

    # Custom print
    def __str__(self):
        return str(self.__class__) + ": " + self.index + str(self.orientation) + str(self.nr_of_tags) + str(self.tags)

    def combineVertical(self, photo2):
        self.index = self.index + ' ' + photo2.index
        self.orientation = '2V'
        self.tags = self.tags | photo2.tags
        self.nr_of_tags = len(self.tags)
        # print("Cal", self.nr_of_tags)
        return self