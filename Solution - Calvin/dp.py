class Dp:
    def main(self, max_cap, nr_pizza_type, list_pizza):

        self.max_cap = max_cap
        self.nr_pizza_type = nr_pizza_type
        self.list_pizza = list_pizza

        # print(max_cap, nr_pizza_type, list_pizza)

        # Create Table T
        # Cell T[i,j] represents the max nr of slice in a problem with the first i pizza and capacity j
        self.max_i = nr_pizza_type
        self.max_j = max_cap
        self.table = []
        for i in range(self.max_i + 1):
            self.table.append([0] * (self.max_j + 1))

        # print(self.table)

        # Initialize
        # # t[0,j] = 0
        # self.table[0] = [0] * (self.max_j + 1)
        # # t[i,0] = 0
        # for i in range(1, self.max_i + 1):
        #     self.table[i][0] = 0

        # Fill in other cells
        for i in range(1, self.max_i + 1):
            # print("i", cur_i)
            # print(self.table)
            for j in range(1, self.max_j + 1):
                # print("j", cur_j)
                self.table[i][j] = self.calculate_value(i,j)


        # print(self.table)
        print("Pizza chosen:", self.get_chosen_pizza())
        print("Total Nr Slice", self.table[self.max_i][self.max_j])

    def calculate_value(self, i, j):
        if self.get_slice_of_pizza_nr(i) > j:
            value = self.table[i-1][j]
        else:
            value_not_taking_i = self.table[i-1][j]
            nr_slice_pizza_i = self.get_slice_of_pizza_nr(i)
            value_taking_i = nr_slice_pizza_i + self.table[i-1][j-nr_slice_pizza_i]
            value = max(value_taking_i, value_not_taking_i)
            # print(i, j, value_taking_i, nr_slice_pizza_i, self.table[i-1][j-nr_slice_pizza_i], value_not_taking_i)
        return value

    def get_slice_of_pizza_nr(self, i):
        # print("get", self.list_pizza[i-1])
        return self.list_pizza[i-1]

    def get_chosen_pizza(self):
        i = self.max_i
        j = self.max_j
        chosen_pizza = []
        while i != 0 and j!= 0:
            # print(i, j)
            if self.get_slice_of_pizza_nr(i) > j:
                i -= 1
            else:
                value_not_taking_i = self.table[i - 1][j]
                nr_slice_pizza_i = self.get_slice_of_pizza_nr(i)
                value_taking_i = nr_slice_pizza_i + self.table[i - 1][j - nr_slice_pizza_i]
                if value_taking_i > value_not_taking_i:
                    chosen_pizza.append(i-1)    # pizza i is pizza i-1
                    i -= 1
                    j -= nr_slice_pizza_i
                else:
                    i -= 1

        return chosen_pizza

if __name__ == '__main__':
    pass
    # Dp.main(17, )