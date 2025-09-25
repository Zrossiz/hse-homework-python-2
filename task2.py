def get_pairs(boys, girls):
    if len(boys) != len(girls):
        return "Кто-то может остаться без пары"
    
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)

    result = []

    for i, item in enumerate(sorted_boys):
        pair_string = ""

        pair_string = pair_string + sorted_boys[i]
        pair_string = pair_string + " и "
        pair_string = pair_string + sorted_girls[i]

        result.append(pair_string)

    return result

print(get_pairs(["Peter", "Alex", "John", "Arthur", "Richard"], ["Kate", "Liza", "Kira", "Emma", "Trisha"]))