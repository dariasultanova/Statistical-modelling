import numpy as np
import matplotlib.pyplot as plt

MAX_DATA_SIZE = 10000
EXPECTED_MEAN = 0.5
EXPECTED_DISPERSION = 0.08333

print("{:^6} {:<15} {:<18} {:<11} {:<15}".format('n', 'Оценка распр.', 'RAND(эксперимент)', 'Теор.знач.', 'Отклонение'))
print("-----------------------------------------------------------------")
n = 20
#while n <= MAX_DATA_SIZE:
u = np.random.uniform(0, 1, n)
print(u)
mean = np.mean(u)

dispersion = 0
for i in range(n):
    dispersion += ((u[i] - mean) ** 2) / n

S = np.sqrt(dispersion)

print("{:5} {:^15} {:^19.7f} {:<11} {:<10.8f}".format(n, 'M', mean, EXPECTED_MEAN, abs(mean - EXPECTED_MEAN)))
print("{:5} {:^15} {:^19.7f} {:<11} {:<10.8f}"
        .format('', 'D', dispersion, EXPECTED_DISPERSION, abs(dispersion - EXPECTED_DISPERSION)))

count, bins, patches = plt.hist(u, 10, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='black')
plt.show()
count, bins, patches = plt.hist(u, 10, density=1, cumulative=True)
plt.show()

acc = 0
for i in range(n):
    acc += (u[i] - mean) ** 2
corr = [None]
for i in range(1, n):
    iter = 0
    for j in range(n - i):
        iter += (u[j] - mean) * (u[j + i] - mean)
    corr.append(iter / acc)
plt.plot(corr)
plt.show()
n *= 10
