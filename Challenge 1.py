def solution(data, n):
    newarr = []
    for num in data:
        if data.count(num) <= n:
            newarr.append(num)

    return newarr

        
x = solution([1,2,2,5,5,3,3,3,4], 1)
print(x)
