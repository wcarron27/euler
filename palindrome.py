import pdb

def isPal(num):
    return str(num) == str(num)[::-1]

def largest():
    pdb.set_trace()
    largest = 0
    x = 999
    while x > 0:
        y = 999
        while y > 0:
            if isPal(x*y):
                if x*y > largest:
                    largest = x*y
                    print(largest)
            y -= 1
        x -= 1

    return largest



print(largest())
