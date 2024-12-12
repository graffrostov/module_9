from os import SEEK_END
from random import choice, random

# ----------------------------------------------------------------------------------------
class MysticBall:

    def __init__(self, *words):

        self.words = words

    def __call__(self):

        return choice(self.words)

# ----------------------------------------------------------------------------------------
def get_advanced_writer(file_name):

    def write_everything(*data_set):

        with open(file_name, 'a', encoding='utf-8') as file:

            file.seek(SEEK_END)

            if iter(data_set):
                for item in data_set:

                    file.write(f'{item}\n')
            else:
                file.write(f'{data_set}\n')

    return write_everything

# ----------------------------------------------------------------------------------------
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))

# ----------------------------------------------------------------------------------------
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# write(8)

# ----------------------------------------------------------------------------------------
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())