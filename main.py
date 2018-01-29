import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, sin, exp


from settings import alpha, n, st_points

def vect_p(arg):
    arg_x, arg_y = arg
    return (4 * arg_x ** 2 - arg_y ** 2) / sqrt((4 * arg_x ** 2 - arg_y ** 2) ** 2 + (-2 * arg_x + 1) ** 2)


def vect_q(arg):
    arg_x, arg_y = arg
    return (-2 * arg_x + 1) / sqrt((4 * arg_x ** 2 - arg_y ** 2) ** 2 + (-2 * arg_x + 1) ** 2)


def calc_a(point1, point2, point3, a):
    dist12 = sqrt((point2[1]-point1[1]) ** 2 + (point2[0]-point1[0]) ** 2)
    dist23 = sqrt((point3[1]-point2[1]) ** 2 + (point3[0]-point2[0]) ** 2)
    if dist12 and dist23 / dist12 < 1:
        a = dist23 / dist12 * alpha
    return a


def calc_a_exp(point1, point2, point3, a):
    dist12 = sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2)
    dist23 = sqrt((point3[1] - point2[1]) ** 2 + (point3[0] - point2[0]) ** 2)
    if dist12 and dist23 / dist12 < 1:
        a = 0.1 * exp(dist23 * dist12)
        #print(dist23 / dist12)
    return a





if __name__ == '__main__':
    print('vse ok')
    coordinates = []

    for j in range(len(st_points)):
        coordinates.append([st_points[j], st_points[j]])

        x, y = st_points[j]
        a = alpha

        for i in range(n):
            x += a * vect_p((x, y))
            y += a * vect_q((x, y))
            coordinates[-1].append((x, y))

            #a = calc_a(coordinates[-1][-3], coordinates[-1][-2], coordinates[-1][-1], a)
            a = (i / n) * calc_a_exp(coordinates[-1][-3], coordinates[-1][-2], coordinates[-1][-1], a)
        # print(coordinates)




        list_x = []
        list_y = []
        # print(list_x)
        for el in range(len(coordinates[j])):
            list_x.append(coordinates[-1][el][0])
            list_y.append(coordinates[-1][el][1])
        # print(list_x)
        plt.plot(list_x, list_y, color='b')

    plt.plot(0.5, 1, marker='o', color='r')
    plt.plot(0.5, -1, marker='o', color='r')
    plt.axis([-3, 4, -4, 4])
    plt.grid(True)
    plt.show()