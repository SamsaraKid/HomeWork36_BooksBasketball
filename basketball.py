class BookShelf:
    def __init__(self):
        self.books = []

    def add(self, title, year):
        self.books.append(Book(title, int(year)))

    def sortbytitle(self):
        self.books.sort(key=lambda x: x.title)

    def sortbyyear(self):
        self.books.sort(key=lambda x: x.year)

    def showbooks(self):
        print('-------------------')
        print('Название       Год')
        print('-------------------')
        for i in self.books:
            i.showbook()
        print('-------------------')

    def menu(self):
        ans = int(input('Выберите действие:\n'
                        '\t1 - Добавить книгу\n'
                        '\t2 - Отсортировать по названию\n'
                        '\t3 - Отсортировать по году\n'
                        '\t4 - Вывести список книг\n'
                        '\t0 - Выход\n'))
        if ans == 1:
            title = input('Введите название:\n')
            year = input('Введите год:\n')
            self.add(title, year)
        elif ans == 2:
            self.sortbytitle()
        elif ans == 3:
            self.sortbyyear()
        elif ans == 4:
            self.showbooks()
        elif ans == 0:
            return
        self.menu()


class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def showbook(self):
        print(self.title.ljust(14), self.year)


b = BookShelf()
b.add('ванп', 1992)
b.add('абнп', 1991)
b.add('аанп', 1998)
b.menu()
