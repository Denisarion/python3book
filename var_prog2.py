x = 50 # глобальная переменная

def func(): 
    global x # указываем, что x глобальная переменная
    print('x равно', x) 
    x = 2    # изменяем глобальную переменную
    print ('Заменяем глобальное значение x на', x)

func() 
print ('Значение x составляет', x)
