def clamp_numbers(*args, **kwargs):
    result = []
    for i in args:
        if kwargs.get('low') or kwargs.get('high'):
            if i <= kwargs.get('low'):
                result.append(kwargs.get('low'))
            elif i >= kwargs.get('high'):
                result.append(kwargs.get('high'))
            else:
                result.append(i)
        else:
            result.append(i)
    return result

print(clamp_numbers(-5, 0, 10, 20, low = 0, high = 15))