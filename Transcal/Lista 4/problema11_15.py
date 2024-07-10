from geral import *

## Dados:
Tc_i = 35 + 273
Tc_o = 120 + 273
Th_i = 300 + 273
mc = 10**4 / 3600
mh = 5*10**3 / 3600
U = 1500

## Calculando Cpc
Cpc = 4195

## Calculando Cph
X = list(range(480,580,10))
Y = np.array([4.53, 4.59, 4.66, 4.74, 4.84, 
              4.95, 5.08, 5.24, 5.43, 5.68]) * 1000
Cph = np.trapz(Y,X) / (X[-1] - X[0])
print(f"Cph = {Cph}")

## Calculando Th,o
Th_o = Th_i - Cpc*(Tc_o - Tc_i)*mc / (Cph*mh)
print(f"Th,o = {Th_o - 273} °C")

## Calculando q
q = mc * Cpc * (Tc_o - Tc_i)
print(f"q = {q} W")

## Calculando Área
P = (Tc_o - Tc_i) / (Th_i - Tc_i)
R = (Th_i - Th_o) / (Tc_o - Tc_i)
F = 0.97
DT1 = Th_i - Tc_o
DT2 = Th_o - Tc_i
A = q/(F*U) * log(DT2/DT1) / (DT2-DT1)
print(f"R = {R}, P = {P}, F = {F}, A = {A}m²\n")


#### Agora considerando incrustação:
Tc_o = 95 + 273
Cpc = 4187

## Novo Cph
X = list(range(500,580,10))
Y = np.array([4.66, 4.74, 4.84, 4.95, 
              5.08, 5.24, 5.43, 5.68]) * 1000
Cph = np.trapz(Y,X) / (X[-1] - X[0])
print(f"Cph = {Cph}")

## Calculando Th,o
Th_o = Th_i - Cpc*(Tc_o - Tc_i)*mc / (Cph*mh)
print(f"Th,o = {Th_o - 273} °C")

## Calculando q
q = mc * Cpc * (Tc_o - Tc_i)
print(f"q = {q} W")

## Calculando U
P = (Tc_o - Tc_i) / (Th_i - Tc_i)
R = (Th_i - Th_o) / (Tc_o - Tc_i)
F = 1
DT1 = Th_i - Tc_o
DT2 = Th_o - Tc_i
U = q/(F*A) * log(DT2/DT1) / (DT2-DT1)
print(f"R = {R}, P = {P}, F = {F}, U = {U}W/m²K")