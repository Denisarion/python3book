class Dog():
    name=""
    # Конструктор
    # Вызывается на момент создания объекта этого типа
    def __init__ (self, newName):
        self.name = newName

# Создаем собаку и устанавливаем ее имя:
myDog = Dog ("Лайка")

# Вывести имя собаки, убедиться, что оно было установлено 
print (myDog.name)

# Следующая команда выдаст ошибку, потому что
# конструктору не было передано имя:
# herDog = Dog()