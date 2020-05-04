import numpy as np
import matplotlib.pyplot as plt


def irnuni(ilow, iup):
    return round(((iup - ilow + 1) * np.random.uniform(0, 1) + ilow), 0)


def irnbin(N, p):
    if N > 100:
        IR = round(rnnorm(N * p, np.sqrt(N * p * (1 - p))) + 0.5)
    else:
        alpha = np.random.rand()
        p_it = (1 - p)**N
        IR = 0
        while alpha - p_it >= 0:
            alpha = alpha - p_it
            p_it = p_it * (((N - IR) / (IR + 1)) * (p / (1 - p)))
            IR = IR + 1
    return IR


def rnnorm(mu, sigma):
    return np.random.normal(mu, sigma)


def irngeo_1(p):
    alpha = np.random.rand()
    p_it = p
    IR = 0
    while alpha - p_it >= 0:
        alpha = alpha - p_it
        p_it = p_it * (1 - p)
        IR = IR + 1
    return IR


def irngeo_2(p):
    alpha = np.random.rand()
    IR = 0
    while alpha > p:
        alpha = np.random.rand()
        IR = IR + 1
    return IR


def irngeo_3(p):
    alpha = np.random.rand()
    IR = round(np.log(alpha) / np.log(1 - p)) + 1
    return IR


def irnpoi(mu):
    if mu > 88:
        IR = rnnorm(mu, mu)
    else:
        alpha = np.random.rand()
        p_it = np.exp(-mu)
        IR = 1
        while (alpha - p_it) >= 0:
            alpha = alpha - p_it
            p_it = p_it * (mu / IR)
            IR = IR + 1
    return IR


def irnpsn(mu):
    if mu > 88:
        IR = rnnorm(mu, mu)
    else:
        alpha = np.random.rand()
        p_it = alpha
        IR = 1
        while p_it >= np.exp(-mu):
            alpha = np.random.rand()
            p_it = p_it * alpha
            IR = IR + 1
    return IR


def irnlog(q):
    p = 1 - q
    alpha = np.random.rand()
    p_it = -(1 / np.log(p)) * (1 - p)
    IR = 1
    while (alpha - p_it) >= 0:
        alpha = alpha - p_it
        p_it = p_it * (IR / (IR + 1)) * (1 - p)
        IR = IR + 1
    return IR


def count_mean(dataset):
    sum = 0
    for i in range(len(dataset)):
        sum += dataset[i]
    mean = sum / len(dataset)
    return mean


def count_dispersion(dataset, mean):
    dispersion = 0
    for i in range(len(dataset)):
        dispersion += ((dataset[i] - mean) ** 2) / len(dataset)
    return dispersion


def show_plots(dataset, bins):
    plt.hist(dataset, bins, density=True)
    plt.show()
    plt.hist(dataset, bins, density=1, cumulative=True)
    plt.show()
