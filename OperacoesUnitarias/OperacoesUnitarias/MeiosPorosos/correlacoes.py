### Escoamento em meios porosos

def kappa(phi, d, epsilon, beta=5):
    return (phi * d) ** 2 * epsilon ** 3 / (36 * beta * (1 - epsilon) ** 2)


def C(k, epsilon, k0=10 ** -10):
    return (0.13 * ((k0 / k) ** 0.37) + 0.1 * ((k0 / k) ** 0.01)) ** 0.98 * epsilon ** (-3 / 2)
