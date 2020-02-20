class Library:
    def __init__(self, nr_of_books, signup_dur, shippable_books_per_day, books):
        self.nr_of_books = nr_of_books
        self.signup_dur = signup_dur
        self.shippable_books_per_day = shippable_books_per_day
        self.books = books

    # Custom print
    def __str__(self):
        return str(self.__class__) + ": " + str(self.nr_of_books) + str(self.signup_dur) + str(self.shippable_books_per_day) + str(self.books)