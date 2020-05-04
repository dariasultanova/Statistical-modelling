from lhw import *

SIZE = 10000

'''UNIFORM DISTRIBUTION'''
EXP_MEAN_UNI = 50.5
EXP_DISPERSION_UNI = 833.25

ilow = 1
iup = 100
u = []
for i in range(SIZE):
    u.append(irnuni(ilow, iup))

mean_uni = count_mean(u)
dispersion_uni = count_dispersion(u, mean_uni)

print("{:^7} {:^10} {:^13} {:^12}".format('Оценка', 'IRNUNI', 'Погрешность', 'Теор.знач.'))
print("--------------------------------------------")
print("{:7} {:^10.5} {:^13.7f} {:^12.2f}".format('M', mean_uni, abs(mean_uni - EXP_MEAN_UNI), EXP_MEAN_UNI))
print("{:7} {:^10.5} {:^13.7f} {:^12.2f}"
      .format('D', dispersion_uni, abs(dispersion_uni - EXP_DISPERSION_UNI), EXP_DISPERSION_UNI))

show_plots(u, 20)


'''BINOMIAL DISTRIBUTION'''
EXP_MEAN_BIN = 5.0
EXP_DISPERSION_BIN = 2.5

N = 10
p = 0.5

b = []
for i in range(SIZE):
    b.append(irnbin(N, p))

mean_bin = count_mean(b)
dispersion_bin = count_dispersion(b, mean_bin)

print("{:^7} {:^10} {:^13} {:^12}".format('Оценка', 'IRNBIN', 'Погрешность', 'Теор.знач.'))
print("--------------------------------------------")
print("{:7} {:^10.5} {:^13.7f} {:^12.2f}".format('M', mean_bin, abs(mean_bin - EXP_MEAN_BIN), EXP_MEAN_BIN))
print("{:7} {:^10.5} {:^13.7f} {:^12.2f}"
      .format('D', dispersion_bin, abs(dispersion_bin - EXP_DISPERSION_BIN), EXP_DISPERSION_BIN))

show_plots(b, 10)


'''GEOMETRIC DISTRIBUTION'''
EXP_MEAN_GEO = 2.0
EXP_DISPERSION_GEO = 2.2

p = 0.5
q = 1 - p

g1 = []
for i in range(SIZE):
    g1.append(irngeo_1(p))

mean_geo_1 = count_mean(g1)
dispersion_geo_1 = count_dispersion(g1, mean_geo_1)


g2 = []
for i in range(SIZE):
    g2.append(irngeo_2(p))

mean_geo_2 = count_mean(g2)
dispersion_geo_2 = count_dispersion(g2, mean_geo_2)


g3 = []
for i in range(SIZE):
    g3.append(irngeo_3(p))

mean_geo_3 = count_mean(g3)
dispersion_geo_3 = count_dispersion(g3, mean_geo_3)

print("{:^7} {:^10} {:^10} {:^10} {:^12}".format('Оценка', 'IRNGEO_1', 'IRNGEO_2', 'IRNGEO_3', 'Теор.знач.'))
print("----------------------------------------------------")
print("{:7} {:^10.3f} {:^10.3f} {:^10.3f} {:^12.2f}".format('M', mean_geo_1, mean_geo_2, mean_geo_3, EXP_MEAN_GEO))
print("{:7} {:^10.3f} {:^10.3f} {:^10.3f} {:^12.2f}"
      .format('D', dispersion_geo_1, dispersion_geo_2, dispersion_geo_3, EXP_DISPERSION_GEO))

show_plots(g1, 10)
show_plots(g2, 10)
show_plots(g3, 10)


'''POISSON DISTRIBUTION'''
EXP_MEAN_POI = 10
EXP_DISPERSION_POI = 10

mu = 10

p1 = []
for i in range(SIZE):
    p1.append(irnpoi(mu))

mean_poi = count_mean(p1)
dispersion_poi = count_dispersion(p1, mean_poi)


p2 = []
for i in range(SIZE):
    p2.append(irnpsn(mu))

mean_psn = count_mean(p2)
dispersion_psn = count_dispersion(p2, mean_psn)

print("{:^7} {:^10} {:^10} {:^12}".format('Оценка', 'IRNPOI', 'IRNPSN', 'Теор.знач.'))
print("-----------------------------------------")
print("{:7} {:^10.3f} {:^10.3f} {:^12.2f}".format('M', mean_poi, mean_psn, EXP_MEAN_POI))
print("{:7} {:^10.3f} {:^10.3f} {:^12.2f}".format('D', dispersion_poi, dispersion_psn, EXP_DISPERSION_POI))

show_plots(p1, 23)
show_plots(p2, 23)


'''LOGARITHMIC DISTRIBUTION'''
EXP_MEAN_LOG = 1.44270
EXP_DISPERSION_LOG = 0.80402

q = 0.5

l = []
for i in range(SIZE):
    l.append(irnlog(q))

mean_log = count_mean(l)
dispersion_log = count_dispersion(l, mean_log)

print("{:^7} {:^10} {:^13} {:^12}".format('Оценка', 'IRNPOI', 'Отклонение', 'Теор.знач.'))
print("---------------------------------------------")
print("{:7} {:^10.3f} {:^13.7f} {:^12.5f}".format('M', mean_log, abs(mean_log - EXP_MEAN_LOG), EXP_MEAN_LOG))
print("{:7} {:^10.3f} {:^13.7f} {:^12.5f}"
      .format('D', dispersion_log, abs(dispersion_log - EXP_DISPERSION_LOG), EXP_DISPERSION_LOG))

show_plots(l, 10)
