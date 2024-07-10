from math import pi

## Dados
T1 = 300
T2 = 1000
D2 = 0.4
D1 = 0.8
L = 0.2
sigma = 5.67 * 10**-8

R1 = D1/2 / L
R2 = lambda D2: D2/2 / L
S = lambda D2: 1 + (1 + R2(D2)**2)/R1**2
F1_ = lambda D2: 1/2 * (S(D2) - (S(D2)**2 - 4*(D2/D1)**2)**(1/2))

F12 = F1_(0.8) - F1_(0.4)

q = pi * D1**2 / 4 * F12 * sigma * (T1**4 - T2**4)

print(q)
