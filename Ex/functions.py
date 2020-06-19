import math

# Функция для определения правого или левого поворота
# На вход подаются три точки pa = [x, y], pb = [x, y], pc = [x, y]
def area(pa: list, pb: list, pc: list):
    return (pb[0] - pa[0]) * (pc[1] - pa[1]) - (pb[1] - pa[1]) * (pc[0] - pa[0])


# Расстояние между точками
# На вход p1 = [x, y], p2 = [x, y]
def length(p1: list, p2: list):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


# Нахождение стартовой точки выпуклого многоугольника
# На вход массив из точек points = [[x, y], [x, y], ...]
def find_first_point(points: list):
    x, y = points[0]
    index = 0
    k = 0
    for point in points:
        if (point[1] < y) or ((point[1] == y) and (point[0] < x)):
            x, y = point
            index = k
        k += 1
    return index


# Косинус между двумя векторами
# На вход принимаются координаты двух векторов
def cos_angle(x1: int, y1: int, x2: int, y2: int):
    return (x1 * x2 + y1 * y2) / (math.sqrt(x1 ** 2 + y1 ** 2) * math.sqrt(x2 ** 2 + y2 ** 2))


# Не помню точно, но наверное произведение двух векторов
# На вход 4 точки p1 = [x, y] p2 = [x, y] и т.д.
def vector_abs(p1: list, p2: list, p3: list, p4: list):
    return (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p4[0] - p3[0]) * (p2[1] - p1[1])

# Проверяет находиться ли точка внутри выпуклого многоугольника
# На вход массив точек p = [[x, y], [x, y], ...] и точка point = [x, y]
def check_point(p: list, point):
    res = False
    j = len(p) - 1
    for i in range(len(p)):
        if (((p[i][1] <= point[1] and p[j][1] > point[1]) or (p[j][1] <= point[1] and p[i][1] > point[1])) and
                ((p[j][1] - p[i][1] != 0) and (
                        point[0] > (p[j][0] - p[i][0]) * (point[1] - p[i][1]) / (p[j][1] - p[i][1]) + p[i][0]))):
            res = not res
        j = i
    return res

# На вход массив точек points = [[x, y], [x, y], ...]
# На выход массив точек, отсортированных по полярному углу
# p_start - точка начала выпуклого многоугольника, от нее считается полярный угол
def sort_points(points: list):
    p_start = find_first_point(points)
    p_start = points.pop(p_start)
    for i in range(len(points) - 1):
        m = math.atan2(points[i][1] - p_start[1], points[i][0] - p_start[0])
        pair = [*points[i]]
        index = i
        for j in range(i + 1, len(points)):
            if (math.atan2(points[j][1] - p_start[1], points[j][0] - p_start[0]) < m):
                m = math.atan2(points[j][1] - p_start[1], points[j][0] - p_start[0])
                pair = points[j]
                index = j
        t = [*points[i]]
        points[i] = [*pair]
        points[index] = [*t]
    points.insert(0, p_start)
    return points

# Построение прямоугольника окружающего отрезок
# На вход две точки отрезка
# На выход две точки прямоугольника
def bounding_rect(pa: list, pb: list):
    x1 = min(pa[0], pb[0])
    y1 = min(pa[1], pb[1])
    x2 = max(pa[0], pb[0])
    y2 = max(pa[1], pb[1])
    p1 = [x1, y1]
    p2 = [x2, y2]
    return [p1, p2]

# Пересечение двух прямоугольников, окружающих отрезки
# На вход четыре точки
def rectangle_intersect(pa: list, pb: list, pc: list, pd: list):
    if pb[0] >= pc[0] and pd[0] >= pa[0] and pb[1] >= pc[1] and pd[1] >= pa[1]:
        return True
    return False

# Предусловие: точка pc лежит на прямой, содержащей отрезок [pa, pb]
# True, если точка является точкой ориентированного отрезка [pa, pb], иначе False
# На вход подаются три точки
def between(pa: list, pb: list, pc: list):
    if min(pa[0], pb[0]) <= pc[0] <= max(pa[0], pb[0]) and min(pa[1], pb[1]) <= pc[1] <= max(pa[0], pb[0]):
        return True
    return False
