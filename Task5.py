# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

print('Введите координаты точки А')
x1 = int(input('x = '))
y1 = int(input('y = '))
print('Введите координаты точки B')
x2 = int(input('x = '))
y2 = int(input('y = '))
AB = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('Расстояние равно', f'{AB:.3f}')