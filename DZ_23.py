# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список
# (тип списка нужно выбрать в зависимости от поставленной ниже задачи). После чего нужно
# показать меню, в котором предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести
# сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения).
# В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next_elem):
        self.next = next_elem


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        temp = Node(value)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
            return count

    def search(self, value):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == value:
                found = True
            else:
                current = current.getNext()
                return found

    def remove(self, value):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == value:
                found = True
            else :
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    l = LinkedList()
    while True:
        print('1. Добавить новое число в список')
        print('2. Удалить все вхождения числа из списка')
        print('3. Показать содержимое списка')
        print('4. Проверить наличие значения в списке')
        print('5. Замена значения в списке')
        print('6. Выход')

        choice = input('Выберите пункт меню "Список чисел": ')
        if choice == '1':
            l.add(int(input(': ')))
        elif choice == '2':
            l.remove(int(input(': ')))
        elif choice == '3':
            #
            break
        elif choice == '4':
            l.search(int(input(': ')))
        elif choice == '5':
            #
            break
        elif choice == '6':
            break
        else:
            print('Неверный пункт меню! \n')

# Задание 2
# Реализуйте класс стека для работы со строками (стек строк). Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать
# необходимую операцию.

class MyStack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.__items = []

    def push(self, value):
        if self.maxSize <= len(self.__items) - 1:
            return self.__items.append(value)
        else:
            print('Стек заполнен, добавление невозможно!')

    def pop(self, value):
        return self.__items.pop(value)

    def length(self):
        return len(self.__items)

    def empty(self):
        if self.length() == 0:
            print('Стек пустой')

    def full(self):
        if self.length() == self.maxSize:
            print('Стек полный')

    def delete(self):
        self.__items = None
        print('Стек удален!')

    def peek(self):
        return self.__items[self.length()-1]


if __name__ == '__main__':
    l = int(input('Введите размер стека строк: '))
    d = MyStack(l)
    while True:
        print('1. Помещение строки в стек')
        print('2. Выталкивание строки из стека')
        print('3. Подсчет количества строк в стеке')
        print('4. Проверку пустой ли стек')
        print('5. Проверку полный ли стек')
        print('6. очистку стека')
        print('7. Получение значения без выталкивания верхней строки из стека')
        print('8. Выход')

        choice = input('Выберите пункт меню "Стек строк фиксированного размера": ')
        if choice == '1':
            d.push(str(input('Введите строку для добавления в стек: ')))
        elif choice == '2':
            d.pop(str(input('Введите строку для добавления в стек: ')))
        elif choice == '3':
            print(d.length())
        elif choice == '4':
            d.empty()
        elif choice == '5':
            d.full()
        elif choice == '6':
            d.delete()
        elif choice == '7':
            print(d.peek())
        elif choice == '8':
            break
        else:
            print('Неверный пункт меню!')


# Задание 3
# Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным.

class Stack:
    def __init__(self):
        self.__items = []

    def push(self, value):
        return self.__items.append(value)

    def pop(self, value):
        return self.__items.pop(value)

    def length(self):
        return len(self.__items)

    def empty(self):
        if self.length() == 0:
            print('Стек пустой')

    def full(self):
        if self.length() != 0:
            print('Стек непустой')

    def delete(self):
        self.__items = None
        print('Стек удален!')

    def peek(self):
        return self.__items[self.length()-1]


if __name__ == '__main__':
    d = Stack()
    while True:
        print('1. Помещение строки в стек')
        print('2. Выталкивание строки из стека')
        print('3. Подсчет количества строк в стеке')
        print('4. Проверку пустой ли стек')
        print('5. Проверку полный ли стек')
        print('6. очистку стека')
        print('7. Получение значения без выталкивания верхней строки из стека')
        print('8. Выход')

        choice = input('Выберите пункт меню "Стек строк фиксированного размера": ')
        if choice == '1':
            d.push(str(input('Введите строку для добавления в стек: ')))
        elif choice == '2':
            d.pop(str(input('Введите строку для добавления в стек: ')))
        elif choice == '3':
            print(d.length())
        elif choice == '4':
            d.empty()
        elif choice == '5':
            d.full()
        elif choice == '6':
            d.delete()
        elif choice == '7':
            print(d.peek())
        elif choice == '8':
            break
        else:
            print('Неверный пункт меню!')

