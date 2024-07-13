import random


def number():
    option = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(option)
    return n
n = number()

result = []
for i in range(1, 21):
    for k in range(i + 1, 21):
        if n % (i + k) == 0:
            result.append(i)
            result.append(k)
            continue
print(n, '-', * result)


