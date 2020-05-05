from lhw import *
from scipy import stats

SIZE = 100000
p = 0.7

g = []
for i in range(SIZE):
    g.append(irngeo_2(p))

mean_geo = count_mean(g)

print(mean_geo)

observed_frequencies = np.bincount(g)
print(observed_frequencies)

expected_frequencies = [len(g) * (p * (1 - p) ** x) for x in range(min(g), max(g)+1)]
print(expected_frequencies)

chi_square = 0
for i in range(min(g), max(g)+1):
    x = ((observed_frequencies[i] - expected_frequencies[i]) ** 2) / expected_frequencies[i]
    chi_square += x

print(chi_square)
# print(stats.chisquare(observed_frequencies, expected_frequencies))

pmf = []
for i in range(min(g), max(g)+1):
    pmf.append(p * ((1 - p) ** i))

plt.hist(g, 10, density=True)
plt.plot(pmf)
plt.show()
