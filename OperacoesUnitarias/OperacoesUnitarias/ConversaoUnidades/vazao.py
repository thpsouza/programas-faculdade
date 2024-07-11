from tempo import min_to_sec
from volume import L_to_m3, cm3_to_m3


def cm3pmin_to_m3ps(x):
    return 1/min_to_sec(1/cm3_to_m3(x))


def Lpmin_to_m3ps(x):
    return 1/min_to_sec(1/L_to_m3(x))