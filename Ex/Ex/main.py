from Geo_Algorithms import GeoAlgorithms
import math
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as patches
import Dimangan

n = int(input())
p = []
for i in range(n):
    x, y = input().split()
    p.append([int(x), int(y)])
print(GeoAlgorithms.Jarvis_March(p))

