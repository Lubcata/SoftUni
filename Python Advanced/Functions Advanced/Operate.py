from functools import reduce


def operate(operator, *nums):
    # result = {
    #     "+": reduce(lambda x, y: x + y, nums),
    #     "-": reduce(lambda x, y: x - y, nums),
    #     "*": reduce(lambda x, y: x * y, nums),
    #     "/": reduce(lambda x, y: x / y, nums),
    # }

    return reduce(lambda x, y: eval(f"{x}{operator}{y}"), nums)


print(operate("*", 3, 4))
