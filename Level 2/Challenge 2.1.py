def solution(l):
    l.sort(key=lambda s: list(map(int, s.split('.'))))
    return l


x = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print("Result: " + str(x))
print("Expected: ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']")
print

x = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
print("Result: " + str(x))
print(
    "Expected: ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0']")
