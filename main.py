s_input = input("Введите строку: ")

def print_word_path(s):
    if len(s) % 2 == 0:
        return print_even(s)
    else:
        return print_odd(s)

def print_odd(s):
    middle_index = len(s) // 2
    return s[middle_index]

def print_even(s):
    middle_right = len(s) // 2
    middle_left = middle_right - 1
    result = s[middle_left] + s[middle_right]

    return result

print(print_word_path(s_input))