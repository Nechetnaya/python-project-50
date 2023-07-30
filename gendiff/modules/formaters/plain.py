def plain(data, path_):
    result = ''
    if "value1" not in data:
        for key in data:
            result += plain(data[key], path_=f'{path_}.{key}')
    elif data['act'] == "+":
        result += f'Property {decorate_path(path_)} was added with value: ' \
                  f'{decorate_value(data["value2"])}\n'
    elif data['act'] == "-":
        result += f'Property {decorate_path(path_)} was removed\n'
    elif data['act'] == "+-":
        result += f'Property {decorate_path(path_)} was updated. '\
                  f'From {decorate_value(data["value1"])} '\
                  f'to {decorate_value(data["value2"])}\n'
    elif data['act'] == "" and is_dict_with_value(data['value1']):
        result += plain(data['value1'], path_)
    return result


def decorate_value(value):
    if type(value) is not dict:
        return decorate_simple_data(value)
    return '[complex value]'


def decorate_simple_data(data):
    if data is None:
        return 'null'
    elif type(data) == bool:
        return str(data).lower()
    else:
        return f"'{str(data)}'"


def decorate_path(path_):
    return f"'{path_[1:]}'"


def is_dict_with_value(data):
    if type(data) is dict:
        for key in data:
            if "value1" in data[key]:
                return True
    return False
