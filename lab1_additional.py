import numpy as np
import math

M = 2
T = 40
N = 1000


def stirling(n, k):
    n1 = n
    k1 = k
    if n <= 0:
        return 1
    elif k <= 0:
        return 0
    elif n == 0 and k == 0:
        return -1
    elif n != 0 and n == k:
        return 1
    elif n < k:
        return 0
    else:
        temp1 = stirling(n1 - 1, k1)
        temp1 = k1 * temp1
        return (k1 * (stirling(n1 - 1, k1))) + stirling(n1 - 1, k1 - 1)


def is_have_all_values(data, m):
    data_list = data.tolist()
    for i in range(2 ** m):
        if data_list.count(i) <= 0:
            return False
    return True


dataset = np.random.randint(0, 2 ** M, N)
# dataset = [0, 1, 2, 0, 1, 3, 2, 2, 2, 3, 0, 1, 0, 2, 3, 1, 1, 1, 0, 3, 2, 1, 2]
print(dataset)
v = dict()
for size in range(M ** 2, T + 1):
    v[size] = 0
    for i in range(len(dataset) - size + 1):
        if is_have_all_values(dataset[i:i + size], M):
            v[size] += 1
print(v)

p = dict()
d = 2 ** M - 1
for i in range(2 ** M, T):
    p[i] = math.factorial(d) / math.pow(d, i) * stirling(i - 1, d - 1)
p[T] = 1 - math.factorial(d) / math.pow(d, T - 1) * stirling(T - 1, d)
print(p)
sum_v = sum(v.values())
print(sum_v)

hi_2 = 0
for i in range(2 ** M, T + 1):
    hi_2 += ((v[i] - sum_v * p[i]) ** 2) / (sum_v * p[i])
print("result hi_2 = {}".format(hi_2))
