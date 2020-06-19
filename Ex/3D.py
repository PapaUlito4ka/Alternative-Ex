import numpy as np
from copy import deepcopy
import math


def volume(a, b, c, d):
    return (1 / 6) * np.dot([d[0] - a[0], d[1] - a[1], d[2] - a[2]],
                            np.cross([b[0] - a[0], b[1] - a[1], b[2] - a[2]], [c[0] - a[0], c[1] - a[1], c[2] - a[2]]))


def squared_area(edge, p_start):
    return np.linalg.norm(np.cross([edge[1][0] - edge[0][0], edge[1][1] - edge[0][1], edge[1][2] - edge[1][2]],
                                   [edge[1][0] - p_start[0], edge[1][1] - p_start[1], edge[1][2] - p_start[2]]))


'''def PivotOnTriangle(edge, point, points):
    vol = volume(edge[0], edge[1], point, points[0])
    res = deepcopy(points[0])
    for i in range(1, len(points)):
        if points[i] not in edge and point != points[i]:
            if volume(edge[0], edge[1], point, points[i]) < vol:
                vol = volume(edge[0], edge[1], point, points[i])
                res = deepcopy(points[i])
    return res'''


def create_flat(p0, p1, p2):
    A = (p1[1] - p0[1]) * (p2[2] - p0[2]) - (p2[1] - p0[1]) * (p1[2] - p0[2])
    B = (p1[0] - p0[0]) * (p2[2] - p0[2]) - (p2[0] - p0[0]) * (p1[2] - p0[2])
    C = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])
    D = -p0[0] * A - p0[1] * B - p0[2] * C
    return (A, B, C, D)


def Merge(points: list):
    return GiftWrapping(points)


def cos_between_flats(A1, B1, C1, A2, B2, C2):
    try:
        return (A1 * A2 + B1 * B2 + C1 * C2) / (
                    math.sqrt(A1 ** 2 + B1 ** 2 + C1 ** 2) * math.sqrt(A2 ** 2 + B2 ** 2 + C2 ** 2))
    except ZeroDivisionError:
        return 1


def point_length(A, B, C, D, point):
    return (math.fabs(A * point[0] + B * point[1] + C * point[2] + D)) / math.sqrt(A ** 2 + B ** 2 + C ** 2)


def PivotOnTriangle(edge, point, points):
    A1, B1, C1, D1 = create_flat(edge[0], edge[1], point)
    cos = -1
    res = []
    for i in range(len(points)):
        if points[i] not in edge and points[i] != point:
            A2, B2, C2, D2 = create_flat(edge[0], edge[1], points[i])
            if math.acos(cos_between_flats(A1, B1, C1, A2, B2, C2)) > cos or \
                    (math.acos(cos_between_flats(A1, B1, C1, A2, B2, C2)) == cos and \
                     point_length(A1, B1, C1, D1, res) < point_length(A1, B1, C1, D1, points[i])):
                cos = math.acos(cos_between_flats(A1, B1, C1, A2, B2, C2))
                res = deepcopy(points[i])
    return res


def PivotOnEdge(edge, points):
    p_start = points[0]
    area2 = squared_area(edge, p_start)
    for i in range(1, len(points)):
        if points[i] not in edge:
            vol = volume(edge[0], edge[1], p_start, points[i])
            if vol < 0:
                p_start = points[i]
            elif vol == 0:
                _area2 = squared_area(edge, points[i])
                if area2 < _area2:
                    p_start = points[i]
                    area2 = _area2
    return p_start


def FindEdgeOnHull(points: list):
    point = points[0]
    q = deepcopy(point)

    for p in points:
        if q[0] < p[0] and q[1] == p[1] and q[2] == p[2]:
            q = deepcopy(p)
    if q == point:
        q[0] += 1
    e = [deepcopy(point), deepcopy(q)]
    q = PivotOnEdge(e, points)
    return [point, q]


def FindTriangleOnHull(points: list):
    p, q = FindEdgeOnHull(points)
    r = PivotOnEdge([p, q], points)
    return [p, q, r]


def GiftWrapping(points: list):
    if len(points) < 4:
        return [points]
    points.sort()
    t = FindTriangleOnHull(points)
    Q = [[t[0], t[1]], [t[2], t[1]], [t[0], t[2]]]
    H = []
    H.append(t)
    proccesed = []

    while len(Q) > 0:
        e = Q.pop()
        if [e[0], e[1]] not in proccesed and [e[1], e[0]] not in proccesed:
            point = []
            for triangle in H:
                if e[0] in triangle and e[1] in triangle:
                    i = 0
                    while triangle[i] == e[0] or triangle[i] == e[1]:
                        i += 1
                    point = deepcopy(triangle[i])
            q = PivotOnTriangle(e, point, points)
            t = [[e[0], e[1]], [e[0], q], [e[1], q]]
            for el in t:
                if [el[0], el[1]] not in Q and [el[1], el[0]] not in Q:
                    Q.append(el)
            key = 0
            for triangle in H:
                if e[0] in triangle and e[1] in triangle and q in triangle:
                    key = 1
                    break
            if key == 0:
                H.append([e[0], e[1], q])
            proccesed.append(e)
    return H


def DivideAndConquer(points: list):
    if len(points) <= 4:
        ps = GiftWrapping(points)
        res = []
        for flat in ps:
            for p in flat:
                if p not in res:
                    res.append(p)
        return res
    else:
        median = points[len(points) // 2][0] if len(points) % 2 == 1 else (points[len(points) // 2][0] +
                                                                           points[len(points) // 2 + 1][0]) / 2
        r = []
        l = []
        for pnt in points:
            if pnt[0] < median:
                r.append(pnt)
            else:
                l.append(pnt)
        r = DivideAndConquer(r)
        l = DivideAndConquer(l)
        t = r + l
        ps = Merge(t)
        res = []
        for flat in ps:
            for p in flat:
                if p not in res:
                    res.append(p)
        return res


def QuickHull(points: list):
    if len(points) < 4:
        return points
    CH = []
    i = 0
    while i <= len(points) - 4:
        a = points[i]
        b = points[i + 1]
        c = points[i + 2]
        d = points[i + 3]
        arr = np.array([[a[0] - d[0], b[0] - d[0], c[0] - d[0]], [a[1] - d[1], b[1] - d[1], c[1] - d[1]],
                        [a[2] - d[2], b[2] - d[2], c[2] - d[2]]])
        if np.linalg.det(arr) == 0.0:
            pass
        else:
            CH += [a, b, c, d]
            # for j in range(4):
            #    points.pop(i)
            break
        i += 1
    return Merge(points)


'''n = int(input())
p = []
for i in range(n):
    x, y, z = input().split()
    p.append([int(x), int(y), int(z)])
p.sort()
a = QuickHull(p)
for el in a:
    print(el)
print(len(a))'''
