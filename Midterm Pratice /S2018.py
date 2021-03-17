def merge_dicts(*dicts):
    d = {}
    for current_dict in dicts:
        for key in current_dict.keys():
            if key in d:
                if isinstance(d[key], list):
                    d[key] = d[key].append(current_dict[key])
                else:
                    newl = [d[key], current_dict[key]]
                    d[key] = newl
            else:
                d[key] = current_dict[key]
    print(d)

merge_dicts({'a': 'apple', 'b': 'banana'}, {'a': 'ant', 'c': 'cat'})

