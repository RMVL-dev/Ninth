def apply_all_func(int_list, *functions):
    dict_to_return = {}
    for func in functions:
        dict_to_return[func.__name__] = func(int_list)
    return dict_to_return


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
