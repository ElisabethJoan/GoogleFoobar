from math import *


def genVectorMap(size, coord, length):
    vectorMap = [coord]
    count = 0
    l, r = -coord, length - coord
    for i in range(size):
        left = vectorMap[0]
        right = vectorMap[count]
        left += (l*2)
        right += (r*2)
        l, r = -r, -l
        vectorMap = [left] + vectorMap + [right]
        count += 2

    return vectorMap


def solution(dimensions, your_position, guard_position, distance):
    mx = your_position[0]
    my = your_position[1]
    gx = guard_position[0]
    gy = guard_position[1]
    width = dimensions[0]
    height = dimensions[1]

    matSize = int(max(distance/width, distance / height)) + 1
    guardMirrors = [genVectorMap(matSize, gx, width),
                    genVectorMap(matSize, gy, height)]
    myMirrors = [genVectorMap(matSize, mx, width),
                 genVectorMap(matSize, my, height)]
    mirrors = [myMirrors, guardMirrors]

    angles = set()
    angleDist = {}
    for i in range(len(mirrors)):
        for j in mirrors[i][0]:
            for k in mirrors[i][1]:
                angle = atan2((your_position[1]-k), (your_position[0]-j))
                dist = sqrt((your_position[0]-j)
                            ** 2 + (your_position[1]-k)**2)
                if [j, k] != your_position and distance >= dist:
                    if (angle in angleDist and angleDist[angle] > dist) or angle not in angleDist:
                        if i == 0:
                            angleDist[angle] = dist
                        else:
                            angleDist[angle] = dist
                            angles.add(angle)

    return len(angles)


x = solution([3, 2], [1, 1], [2, 1], 4)
print("Result: " + str(x))
print("Expected: 7")
print

x = solution([300, 275], [150, 150], [185, 100], 500)
print("Result: " + str(x))
print("Expected: 9")
