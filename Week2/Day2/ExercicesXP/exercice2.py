my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]

def sum_numbers(my_list):
    total = 0

    for item in my_list:
        if isinstance(item, (int, float)):
            total += item

    return total

print(sum_numbers(my_list))
