check_list = [11,13,14,16,17,18,19,20]


def smallestMultiple():
    for num in xrange(2520, 99999999999, 20):
        if all(num % n == 0 for n in check_list):
            return num
    return None

print(smallestMultiple())
