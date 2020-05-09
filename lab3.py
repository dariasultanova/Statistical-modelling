from lhw import *

SIZE = 10000

'''UNIFORM DISTRIBUTION'''
a = 1
b = 5
u = []
for i in range(SIZE):
    u.append(rnuni(a, b))

TEOR_MEAN_UNI = (a + b) / 2
TEOR_DISPERSION_UNI = ((b - a) ** 2) / 12

mean_uni = count_mean(u)
dispersion_uni = count_dispersion(u, mean_uni)

print("{:^7} {:^10} {:^13} {:^12}".format('Оценка', 'RNUNI', 'Погрешность', 'Теор.знач.'))
print("--------------------------------------------")
print("{:7} {:^10.5f} {:^13.7f} {:^12.2f}".format('M', mean_uni, abs(mean_uni - TEOR_MEAN_UNI), TEOR_MEAN_UNI))
print("{:7} {:^10.5f} {:^13.7f} {:^12.2f}"
      .format('D', dispersion_uni, abs(dispersion_uni - TEOR_DISPERSION_UNI), TEOR_DISPERSION_UNI))

show_plots(u, 15)


'''NORMAL DISTRIBUTION'''
TEOR_MEAN_NORM = 0.0
TEOR_DISPERSION_NORM = 1.0

n1 = []
n2 = []
for i in range(SIZE):
    n1.append(rnrm1())
    n2.append(rnrm2())

mean_norm1 = count_mean(n1)
dispersion_norm1 = count_dispersion(n1, mean_norm1)

mean_norm2 = count_mean(n2)
dispersion_norm2 = count_dispersion(n2, mean_norm2)

print("{:^7} {:^10} {:^10} {:^12}".format('Оценка', 'RNRM1', 'RNRM2', 'Теор.знач.'))
print("-----------------------------------------")
print("{:7} {:^10.5f} {:^10.5f} {:^12.2f}".format('M', mean_norm1, mean_norm2, TEOR_MEAN_NORM))
print("{:7} {:^10.5f} {:^10.5f} {:^12.2f}"
      .format('D', dispersion_norm1, dispersion_norm2, TEOR_DISPERSION_NORM))

show_plots(n1, 20)
show_plots(n2, 20)


'''EXPONENTIAL DISTRIBUTION'''
TEOR_MEAN_EXP = 1.0
TEOR_DISPERSION_EXP = 1.0

b = 1

e = []
for i in range(SIZE):
    e.append(rnexp(b))

mean_exp = count_mean(e)
dispersion_exp = count_dispersion(e, mean_exp)

print("{:^7} {:^10} {:^12}".format('Оценка', 'RNEXP', 'Теор.знач.'))
print("--------------------------------------------")
print("{:7} {:^10.5f} {:^12.2f}".format('M', mean_exp, TEOR_MEAN_EXP))
print("{:7} {:^10.5f} {:^12.2f}".format('D', dispersion_exp, TEOR_DISPERSION_EXP))

show_plots(e, 20)


'''CHI-SQUARED DISTRIBUTION'''
TEOR_MEAN_CHI = 10
TEOR_DISPERSION_CHI = 20

N = 10

c = []
for i in range(SIZE):
    c.append(rnchis(N))

mean_chi = count_mean(c)
dispersion_chi = count_dispersion(c, mean_chi)

print("{:^7} {:^10} {:^12}".format('Оценка', 'RNCHIS', 'Теор.знач.'))
print("------------------------------")
print("{:7} {:^10.5f} {:^12.2f}".format('M', mean_chi, TEOR_MEAN_CHI))
print("{:7} {:^10.5f} {:^12.2f}".format('D', dispersion_chi, TEOR_DISPERSION_CHI))

show_plots(c, 20)


'''STUDENT'S DISTRIBUTION'''
TEOR_MEAN_STUD = 0
TEOR_DISPERSION_STUD = 1.25

N = 10

s = []
for i in range(SIZE):
    s.append(rnstud(N))

mean_stud = count_mean(s)
dispersion_stud = count_dispersion(s, mean_stud)

print("{:^7} {:^10} {:^13} {:^12}".format('Оценка', 'RNSTUD', 'Погрешность', 'Теор.знач.'))
print("--------------------------------------------")
print("{:7} {:^10.5f} {:^13.7f} {:^12.2f}".format('M', mean_stud, abs(mean_stud - TEOR_MEAN_STUD), TEOR_MEAN_STUD))
print("{:7} {:^10.5f} {:^13.7f} {:^12.2f}"
      .format('D', dispersion_stud, abs(dispersion_stud - TEOR_DISPERSION_STUD), TEOR_DISPERSION_STUD))

show_plots(s, 20)
