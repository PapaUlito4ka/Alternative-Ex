def mk_OP(a, b):
    x1 = min(a[0], b[0])
    x2 = max(a[0], b[0])
    y1 = min(a[1], b[1])
    y2 = max(a[1], b[1])
    t1 = [x1, y1]
    t2 = [x2, y2]
    p = [t1, t2]
    return p


def find_OP_cross(p1, p2):
    if ((p1[1][0] >= p2[0][0]) and (p2[1][0] >= p1[0][0]) and (p1[1][1] >= p2[0][1]) and (p2[1][1] >= p1[0][1])):
        return True
    else:
        return False


def area_triangle(a, b, c):
    S = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return S


def exact_method(a, b, c, d):
    S1 = area_triangle(a, b, c)
    S2 = area_triangle(a, b, d)
    S3 = area_triangle(c, d, a)
    S4 = area_triangle(c, d, b)
    if (S1 * S2 > 0) or (S3 * S4 > 0):
        return False
    # else if (S1 * S2 < 0) or (S3 * S4 < 0):
    else:
        return True  # все остальные случаи, когда отрезки не пересекаются, были отброшены на первом этапе


def PPPO(a, b, c, d):
    if not (find_OP_cross(mk_OP(a, b), mk_OP(c, d))):
        return False
    else:
        return exact_method(a, b, c, d)


a = [1, 1]
b = [4, 2]
c = [7, 3]
d = [10, 4]

if PPPO(a, b, c, d):
    print("CROSS")
else:
    print("NO CROSS")

