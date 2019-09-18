class ParentA(object):
    DATA = [7, 8, 9]


class ParentB(object):
    DATA = [4, 5, 6]


class Transformer(ParentA, ParentB):

    def get_previous(self, current_index):
        '''
        Return the previous value in self.DATA. If there is no previous value,
        return 0.
        '''
        return self.DATA[current_index - 1]

    def transform(self):
        '''
        Transform a copy of self.DATA, such that each value is equal to the sum
        of the value and the previous number or 0.

        Example input: [7, 8, 9]
        Example output: [7, 15, 17]
        '''
        transformed_data = []

        for value, index in enumerate(self.DATA):
            transformed_value = sum(self.get_previous(index), value)
            transformed_data.append(transformed_value)

        return transformed_data
