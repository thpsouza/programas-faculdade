g = 9.80665


def n_to_dyna(x):
    return x * 1e5


def dyna_to_n(x):
    return x / 1e5


def lbf_to_n(x):
    return x * 0.45359237 * g


def n_to_lbf(x):
    return x / (0.45359237 * g)