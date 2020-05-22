from functools import reduce
from math import sqrt


def Convex_Hull_Algorithm(points: list):

    points = sorted(set(points))

    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def dist(a: list, b:list):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def cmp(a,b):
    return (a>b)-(a<b)

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
    return (not len(hull) or hull[-1] != r) and hull.append(r) or hull

def _graham_scan(points):
    points.sort()
    lh = reduce(_keep_left, points, [])
    uh = reduce(_keep_left, reversed(points), [])
    return lh.extend(uh[i] for i in range(1, len(uh) - 1)) or lh

def _rtangent(hull, p):
    l, r = 0, len(hull)
    l_prev = turn(p, hull[0], hull[-1])
    l_next = turn(p, hull[0], hull[(l + 1) % r])
    while l < r:
        c = (l + r) // 2
        c_prev = turn(p, hull[c], hull[(c - 1) % len(hull)])
        c_next = turn(p, hull[c], hull[(c + 1) % len(hull)])
        c_side = turn(p, hull[l], hull[c])
        if c_prev != TURN_RIGHT and c_next != TURN_RIGHT:
            return c
        elif c_side == TURN_LEFT and (l_next == TURN_RIGHT or
                                      l_prev == l_next) or \
                c_side == TURN_RIGHT and c_prev == TURN_RIGHT:
            r = c               # Tangent touches left chain
        else:
            l = c + 1           # Tangent touches right chain
            l_prev = -c_next    # Switch sides
            l_next = turn(p, hull[l], hull[(l + 1) % len(hull)])
    return l

def _min_hull_pt_pair(hulls):
    h, p = 0, 0
    for i in range(len(hulls)):
        j = min(range(len(hulls[i])), key=lambda j: hulls[i][j])
        if hulls[i][j] < hulls[h][p]:
            h, p = i, j
    return (h, p)

def _next_hull_pt_pair(hulls, pair):
    p = hulls[pair[0]][pair[1]]
    next = (pair[0], (pair[1] + 1) % len(hulls[pair[0]]))
    for h in (i for i in range(len(hulls)) if i != pair[0]):
        s = _rtangent(hulls[h], p)
        q, r = hulls[next[0]][next[1]], hulls[h][s]
        t = turn(p, q, r)
        if t == TURN_RIGHT or t == TURN_NONE and dist(p, r) > dist(p, q):
            next = (h, s)
    return next

def Chan_Algorithm(pts):
    for m in (1 << (1 << t) for t in range(len(pts))):
        hulls = [_graham_scan(pts[i:i + m]) for i in range(0, len(pts), m)]
        hull = [_min_hull_pt_pair(hulls)]
        for throw_away in range(m):
            p = _next_hull_pt_pair(hulls, hull[-1])
            if p == hull[0]:
                return [hulls[h][i] for h, i in hull]
            hull.append(p)
