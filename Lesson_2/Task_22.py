# Найти расстояние между точками в пространстве 2D/3D
#             координаты двух точек и находит расстояние между ними в 2D пространстве.
#             A (3,6); B (2,1) -> 5,09
#             A (7,-5); B (1,-1) -> 7,21 */
import math

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

distanse = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y2, 2))
print(f"distance: {distanse}")