def age_assignment(*names, **kwargs):
    result = {}
    for name in names:
        for key, value in kwargs.items():
            if key in name:
                result[name] = value
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    return "\n".join(f"{name} is {age} years old." for name, age in sorted_result)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))