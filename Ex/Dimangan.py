def check(L: list, R: list, most: list, side):
    key = 1
    if side == 1:
        for i in L:
            y = (i[0] - most[0][0]) * (most[1][1] - most[0][1]) / (most[1][0] - most[0][0]) + most[0][1]
            if i[0] >= most[0][0] and i[1] > y:
                key = 0
        for j in R:
            y = (j[0] - most[0][0]) * (most[1][1] - most[0][1]) / (most[1][0] - most[0][0]) + most[0][1]
            if j[0] <= most[1][0] and j[1] > y:
                key = 0
    else:
        for i in L:
            y = (i[0] - most[0][0]) * (most[1][1] - most[0][1]) / (most[1][0] - most[0][0]) + most[0][1]
            if i[0] >= most[0][0] and i[1] < y:
                key = 0
        for j in R:
            y = (j[0] - most[0][0]) * (most[1][1] - most[0][1]) / (most[1][0] - most[0][0]) + most[0][1]
            if j[0] <= most[1][0] and j[1] < y:
                key = 0
    return key


def bridge(L: list, R: list):
    S1 = []
    S2 = []
    S = []
    L.sort(key=lambda x: x[1])
    R.sort(key=lambda x: x[1])
    for i in L:
        for j in R:
            if check(L, R, [i, j], 1) == 1:
                if S1[0][1] == i[1] or S1[1][1] == j[1]:
                    if S1[0][0] > i[0] or S1[1][0] < j[0]:
                        S1 = [i, j]
    L.sort(key=lambda x: x[1], reverse=True)
    R.sort(key=lambda x: x[1], reverse=True)
    for i in L:
        for j in R:
            if check(L, R, [i, j], 2) == 1:
                if S2[0][1] == i[1] or S2[1][1] == j[1]:
                    if S2[0][0] > i[0] or S2[1][0] < j[0]:
                        S2 = [i, j]
    S = S1 + S2
    return S


def Q(L: list, pq: list, R: list):
    S = []
    S = L + R
    for p in range(len(S)):
        i = S[p]
        y1 = (i[0] - pq[0][0]) * (pq[1][1] - pq[0][1]) / (pq[1][0] - pq[0][0]) + pq[0][1]
        y2 = (i[0] - pq[2][0]) * (pq[3][1] - pq[2][1]) / (pq[3][0] - pq[2][0]) + pq[2][1]
        if i[0] >= pq[0][0] and i[0] <= pq[1][0] and i[1] < y1:
            if i[0] >= pq[2][0] and i[0] <= pq[3][0] and i[1] > y2:
                S = S[:p] + S[p + 1:]
    return S


def UpperHull(points: list):
    L = []
    R = []
    pq = []
    points.sort(key=lambda x: x[0])
    if len(points) <= 2:
        return points
    else:
        x_max = points[len(points) - 1][0]
        x_min = points[0][0]
        x_med = 0
        if len(points) % 2 == 0:
            x_med = (points[int(len(points) / 2)][0] + points[int(len(points) / 2 - 1)][0]) / 2
        else:
            x_med = points[int((len(points) + 1) / 2)][0]
        j = 1
        for i in points:
            if i[0] < x_med:
                L.append(i)
            elif i[0] > x_med:
                R.append(i)
            else:
                if j % 2 == 1:
                    L.append(i)
                    j += 1
                else:
                    R.append(i)
                    j += 1
        pq = bridge(L, R)
        LUH = UpperHull(L)
        RUH = UpperHull(R)
        return Q(LUH, pq, RUH)

p1 = []
n = int(input())
for i in range(n):
    x, y = input().split()
    p1.append([int(x), int(y)])
print(UpperHull(p1))