## VISCOSIDADE
def cp_to_pas(x):
    return x * 0.001


## PRESSÃO
def bar_to_pa(x):
    return x * 100000


def atm_to_pa(x):
    return x * 101325


def cmHG_to_pa(x):
    return x * 1333.2239


def cmH2O_to_pa(x):
    return x * 98.0368


def psi_to_pa(x):
    return x * 6894.76


## TEMPO
def min_to_s(x):
    return x*60


def hour_to_s(x):
    return x*60*60


## COMPRIMENTO
def in_to_m(x):
    return x * 0.0254


## VOLUME
def cm3_to_m3(x):
    return x * (0.01)**3


def L_to_m3(x):
    return x * 0.001


## VAZÃO
def cm3_min_to_m3_s(x):
    return 1/min_to_s(1/cm3_to_m3(x))


def L_min_to_m3_s(x):
    return 1/min_to_s(1/L_to_m3(x))



## VELOCIDADE
def rpm_to_radps(x):
    # Lazy import
    from math import pi
    return x * 2*pi/60


def radps_to_rpm(x):
    # Lazy import
    from math import pi
    return x * 60 / (2*pi)


def main():
    ...


if __name__ == '__main__':
    main()