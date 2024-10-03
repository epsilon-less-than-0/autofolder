def string_to_int(value):
    if isinstance(value, list):
        # If it's a list, assume we want the first element
        return int(value[0])
    else:
        # If it's not a list, assume it's a string
        return int(value)

# Examples
# print(string_to_int('1'))        # Output: 1
# print(string_to_int(['1']))      # Output: 1