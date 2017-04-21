def findTriNum():
    divisors = []
    iterable = 1
    num = 1
    answer = 0

    while answer == 0:
        for x in range(1,num):
            if (num % x == 0):
                divisors.append(x)
                if len(divisors) >= 500:
                    answer = num
                    break
        print(len(divisors))
        divisors = []
        iterable += 1
        num += iterable

    print(answer)
    return answer

findTriNum()
