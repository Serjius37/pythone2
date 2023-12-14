#!/usr/bin/python3
'''
Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
Формат входных данных
На вход программе в первой строке подается число nn – общее количество слов. Далее идут nn строк со словами.
Формат выходных данных
Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.
'''


s = set()

s = {
    x
      for _ in range(int(input()))
      for x in input().lower()
      }
for _ in range(int(input())):
    for x in input().lower():
        s.add(x)
        
print(len(s))