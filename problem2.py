class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", 1, None)
person_b = Person("User", 2, person_a)


def print_depth(data):
    c = 1
    for key, val in data.items():
        if type(val) != dict and isinstance(val, Person) == False:
            print(f"{key}  {c}")
        else:
            print(f"{key}  {c}")
            c = c + 1
            temp = val
            while type(temp) == dict or isinstance(temp, Person):
                for k1, v1 in temp.items():
                    if type(v1) == dict:
                        print(f"{k1}  {c}")
                        temp = v1
                    elif isinstance(v1, Person):
                        print(f"{k1}:  {c}")
                        temp = v1
                        c = c + 1
                        while isinstance(temp, Person):
                            print(f"first_name:  {c}")
                            print(f"last_name:  {c}")
                            print(f"father:  {c}")
                            if isinstance(temp.father, Person):
                                temp = temp.father
                                c = c + 1
                            else:
                                temp = 0
                    else:
                        print(f"{k1}  {c}")
                        temp = 0
                c = c + 1


a = {
    'key1': 1,
    'key2':
        {'key3': 1,
         'key4': {
             'key5': 4,
             'user': person_b
         }}}

print_depth(a)
