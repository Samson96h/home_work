def open_list_recursive (ml):
    result = []
    for el in ml:
        if isinstance(el, list):
            result.extend(open_list_recursive(el))
        else:
            result.append(el)
    return result

print(open_list_recursive([1,2,3, [4,5,[0,0,0],6, [7,8,[40, 50, 60],9], 54, 6]]))


def open_list (ml):
    result = []
    while ml:
        el = ml.pop(0)
        if isinstance(el, list):
            ml = el + ml
        else:
            result.append(el)
    return result


print(open_list([1,2,3, [4,5,[0,0,0],6, [7,8,[40, 50, 60],9], 54, 6]]))


class MList:
    def __init__(self, *args):
        self.__my_list = [None] * len(args)
        for i in range(len(args)):
            self.__my_list[i] = args[i]

    @property
    def list(self):
        return self.__my_list

    def __getitem__(self, index):
        return self.__my_list[index]

    def __setitem__(self, index, value):
        self.__my_list[index] = value

    def __repr__(self):
        return str(self.list)


m1 = MList(1,2,3,9)
print(m1)

m1[2] = 5
print(m1)