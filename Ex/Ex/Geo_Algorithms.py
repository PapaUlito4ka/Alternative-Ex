import functions
import math
import Dimangan
from Segments_Algoritms import VPO
import Andrei


class GeoAlgorithms:

    def __init__(self):
        pass

    @staticmethod
    def Jarvis_March(points: list):
        if len(points) == 1:
            return points
        m = functions.find_first_point(points)
        b = []
        b.append(points[m])
        points[m] = points[0]
        points[0] = b[0]
        k = 0
        minn = 1

        for j in range(1, len(points)):
            if (functions.vector_abs(b[k], points[minn], b[k], points[j]) < 0) or \
                (functions.vector_abs(b[k], points[minn], b[k], points[j]) == 0 and
                 functions.length(b[k], points[minn]) < functions.length(b[k], points[j])):
                minn = j
        k += 1
        b.append(points[minn])
        minn = 0
        while not(b[k][0] == b[0][0] and b[k][1] == b[0][1]):
            for j in range(1, len(points)):
                if (functions.vector_abs(b[k], points[minn], b[k], points[j]) < 0) or \
                    ((functions.vector_abs(b[k], points[minn], b[k], points[j]) == 0) and
                     (functions.length(b[k], points[minn]) < functions.length(b[k], points[j]))):
                    minn = j
            k += 1
            b.append(points[minn])
            minn = 0
        b.pop()
        return b

    @staticmethod
    def Graham_Scan(points: list):
        stack = []
        p_start = functions.find_first_point(points)
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
        stack.append(p_start)
        for i in range(len(points)):
            next_to_top = 0
            if len(stack) == 1:
                next_to_top = stack[-1]
            else:
                next_to_top = stack[-2]
            while len(stack) > 0 and functions.area(next_to_top, stack[-1], points[i]) < 0:
                stack.pop()
            stack.append(points[i])
        return stack

    @staticmethod
    def Sequential(points: list):
        l = []
        l.append(points[0])
        if len(points) == 1:
            return l
        for i in range(1, len(points)):
            if len(l) < 3:
                l.append(points[i])
            else:
                if functions.check_point(l, points[i]) or l.count(points[i]) != 0:
                    continue
                functions.sort_points(l)
                pair = []
                i1 = 0
                i2 = 0
                m = 1
                for j in range(len(l) - 1):
                    for k in range(j + 1, len(l)):
                        if functions.cos_angle(l[j][0] - points[i][0], l[j][1] - points[i][1], l[k][0] - points[i][0], l[k][1] - points[i][1]) < m:
                            m = functions.cos_angle(l[j][0] - points[i][0], l[j][1] - points[i][1], l[k][0] - points[i][0], l[k][1] - points[i][1])
                            pair = [l[j], l[k]]
                            try:
                                i1 = l.index(l[j])
                                i2 = l.index(l[k])
                            except:
                                pass
                if i2 - i1 == len(l) - 1:
                    l.append(points[i])
                elif i2 - i1 == 1:
                    l.pop()
                    l.insert(i2 - 1, points[i])
                else:
                    i1 += 1
                    while i1 < i2:
                        l.pop(i1)
                        i2 -= 1
                    l.insert(i1, points[i])
        functions.sort_points(l)
        return l

    @staticmethod
    def Segments_Intersect(pa: list, pb: list, pc: list, pd: list):
        p1, p2 = functions.bounding_rect(pa, pb)
        p3, p4 = functions.bounding_rect(pc, pd)
        if not functions.rectangle_intersect(p1, p2, p3, p4):
            return False
        s1 = functions.area(pc, pd, pa)
        s2 = functions.area(pc, pd, pb)
        s3 = functions.area(pa, pb, pc)
        s4 = functions.area(pa, pb, pd)
        if ((s1 > 0 > s2) or (s1 < 0 < s2)) and ((s3 > 0 > s4) or (s3 < 0 < s4)):
            return True
        elif s1 == 0 and functions.between(pc, pd, pa):
            return True
        elif s2 == 0 and functions.between(pc, pd, pb):
            return True
        elif s3 == 0 and functions.between(pa, pb, pc):
            return True
        elif s4 == 0 and functions.between(pa, pb, pd):
            return True
        return False

    # Методы Дмитрия
    @staticmethod
    def Convex_Hull(points: list):
        return Dimangan.Convex_Hull_Algorithm(points)

    @staticmethod
    def Chan_Algorithm(points: list):
        return Dimangan.Chan_Algorithm(points)

    # Методы Романа
    @staticmethod
    def ASI(segments: list):
        return VPO(segments)

    @staticmethod
    def GiftWrapping3D(points: list):
        return Andrei.GiftWrapping(points)

    @staticmethod
    def DivideAndConquer3D(points: list):
        return Andrei.DivideAndConquer(points)

    @staticmethod
    def QuickHull3D(points: list):
        return Andrei.QuickHull(points)
