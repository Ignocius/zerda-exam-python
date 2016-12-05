# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].


def evry_second_element_from_list(data_list):
    if isinstance(data_list, list):
        return_list = []
        for index in range(len(data_list)):
            if data_list[index] % 2 == 0:
                return_list.append(data_list[index])
        return return_list
    else:
        raise TypeError

example = [1, 2, 3, 4, 5]
wrong_test_example = 1
print(evry_second_element_from_list(example))
print(evry_second_element_from_list(wrong_test_example))
