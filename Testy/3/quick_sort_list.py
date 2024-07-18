from Testy.helpers.validate_arg_type import validate_arg_type


@validate_arg_type(list)
def quick_sort_list(elements):
    if len(elements) in [0, 1]:
        return elements

    pivot = elements[0]

    left = [element for element in elements[1:] if element <= pivot]
    right = [element for element in elements[1:] if element > pivot]

    return quick_sort_list(left) + [pivot] + quick_sort_list(right)
