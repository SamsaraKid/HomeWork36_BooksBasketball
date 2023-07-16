class BasketballAssociation:
    def __init__(self):
        self.players = []

    def find(self, text):
        nums = []
        finded = []
        for i, p in enumerate(self.players):
            if p.name == text or str(p.height) == text or p.club == text:
                nums.append(i)
                finded.append(p)
        return nums, finded

    def showfinded(self, text):
        nums, finded = self.find(text)
        if finded:
            self.showplayers(finded, nums)
        else:
            print('Не найдено')

    def add(self, name, height, club):
        self.players.append(Player(name, int(height), club))

    def remove(self, num):
        self.players.pop(num - 1)

    def replace(self, num, what, text):
        if what == 1:
            self.players[num - 1].name = text
        elif what == 2:
            self.players[num - 1].height = int(text)
        elif what == 3:
            self.players[num - 1].club = text

    def showplayers(self, players, nums=[]):
        if not nums:
            nums = [i for i in range(len(players))]
        print('-------------------------------------------')
        print('№  Имя            Рост      Клуб           ')
        print('-------------------------------------------')
        for i, p in enumerate(players):
            print(str(nums[i] + 1).ljust(3), end='')
            p.showplayer()
        print('-------------------------------------------')

    def menu(self):
        ans = int(input('Выберите действие:\n'
                        '\t1 - Добавить игрока\n'
                        '\t2 - Удалить игрока\n'
                        '\t3 - Найти игроков\n'
                        '\t4 - Замена данных\n'
                        '\t5 - Вывод списка игроков\n'
                        '\t0 - Выход\n'))
        if ans == 1:
            name = input('Введите имя:\n')
            height = input('Введите рост:\n')
            club = input('Введите клуб:\n')
            self.add(name, height, club)
        elif ans == 2:
            num = int(input('Введите номер игрока для удаления:\n'))
            self.remove(num)
        elif ans == 3:
            text = input('Введите имя, рост или клуб для поиска:\n')
            self.showfinded(text)
        elif ans == 4:
            num = int(input('Введите номер игрока для изменения данных:\n'))
            what = int(input('Что будем менять?\n'
                             '\t1 - Имя\n'
                             '\t2 - Рост\n'
                             '\t3 - Клуб\n'))
            text = input('На что будем менять?\n')
            self.replace(num, what, text)
        elif ans == 5:
            self.showplayers(self.players)
        elif ans == 0:
            return
        self.menu()


class Player:
    def __init__(self, name, height, club):
        self.name = name
        self.height = height
        self.club = club

    def showplayer(self):
        print(self.name.ljust(14), str(self.height).ljust(9), self.club.ljust(14))


nba = BasketballAssociation()
nba.add('Вася', 175, 'Клуб 1')
nba.add('Петя', 185, 'Клуб 3')
nba.add('Саша', 179, 'Клуб 1')
nba.add('Стас', 175, 'Клуб 2')
nba.add('Гена', 195, 'Клуб 2')
nba.menu()