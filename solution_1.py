def sqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    return res
x = int(input('Enter number of given example : '))
res = sqrt(x)
print(res)
