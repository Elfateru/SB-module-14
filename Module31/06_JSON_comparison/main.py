import json


def find_diff(old_d, new_d, diff, res=None):
    if not res:
        res = dict()
    for key, val in old_d.items():
        if key in diff:
            if old_d[key] != new_d[key]:
                res[key] = new_d[key]
        if isinstance(val, dict):
            res = find_diff(old_d[key], new_d[key], diff, res)
        if isinstance(val, list):
            for i, i_val in enumerate(val):
                if isinstance(i_val, dict):
                    res = find_diff(old_d[key][i], new_d[key][i], diff, res)
    return res


diff_list = ["services", "staff", "datetime"]

with open('json_old.json', 'r') as file:
    old_file = json.load(file)

with open('json_new.json', 'r') as file:
    new_file = json.load(file)

result = find_diff(old_file, new_file, diff_list)

with open('result.json', 'w', encoding='utf8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
print(result)
