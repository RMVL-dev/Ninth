def is_prime(func):
    def check(*args, **kwargs):
        result_to_return = func(*args, **kwargs)
        is_prime_value = False
        i = 1
        while is_prime_value == False and i <= result_to_return:
            if result_to_return % i == 0 and i != 1 and i != result_to_return:
                is_prime_value = True
            i += 1
        if is_prime_value:
            print("Составное")
        else:
            print("Простое")
        return result_to_return

    return check


@is_prime
def sum_three(num1, num2, num3):
    result = num1 + num2 + num3
    return result


result = sum_three(2, 3, 6)
print(result)