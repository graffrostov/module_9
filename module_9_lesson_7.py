def is_prime(func):
    def wrapper(*args):

        summ = func(*args)


        if summ <= 1:
            itog = 'Не простое и не составное число'

        elif summ == 2:
            itog = 'Простое'

        elif summ % 2 == 0:
            itog = 'Составное'

        else:
            itog = 'Простое'

            for i in range(3, int(summ ** 0.5) + 1, 2):
                if summ % i == 0:
                    itog = 'Составное'
                    break

        print(itog)
        return summ

    return wrapper

@is_prime
def sum_three(a:int, b:int, c:int):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
