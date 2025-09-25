s_input = input("Введите строку: ")

def get_word_path(s):
    if len(s) % 2 == 0:
        return get_even(s)
    else:
        return get_odd(s)

def get_odd(s):
    middle_index = len(s) // 2
    return s[middle_index]

def get_even(s):
    middle_right = len(s) // 2
    middle_left = middle_right - 1
    result = s[middle_left] + s[middle_right]

    return result

print(get_word_path(s_input))