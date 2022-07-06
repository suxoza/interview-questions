'''
    flat_list([1, 2, 3]) == [1, 2, 3]
    flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
    flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
'''


def flat_list(arg):
    result = []
    for item in arg:
        if type(item) == list:
            res = flat_list(item)
            for i in res:
                result.append(i)
        else:
            result.append(item)
    return result
        
#res = flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])


def flatten(l):
    result = []
    for item in l:
        if type(item) == list:
            for i in flatten(item):
                result.append(i)
        else:
            result.append(item)
    return result

print(flatten([[1, 2], [3, 4]]))


