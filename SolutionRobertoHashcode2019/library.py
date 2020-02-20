class Library:
    def __init__(self, id, nr_of_books, signup_dur, shippable_books_per_day, books, max_score):
        self.id = id
        self.nr_of_books = nr_of_books
        self.signup_dur = signup_dur
        self.shippable_books_per_day = shippable_books_per_day
        self.books = books
        self.scanned_books = []
        self.max_score = max_score

    # Custom print
    def __str__(self):
        return str(self.__class__) + ": ID: " + str(self.id) + ';No of Books: ' + str(self.nr_of_books) + ';Signup Dur: ' +  str(self.signup_dur) + ';Shippable books per day: ' +  str(self.shippable_books_per_day) + ';Books: ' +  str(self.books)
