from Geo_Algorithms import GeoAlgorithms
import math
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as patches


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    p = []
    n = int(input())
    for i in range(n):
        x, y = input().split()
        p.append([int(x), int(y)])
        points = GeoAlgorithms.Sequential(p)
        for i in range(len(points)):
            points[i] = (float(points[i][0]), float(points[i][1]))
        print(points)
