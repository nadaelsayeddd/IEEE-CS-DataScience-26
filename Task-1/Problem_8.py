import math

coordinates_1 = tuple(map(int, input().split()))
coordinates_2 = tuple(map(int, input().split()))

disatance = math.dist(coordinates_1,coordinates_2)

print(f"The distance is {disatance}")


          