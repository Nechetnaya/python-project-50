import json
import yaml


def decode_file(file):
    with open(file) as data:
        if not data.read().strip():
            return {}
        elif file[-4:] == 'yaml' or '.yml':
            return yaml.load(open(file), Loader=yaml.FullLoader)
        else:
            return json.load(open(file))


def code_data(data):
    return json.dumps(data, separators=('', ': '), indent=2).replace('"', '')


def generate_diff(file1, file2):
    data_1 = decode_file(file1)
    data_2 = decode_file(file2)
    result = {}
    keys = set(data_1.keys()) | set(data_2.keys())
    for item in sorted(keys):
        if item in data_1 and item not in data_2:
            result[f'- {item}'] = data_1[item]
        elif item in data_2 and item not in data_1:
            result[f'+ {item}'] = data_2[item]
        elif data_1[item] == data_2[item]:
            result[f'  {item}'] = data_1[item]
        else:
            result[f'- {item}'] = data_1[item]
            result[f'+ {item}'] = data_2[item]
    return code_data(result)
