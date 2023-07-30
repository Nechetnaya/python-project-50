def stylish_(data):
    return data


def stylish(data, key=None, gap=''):
    if data == {}:
        return "{}"
    result = ''
    if type(data) is not dict:
        result += decorate_simple_data(data)
    elif has_value(data):
        result += decorate_value_dict(data, key, gap)
    elif is_simple_dict(data):
        result += decorate_dict(data, gap)
    else:
        result += '{'
        for key in data:
            result += decorate_multy_dict(data[key], key, gap)
        result += f'\n{gap}' + '}'
    return str(result)


def is_simple_dict(data):
    for key in data:
        if type(data[key]) is dict:
            return False
    return True


def has_value(data):
    return True if "value1" in data else False


def decorate_dict(data, gap):
    result = '{\n'
    for key in data:
        result += f'{gap + "    "}{key}: {data[key]}\n'
    result += f'{gap}' + '}'
    return result


def decorate_simple_data(data):
    if data is None:
        return 'null'
    elif type(data) == bool:
        return str(data).lower()
    else:
        return str(data)


def decorate_multy_dict(data, key, gap):
    if type(data) is dict and "value1" in data:
        return stylish(data, key, gap=gap + '  ')
    else:
        return f'\n{gap + "    "}{key}: '\
               f'{stylish(data, key, gap=gap + "    ")}'


def decorate_value_dict(data, key, gap):
    result = ''
    if data["act"] == '+-':
        act1, act2 = give_act(data)
        val1, val2 = give_value(data)
        result += f'\n{gap}{act1}{key}: {stylish(val1, gap=gap + "  ")}'
        result += f'\n{gap}{act2}{key}: {stylish(val2, gap=gap + "  ")}'
    else:
        result += f'\n{gap}{give_act(data)}{key}: ' \
                  f'{stylish(give_value(data), gap=gap + "  ")}'
    return result


def give_act(data):
    if data["act"] == '+':
        return '+ '
    elif data["act"] == '-':
        return '- '
    elif data["act"] == '':
        return '  '
    elif data["act"] == '+-':
        acts = ('- ', '+ ')
        return acts


def give_value(data):
    if data["act"] == '+':
        return data["value2"]
    elif data["act"] == '-':
        return data["value1"]
    elif data["act"] == '':
        return data["value1"]
    elif data["act"] == '+-':
        acts = (data["value1"], data["value2"])
        return acts
