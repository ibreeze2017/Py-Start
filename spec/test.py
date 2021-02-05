from math import sqrt


def is_prime(n: int):
    flag = True
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            flag = False
            break
    return flag


def split_num(a: int, v_list: list):
    if is_prime(a):
        v_list.append(str(a))
    else:
        for i in range(2, int(a / 2)):
            if 0 == a % i:
                if is_prime(i):
                    v_list.append(str(i) + ' ')
                    a = int(a / i)
                    break
        split_num(a, v_list)


def _round(a: float):
    s = str(a).split('.')
    i = int(s[0])
    r = int(s[1][0])
    if r >= 5:
        return i + 1
    return i


def __round():
    a = str(float(input()))
    b = a.split('.')
    if int(b[1][0]) >= 5:
        return int(b[0]) + 1
    return int(b[0])


# print(_round(float(input())))
print(__round())
