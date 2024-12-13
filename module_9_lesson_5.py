class StepValueError(ValueError):
    pass

class RangeValueError(ValueError):
    pass

# -----------------------------------------------------------------------------------------
class Iterator:
    # -------------------------------------------------------------------------------------
    def __init__(self, start:int, stop:int, step:int=1):

        # Если шаг равен 0, то генерируем ошибку
        if step == 0:
            raise StepValueError()
        else:
            self.step = step

        self.start = start
        self.stop = stop
        self.pointer = self.start

        # Признак первого элемента
        self.first_elem = True

    # -------------------------------------------------------------------------------------
    def __iter__(self):

        # Устанавливаем точку отсчёта на стартовую позицию
        self.pointer = self.start

        # Восстанавливаем признак первого элемента
        self.first_elem = True

        return self

    # -------------------------------------------------------------------------------------
    def __next__(self):

        # Если первый элемент
        if self.first_elem:

            # Проверяем диапазон на пригодность
            if (self.step > 0 and (self.start < self.stop)) or (self.step < 0 and (self.start > self.stop)):

                # Меняем признак первого элемента и возвращаем значение
                self.first_elem = False
                return self.pointer
            # Иначе генерируем ошибку
            else:
                raise RangeValueError()

        # self.step > 0 and
        if (self.start < self.stop):
            if self.pointer <= (self.stop - self.step):
                self.pointer += self.step
            else:
                raise StopIteration()

        # self.step < 0 and
        elif (self.start > self.stop):
            if self.pointer >= (self.stop - self.step):
                self.pointer += self.step
            else:
                raise StopIteration()

        # На всякий случай для неучтённых ситуаций
        else:
            raise RangeValueError()

        return self.pointer

# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')

print()

for i in iter3:
    print(i, end=' ')

print()

for i in iter4:
    print(i, end=' ')

print()


try:
    for i in iter5:
        print(i, end=' ')
except RangeValueError:
    print('Неверные параметры')

# for i in iter5:
#     print(i, end=' ')

