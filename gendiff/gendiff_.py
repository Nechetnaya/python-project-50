import json


def generate_diff(file1, file2):
    data_1 = json.load(open(file1))
    data_2 = json.load(open(file2))
    if data_1 == data_2:
        result = data_1
    else:
        result = {}
        keys = set(data_1.keys()) | set(data_2.keys())
        for item in sorted(keys):
            if item in data_1 and item not in data_2:
                result[f'- {item}'] = data_1[item]
            elif item in data_2 and item not in data_1:
                result[f'+ {item}'] = data_2[item]
            else:
                if data_1[item] == data_2[item]:
                    result[f'  {item}'] = data_1[item]
                else:
                    result[f'- {item}'] = data_1[item]
                    result[f'+ {item}'] = data_2[item]
    return json.dumps(result, separators=('', ': '), indent=2).replace('"', '')
