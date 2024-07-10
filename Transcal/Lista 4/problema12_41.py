## Dados:
p = 7900
cp = 640
Ts = 1200
delta = 3*10**-3
sigma = 5.67 * 10**-8

## Fração de radiação
F0_1 = 0.002134
F0_6 = 0.819217
F1_6 = F0_6 - F0_1
F6_inf = 1 - F0_6

## Emissividade total (integral):
epsilon = I = 0.6*F0_1 + 0.4*F1_6 + 0.25*F6_inf
print(f"I = {I}, e = {epsilon}")

##  Derivada?
dTdt = -2 * epsilon * sigma * Ts**4 / (p * cp * delta)
print(f"dT/dt = {dTdt}")


t = p*delta*cp/(4800*epsilon*sigma) * (1/(Ts/2)**2 - 1/(Ts**2))
print(f"t = {t}s")