def concatenate(*args, **kwargs):

    concatenate_result = "".join(args)

    for key in kwargs:
        if key in concatenate_result:
            concatenate_result = concatenate_result.replace(key, kwargs[key])

    return concatenate_result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
