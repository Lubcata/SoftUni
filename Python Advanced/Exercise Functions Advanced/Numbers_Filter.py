def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "even":
            even_elements = [el for el in value if el % 2 == 0]
            result[key] = even_elements
        elif key == "odd":
            even_elements = [el for el in value if el % 2 != 0]
            result[key] = even_elements

    sorted_result = dict(sorted(result.items(), key=lambda item: -len(item[1])))
    return sorted_result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
