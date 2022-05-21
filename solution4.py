# 4. Write a function that calculates the value of 'a' to the power of 'b'.
# For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.


def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


print(power(4, 2))
