from Geo_Algorithms import GeoAlgorithms
import math
import Dimangan
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
        return
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")


run = True

while run:
    print("\t" * 2 + "Advanced Geometrical Algorithms" + "\t" * 2)
    print("Menu:")
    print("Module: Basic algorithms")
    print("\tEnter 1 to test Jarvis algorithm")
    print("\tEnter 2 to test Graham algorithm")
    print("\tEnter 3 to test Sequential algorithm")
    print("Module: Algorithms with sorting")
    print("\tEnter 4 to test Convex Hull algorithm")
    print("\tEnter 5 to test Chan algorithm")
    print("Module: 3-d algoritms")
    print("Module: Segment Algorithms")
    print("\tEnter 6 to test Segment intersection algorithm")
    print("Enter 0 to exit program")

    choice = int(input("Enter number here: "))

    if choice == 0:
        run = False
    elif choice == 1 or choice == 2:
        clear()
        print("This algoritm creates convex hull out of given points in 2d")
        n = int(input("Enter number of points: "))
        pts = []
        print("Enter points:(Example: 1 2)")
        for i in range(n):
            x, y = input().strip().lstrip().split()
            pts.append([int(x), int(y)])
        print("Result:")
        if choice == 1:
            res = GeoAlgorithms.Jarvis_March(pts)
            for i in range(len(res)):
                print(str(i + 1) + " point: " + str(res[i][0]) + " " + str(res[i][1]))
        elif choice == 2:
            res = GeoAlgorithms.Graham_Scan(pts)
            for i in range(len(res)):
                print(str(i + 1) + " point: " + str(res[i][0]) + " " + str(res[i][1]))
        choice = input("Do you want to continue?(y/n)")
        if choice == 'y':
            clear()
        elif choice == 'n':
            clear()
            run = False
        else:
            clear()
    elif choice == 3:
        clear()
        print("This algorithm creates convex hull online out of given points")
        n = int(input("Enter number of points: "))
        pts = []
        print("Enter points: (Example: 1 2)")
        for i in range(n):
            x, y = input().strip().lstrip().split()
            pts.append([int(x), int(y)])
            res = GeoAlgorithms.Sequential(pts)
            for j in range(len(res)):
                print(str(i + 1) + " point: " + str(res[j][0]) + " " + str(res[j][1]))
        if choice == 'y':
            clear()
        elif choice == 'n':
            clear()
            run = False
        else:
            clear()
    elif choice == 4 or choice == 5:
        clear()
        print("This algorithm creates convex hull and implements sorting algorithm to do it")
        n = int(input("Enter number of points"))
        pts = []
        print("Enter points: (Example: 1 2)")
        for i in range(n):
            x, y = input().strip().lstrip().split()
            pts.append([int(x), int(y)])
        print("Result:")
        if choice == 1:
            res = GeoAlgorithms.Convex_Hull(pts)
            for i in range(len(res)):
                print(str(i + 1) + " point: " + str(res[i][0]) + " " + str(res[i][1]))
        elif choice == 2:
            res = GeoAlgorithms.Chan_Algorithm(pts)
            for i in range(len(res)):
                print(str(i + 1) + " point: " + str(res[i][0]) + " " + str(res[i][1]))
        if choice == 'y':
            clear()
        elif choice == 'n':
            clear()
            run = False
        else:
            clear()
    elif choice == 6:
        clear()
        print("This algoritm checks if given pair of segments intersects")
        print("Enter first segment coordinates: (Example: 0 0 3 4)", end="")
        t = [int(i) for i in input().strip().lstrip().split()]
        p1 = [t[0], t[1]]
        p2 = [t[2], t[3]]
        print("Enter second segment coordinates: ", end="")
        t = [int(i) for i in input().strip().lstrip().split()]
        p3 = [t[0], t[1]]
        p4 = [t[2], t[3]]
        res = GeoAlgorithms.Segments_Intersect(p1, p2, p3, p4)
        print("Result:")
        if res:
            print("Given segments intersect")
        else:
            print("Given segments don't intersect")
        if choice == 'y':
            clear()
        elif choice == 'n':
            clear()
            run = False
        else:
            clear()



