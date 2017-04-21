import math

def sumsquare():
    sumOfSquares, squareOfSum, difference = 0, 0, 0
    for x in range(101):
        sqr = x*x
        sumOfSquares += sqr
        squareOfSum += x
        print squareOfSum

    squareOfSum *= squareOfSum
    difference = squareOfSum - sumOfSquares

    return [sumOfSquares, squareOfSum, difference]

print(sumsquare())
