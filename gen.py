import types


def flat_generator(list_of_lists):
    current_list = []
    for i in list_of_lists:
        for j in i:
            yield j
            current_list.append(j)
    return current_list

