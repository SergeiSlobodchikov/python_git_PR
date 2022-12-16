# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def OneTask():
      number = int(input(('введите число обозначающую день недели ')))
      if number > 0 and number < 6:
            print('будни')
      elif number > 5 and number < 8:
            print('выходной')
      else:
            print('не то число')



# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def TwoTask():
      for x in [0, 1]:
          for y in [0, 1]:
              for z in [0, 1]:
                  print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} ',
                        not (x or y or z) == (not x and not y and not z))


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def ThreeTask():
      print('Программа, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости,\n'
      'в которой находится эта точка (или на какой оси она находится).')
      x = int(input(('введите координаты x: ' )))
      y = int(input(('введите координаты y: ' )))
      if x > 0 and y > 0:
          print('номер четверти плоскости 1')
      elif x < 0 and y < 0:
          print('номер четверти плоскости 3')
      elif x > 0 and y < 0:
          print('номер четверти плоскости 4')
      elif x == 0:
          if y == 0:
              print('Точка находится в центре')
          else:
              print('Точка находится на оси x')
      elif y == 0:
              print('Точка находится на оси y')
      else:
          print('номер четверти 2')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def FourTask():
      print('Программа, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)')
      number = int(input(('введите номер четверти: ' )))
      if number == 1:
          print('Диапазон x(0;+∞) y(0;+∞)')
      elif number == 2:
          print('Диапазон x(0;-∞) y(0;+∞)')
      elif number == 3:
          print('Диапазон x(0;-∞) y(0;-∞)')
      elif number == 4:
          print('Диапазон x(0;+∞) y(0;-∞)')
      else:
          print('Не то число')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
def FiveTask():
      print('Программа которая принимает на вход координаты двух точек и находит расстояние между ними \n'
            'введите координаты точки А через пробел')
      xa, ya = [int(x) for x in input().split()]
      print('введите координаты точки B через пробел')
      xb, yb = [int(x) for x in input().split()]
      print('расстояние между ними', round(((xb-xa)**2+(yb-ya)**2)**0.5, 3))

# OneTask()
# TwoTask()
# ThreeTask()
# FourTask()
# FiveTask()


