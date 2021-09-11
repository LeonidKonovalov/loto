import random

answer = ''
win_numbers = []  # выпавшие чила
fun_text = {
    1: 'кол', 2: 'гусь', 3: 'трое, на троих', 4: 'стул', 7: 'топор', 8: 'матрёшка', 10: 'часовой',
    11: 'барабанные палочки', 12: 'дюжина', 13: 'чертова дюжина', 18: 'в первый раз', 20: 'лебединое озеро',
    21: 'очко', 22: 'гуси-лебеди', 24: 'лебедь на стуле', 25: 'опять двадцать пять', 27: 'лебедь с топором',
    33: 'кудри', 41: 'ем один', 44: 'стульчики', 48: 'половинку просим', 50: 'полста', 55: 'перчатки', 66: 'валенки',
    69: 'туда-сюда', 70: 'топор в озере', 77: 'топорики', 80: 'бабушка', 81: 'бабка с клюшкой', 85: 'перестройка',
    88: 'крендельки', 89: 'дедушкин сосед', 90: 'дедушка'
}


class Ticket:
    def __init__(self, name):
        self._name = name
        self._count = 15  # кол-во не вычеркнутых цифр
        self._ticket = [[0] * 9 for _ in range(3)]

    def __str__(self):
        return "{} ticket. Count of numbers: {}".format(self._name, self.count)

    @property
    def name(self):
        return self._name

    @property
    def count(self):
        return self._count

    @property
    def ticket(self):
        return self._ticket

    def generate(self):
        tmp = random.sample(range(1, 91), 15)  # 15 уникальных цифр для билета
        for i in range(3):
            row = tmp[i::3]  # отрезаем по 5 цифр на строку
            row.sort()
            k = 0
            position = random.sample(range(9), 5)  # позиции в строке
            position.sort()
            for j in position:
                self.ticket[i][j] = row[k]
                k += 1

    def check(self, number):
        for i in range(3):
            try:
                self._ticket[i][self._ticket[i].index(number)] = -1
                self._count -= 1
                return True
            except ValueError:
                pass
        return False

    def show(self):
        length = (27 - (len(self._name) + 2)) // 2

        if len(self._name) % 2 == 0:
            print('-' * length, self._name, '-' * (length + 1))
        else:
            print('-' * length, self._name, '-' * length)

        for i in range(3):
            row = ''
            for j in self.ticket[i]:
                if j == 0:
                    row += '   '
                elif j == -1:
                    row += ' - '
                elif j < 10:
                    row += ' ' + str(j) + ' '
                elif j >= 10:
                    row += ' ' + str(j)
            print(row)

        print('-' * 27)


def play():
    win_numbers.clear()
    # name = input('Ввдеите свое имя: ')
    #
    # if name != '' and len(name) < 28:
    #     pl_ticket = Ticket(name)
    # else:
    pl_ticket = Ticket('Player')
    en_ticket = Ticket('PC')
    pl_ticket.generate()
    en_ticket.generate()

    def gen_num():
        num = random.randint(1, 91)

        while num in win_numbers:
            num = random.randint(1, 91)

        return num

    while True:
        if pl_ticket.count == 0 or en_ticket.count == 0:
            if pl_ticket.count == 0 and en_ticket.count == 0:
                print('Ничья!')
            elif pl_ticket.count == 0:
                print('Выиграл {}!'.format(pl_ticket.name))
            elif en_ticket.count == 0:
                print('Выиграл {}!'.format(en_ticket.name))

            print('Выпавшие номера: {}'.format(win_numbers))
            break
        else:
            print('\n')
            pl_ticket.show()
            en_ticket.show()

            number = gen_num()
            win_numbers.append(number)

            print('\nВыпавшее число: {}'.format(number), '' if fun_text.get(number) is None else '- ' +
                                                                                                 fun_text.get(number),
                  'Боченков осталось:', 90 - len(win_numbers))
            ans = input('\nЗачеркнуть чило? (y/n/q - сдаться) ')

            if ans.lower() == 'y':
                if not pl_ticket.check(number):
                    print('Вы проиграли!')
                    break
            elif ans.lower() == 'n':
                if pl_ticket.check(number):
                    print('Вы проиграли!')
                    break
            elif ans.lower() == 'q':
                print('Вы сдались!')
                break

            en_ticket.check(number)


while answer.lower() != 'n':
    answer = input('\nИграть? (y/n) ')

    if answer.lower() == 'y':
        play()
