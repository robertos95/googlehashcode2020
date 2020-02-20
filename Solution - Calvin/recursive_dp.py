class RecursiveDp:
    def main(self, max_cap, nr_pizza_type, list_pizza):
        self.max_cap = max_cap
        self.nr_pizza_type = nr_pizza_type
        self.list_pizza = list_pizza
        self.solution_ht = dict()       # hashtable inside hashtable
        self.max_i = nr_pizza_type
        self.max_j = max_cap

    def find_best_pizza_combination(self):
        self.get_value_in_table(self.max_i, self.max_j)
        # print(self.table)
        print("Pizza chosen:", self.get_chosen_pizza())
        print("Total Nr Slice", self.table[self.max_i][self.max_j])

    def get_value_in_table(self, i, j):
        # Base Case 1
        if i == 0 or j == 0:
            return 0

        # Base Case 2
        cur_pizza_nr = self.get_slice_of_pizza_nr(i)
        if cur_pizza_nr == j:
            return cur_pizza_nr

        # Check Hash Table for existing solution
        if i not in self.solution_ht:
            self.solution_ht[i] = dict()
        cur_ht = self.solution_ht[i]

        if j in cur_ht:
            return cur_ht[j]
        else:
            cur_ht[j] = self.calculate_value(i,j)

    def calculate_value(self, i, j):
        if self.get_slice_of_pizza_nr(i) > j:
            value = self.get_value_in_table(i - 1, j)
        else:
            value_not_taking_i = self.get_value_in_table(i - 1, j)
            nr_slice_pizza_i = self.get_slice_of_pizza_nr(i)
            value_taking_i = nr_slice_pizza_i + self.get_value_in_table(i - 1, j - nr_slice_pizza_i)
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
        while i != 0 and j != 0:
            # print(i, j)
            if self.get_slice_of_pizza_nr(i) > j:
                i -= 1
            else:
                value_not_taking_i = self.get_value_in_table(i - 1, j)
                nr_slice_pizza_i = self.get_slice_of_pizza_nr(i)
                value_taking_i = nr_slice_pizza_i + self.get_value_in_table(i - 1, j - nr_slice_pizza_i)
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