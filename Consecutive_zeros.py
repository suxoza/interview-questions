def consecutive_zeros(binary_string):
    res, max = 0, 0
    for x in binary_string:
        if int(x) == 0:
            res += 1
            if res > max: 
                max = res
        else:
            res = 0
    return max