
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_idx = 0
        self.inner_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_idx < len(self.list_of_list):
            current_list = self.list_of_list[self.outer_idx]

            if self.inner_idx < len(current_list):
                item = current_list[self.inner_idx]
                self.inner_idx += 1
                return item

            else:
                self.outer_idx += 1
                self.inner_idx = 0

        raise StopIteration


