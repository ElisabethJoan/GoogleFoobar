def solution(n):
    n = int(n)
    actions = 0

    while n > 1:
        x = (n - 1)/2
        if n % 2 != 0:
            if x == 1:
                n -= 1
            elif x % 2 == 0:
                n -= 1
            else:
                n += 1
            actions += 1
        else:
            n = n / 2
            actions += 1
    return actions


x = solution("15")
print("Result: " + str(x))
print("Expected: 5")
print

x = solution("4")
print("Result: " + str(x))
print("Expected: 2")
