import time

slow = False

if slow:
    def get_nod(a, b):
        """ Вычисление НОД для целых чисел a и b
            по алгоритму Евклида (медленный)

        :param a: первое целое число
        :param b: второе целое число
        :return: НОД
        """
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a

        return a

else:
    def get_nod(a, b):
        """ Вычисление НОД для целых чисел a и b
            по алгоритму Евклида (быстрый)

        :param a: первое целое число
        :param b: второе целое число
        :return: НОД
        """
        while min(a, b) > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return max(a,b)

def test_nod(func):
    #  --- test #1 ------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("Test 1 - ok")
    else:
        print("Test 1 failed")

    #  --- test #2 ------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("Test 2 - ok")
    else:
        print("Test 2 failed")
    #  --- test #3 Speed -------
    a = 2
    b = 100000000
    start_time = time.time()
    res = get_nod(a, b)
    end_time = time.time()
    dt = end_time - start_time
    if res == 2 and dt < 1:
        print("Test 3 - ok")
    else:
        print("Test 3 failed")


res = get_nod(18, 24)
print(res)
test_nod(get_nod)  # Тестирование функции (имя функции без вызова, то есть аргументов)
