#!/usr/bin/python3
'''
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.
Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.
Формат входных данных
На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице, далее идут n×mn×m слов, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
'''

n, m = int(input()), int(input())
matrix = []

for i in range(n):
#    row = []
    for w in range(m):
#        row.append(input())
        matrix.append(input())
    
for t in range(n):
    for k in range(m):
        print(matrix[t][k], end=' ')
    print()