swap_coordinates = ("15", "30")
(first, second) = swap_coordinates
print(f"The swap coordinates are {first}, {second}")
print(f"The swapped value is {second}, {first}")

import math
A = (15, 30)
B = (30, 15)
print(f"The distance from A to B is: ", math.dist(A, B))

#or
distance = math.sqrt(((B[0] - A[0]) ** 2) + ((B[1] - A[1]) ** 2))
print ("The distance between A and B is: ", distance)