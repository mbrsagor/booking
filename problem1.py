def print_depth(data):
    c = 1
    for key, val in data.items():
        if type(val) != dict:
            print(f"{key}  {c}")
        else:
            print(f"{key}  {c}")
            c = c + 1
            temp = val
            while type(temp) == dict:
                for k1, v1 in temp.items():
                    if type(v1) == dict:
                        print(f"{k1}  {c}")
                        temp = v1
                    else:
                        print(f"{k1}  {c}")
                        temp = 0
                c = c + 1


a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4
        }
    }
}

print_depth(a)
