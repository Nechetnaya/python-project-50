import json


def stylish_(data):
    return data


def stylish(data, key=None, gap=''):
    if data == {}:
        return "{}"
    result = ''
    if type(data) is not dict:
        if data is None:
            result += 'null'
        else:
            result += str(data).lower() if type(data) == bool else str(data)
    else:
        if has_value(data):
            if data["act"] == '+-':
                act1, act2 = give_act(data)
                val1, val2 = give_value(data)
                result += f'\n{gap}{act1}{key}: {stylish(val1, gap=gap+"  ")}'
                result += f'\n{gap}{act2}{key}: {stylish(val2, gap=gap+"  ")}'
            else:
                result += f'\n{gap}{give_act(data)}{key}: {stylish(give_value(data), gap=gap+"  ")}'
        else:
            if is_simple_dict(data):
                result += decorate_dict(data, gap)
            else:
                result += '{'
                for key in data:
                    if type(data[key]) is dict and "value1" in data[key]:
                        result += stylish(data[key], key, gap=gap+'  ')
                    else:
                        result += f'\n{gap + "    "}{key}: {stylish(data[key], key, gap=gap+"    ")}'
                result += f'\n{gap}' + '}'
    return str(result)


def is_simple_dict(data):
    for key in data:
        if type(data[key]) is dict:
            return False
    return True


def has_value(data):
    return True if "value1" in data else False


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


def decorate_dict(data, gap):
    result = '{\n'
    for key in data:
        result += f'{gap + "    "}{key}: {data[key]}\n'
    result += f'{gap}' + '}'
    return result
