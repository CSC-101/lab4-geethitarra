from data import Point
import math
# Write your functions for each part in the space below.

# Part 1
def first_element(list):
    final = []
    i = 0
    while i < len(list):
        if list[i]:
            final.append(list[i][0])
        i +=1
    return final

# Part 2
def x_coordinates(list_of_points):
    return_list = []
    for data in list_of_points:
        return_list.append(data.x)
    return return_list

# Part 3
def are_in_positive_quadrant(list_of_points):
    return_list = []
    for data in list_of_points:
        if data.x>=0 and data.y>=0:
            return_list.append(data)
    return return_list

# Part 4
def distance(point1, point2):
    return math.sqrt(((point2.x - point1.y)**2) + ((point2.y - point1.y)**2))

# Part 5
def manhattan_distance(point1, point2):
    return (abs(point1.x - point2.x)) + (abs(point1.y - point2.y))

# Part 6




