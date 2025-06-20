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


def recursive_max(arr):
    if len(arr) == 1:
        return arr[0]
    sub_max = recursive_max(arr[1:])
    if arr[0] > sub_max:
        return arr[0]
    else:
        return sub_max

print(recursive_max([4, 8, 96, 78, 56]))


def recursive_count(arr):
    if not arr:
        return 0
    return 1 + recursive_count(arr[1:])

print(recursive_count([4, 8, 96, 78, 56]))


from random import randint

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    index = randint(0, len(lst) - 1)
    pivot = lst[index]
    rest = lst[:index] + lst[index + 1:]

    less = [i for i in rest if i <= pivot]
    greater = [i for i in rest if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([4, 8, 96, 78, 56]))