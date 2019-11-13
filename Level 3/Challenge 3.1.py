def solution(n):
    stairs = [[-1 for j in range(n + 2)] for i in range(n + 2)]
    return count(1, n, stairs) - 1


def count(height, left, staircase):
    if staircase[height][left] != -1:
        return staircase[height][left]
    if left == 0:
        return 1
    if left < height:
        return 0
    staircases = count(height + 1, left - height, staircase) + count(
        height + 1, left, staircase
    )
    staircase[height][left] = staircases
    return staircases


x = solution(5)
print("Result: " + str(x))
print("Expected: 2")

x = solution(200)
print("Result: " + str(x))
print("Expected: 487067745")
