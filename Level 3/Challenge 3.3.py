from fractions import *
from functools import reduce


def transToProb(tm):
    probMatrix = []
    for i in range(len(tm)):
        newRow = []
        if all([v == 0 for v in tm[i]]):
            for j in tm[i]:
                newRow.append(0)
            newRow[i] = 1
            probMatrix.append(newRow)
        else:
            for j in tm[i]:
                if j == 0:
                    newRow.append(0)
                else:
                    newRow.append(Fraction(j, sum(tm[i])))
            probMatrix.append(newRow)

    return probMatrix


def getSubMatrix(m, rows, cols):
    result = []
    for row in rows:
        current_row = []
        for col in cols:

            current_row.append(m[row][col])
        result.append(current_row)

    return result


def genIdentMatrix(n):
    result = [[0 for x in range(n)] for x in range(n)]
    for i in xrange(n):
        result[i][i] = Fraction(1, 1)

    return result


def subtractMatrices(a, b):
    result = []
    for row_index, row in enumerate(a):
        column = []
        for col_index in range(len(row)):
            column.append(a[row_index][col_index] - b[row_index][col_index])
        result.append(column)

    return result


def inverseMatrix(m, inverse):
    for col in range(len(m)):
        diagonal_row = col
        k = Fraction(1, m[diagonal_row][col])
        m = multiplyRow(m, diagonal_row, k)
        inverse = multiplyRow(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(len(m)):
            if source_row != target_row:
                k = -m[target_row][col]
                m = addMultipleOfRow(m, source_row, k, target_row)
                inverse = addMultipleOfRow(inverse, source_row, k, target_row)
    return inverse


def multiplyRow(m, row, k):
    row_operator = genIdentMatrix(len(m))
    row_operator[row][row] = k
    return multiplyMatrices(row_operator, m)


def addMultipleOfRow(m, source_row, k, target_row):
    row_operator = genIdentMatrix(len(m))
    row_operator[target_row][source_row] = k
    return multiplyMatrices(row_operator, m)


def multiplyMatrices(a, b):
    a_cols = len(a[0])
    rows = len(a)
    cols = len(b[0])

    result = [[0 for x in range(cols)] for x in range(rows)]
    for row in range(rows):
        for col in range(cols):
            dotProduct = Fraction(0, 1)
            for i in range(a_cols):
                dotProduct += a[row][i]*b[i][col]
            result[row][col] = dotProduct
    return result


def solution(m):
    if len(m) == 1:
        return [1, 1]

    terminalStates = []
    nonTerminalStates = []
    for index, row in enumerate(m):
        if sum(row) == 0:
            terminalStates.append(index)
        else:
            nonTerminalStates.append(index)

    probMatrix = transToProb(m)

    Q = getSubMatrix(probMatrix, nonTerminalStates, nonTerminalStates)
    R = getSubMatrix(probMatrix, nonTerminalStates, terminalStates)

    x = genIdentMatrix(len(Q))
    y = subtractMatrices(x, Q)
    z = inverseMatrix(y, x)

    probVector = multiplyMatrices(z, R)

    denominators = []
    for i in probVector[0]:
        denominators.append(Fraction(i).limit_denominator().denominator)

    denominator = reduce(lambda a, b: a*b // gcd(a, b), denominators)
    result = [item.numerator * denominator /
              item.denominator for item in probVector[0]]
    result.append(denominator)

    return map(int, result)


x = solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)
print(str(x))
print("[7, 6, 8, 21]")
print

x = solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)
print(str(x))
print("[0, 3, 2, 9, 14]")
