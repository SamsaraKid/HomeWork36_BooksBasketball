from lxml import etree
import os.path



# etree.SubElement(book, 'title')
# etree.SubElement(book, 'year')
# book = etree.SubElement(root, 'book')
# etree.SubElement(book, 'title')
# etree.SubElement(book, 'year')
#




class BookShelf:
    def __init__(self):
        self.root = etree.Element('bookshelf', shelfname='Художественная литература')
        if os.path.isfile('bookshelf.xml'):
            # doc = etree.parse('bookshelf.xml')
            # print(doc)
            file = open('bookshelf.xml')
            xml = file.read().encode('utf-8')
            root = etree.fromstring(xml)
            book_dict = {}
            books = []
            for book in root.getchildren():
                for elem in book.getchildren():
                    if not elem.text:
                        text = "None"
                    else:
                        text = elem.text
                    print(elem.tag + " => " + text)
                    book_dict[elem.tag] = text
                if book.tag == "book":
                    books.append(book_dict)
                    book_dict = {}
            print(book_dict)
        else:
            print(False)
        self.books = []

    def add(self, title, year):
        self.books.append(Book(title, int(year)))
        book = etree.SubElement(self.root, 'book')
        etree.SubElement(book, 'title').text = title
        etree.SubElement(book, 'year').text = str(year)
        doc = etree.tostring(self.root, pretty_print=True, encoding='utf-8', xml_declaration=True).decode('utf-8')
        file = open('bookshelf.xml', 'w', encoding='utf-8')
        file.write(doc)
        file.close()


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
# b.menu()
