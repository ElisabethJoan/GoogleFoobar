def solution(s):
    counter = 0
    lefts = [pos for pos, char in enumerate(s) if char == "<"]
    rights = [pos for pos, char in enumerate(s) if char == ">"]
    for i in range(len(rights)):
        for j in range(len(lefts)):
            if rights[i] < lefts[j]:
                counter += 2

    return counter


x = solution(">----<")
print("Result: " + str(x))
print("Expected: 2")

x = solution("<<>><")
print("Result: " + str(x))
print("Expected: 4")
