a = []  # объявляем пустой список
n = int (input())  # указываем количество элементов списка
for i in range(n):  
    new_element = int(input())  # указываем очередной элемент списка
    a.append(new_element)  # добавляем элемент в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)