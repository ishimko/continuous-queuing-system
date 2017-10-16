def read_positive_float(name):
    return read_from_keyboard(name, float, lambda x: x > 0)

def read_from_keyboard(name, type_constructor, validator=lambda x: True):
    result = None
    valid = False
    while not valid:
        result = _try_convert(input('{}: '.format(name)), type_constructor)
        valid = result is not None and validator(result)
        if not valid:
            print('Invalid input')
    return result

def _try_convert(value, type_constructor):
    try:
        return type_constructor(value)
    except ValueError:
        return None
