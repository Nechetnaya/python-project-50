import json
import yaml
from gendiff.modules.formaters.stylish import stylish
from gendiff.modules.formaters.plain import plain


def generate_diff(file1, file2, format_="stylish"):
    data_1 = decode_file(file1)
    data_2 = decode_file(file2)
    if format_ == "stylish":
        return stylish(build_diff(data_1, data_2))
    if format_ == 'plain':
        return plain(build_diff(data_1, data_2), '')[:-1]


def decode_file(file):
    with open(file) as data:
        if not data.read().strip():
            return {}
        elif file[-4:] == 'yaml' or '.yml':
            return yaml.load(open(file), Loader=yaml.FullLoader)
        else:
            return json.load(open(file))


def build_diff(data_1, data_2):
    result = {}
    keys = set(data_1.keys()) | set(data_2.keys())
    for item in sorted(keys):
        if item in data_1 and item not in data_2:
            result[item] = {"act": "-", "value1": data_1[item], "value2": None}
        elif item in data_2 and item not in data_1:
            result[item] = {"act": "+", "value2": data_2[item], "value1": None}
        else:
            if type(data_1[item]) is dict and type(data_2[item]) is dict:
                result[item] = {
                    "act": "",
                    "value1": build_diff(data_1[item], data_2[item]),
                }
            else:
                if data_1[item] == data_2[item]:
                    result[item] = {
                        "act": "",
                        "value1": data_1[item],
                        "value2": data_2[item],
                    }
                else:
                    result[item] = {
                        "act": "+-",
                        "value1": data_1[item],
                        "value2": data_2[item],
                    }
    return result
