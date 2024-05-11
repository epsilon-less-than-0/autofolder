def are_dict_values_same_up_to_cyclic_order(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    # Check each key-value pair in dict1
    for key, value1 in dict1.items():
        # Check if the corresponding key exists in dict2
        if key not in dict2:
            return False

        value2 = dict2[key]

        # Check if the values are lists
        if not isinstance(value1, list) or not isinstance(value2, list):
            return False

        # Check if the lists are the same up to cyclic order
        if not are_lists_same_up_to_cyclic_order(value1, value2):
            return False

    return True


def are_lists_same_up_to_cyclic_order(list1, list2):
    if len(list1) != len(list2):
        return False

    # Create all cyclic permutations of list1
    n = len(list1)
    for i in range(n):
        if all(list1[(j + i) % n] == list2[j] for j in range(n)):
            return True
    return False


# Example usage
# dict1 = {'a': [1, 2, 3, 4, 5], 'b': [4, 5, 1, 2, 3]}
# dict2 = {'a': [4, 5, 1, 2, 3], 'b': [1, 2, 3, 4, 5]}
# print(are_dict_values_same_up_to_cyclic_order(dict1, dict2))  # Output: True

# dict3 = {'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]}
# dict4 = {'a': [1, 3, 4, 5, 2], 'b': [1, 2, 3, 4, 5]}
# print(are_dict_values_same_up_to_cyclic_order(dict3, dict4))  # Output: False
