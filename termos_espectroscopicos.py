from itertools import product, combinations
from collections import Counter
import os
import numpy as np

term_letters = 'SPDFGHIKLMNOQRTUVWXYZ'


def get_term_symbols(l, r):
    """Return a list of term symbols for the configuration l^r."""

    # Total number of (ml, ms) pairs for this subshell.
    n = (2*l+1)*2
    # All possible values of ml = -l, -l+1, ..., l-1, l.
    ml = list(range(-l,l+1))
    # All possible values of 2ms = -1, 1. That is, ms = -1/2, +1/2. We work
    # with 2ms instead of ms so that we can handle integers only.
    ms2 = [-1,1]
    # All possible (ml, 2ms) pairs for this subshell.
    ml_ms2 = list(product(ml, ms2))

    # All possible microstates for r electrons in this subshell.
    microstates = list(combinations(range(n), r))
    # The totals ML = sum(ml) and MS2 = sum(2ms) for each microstate
    ML = [sum([ml_ms2[microstate[j]][0] for j in range(r)])
                                    for microstate in microstates]
    MS2 = [sum([ml_ms2[microstate[j]][1] for j in range(r)])
                                    for microstate in microstates]
    # Count the microstates (MS, ML). Store them this way round so we can
    # pick off the ground state term (maximum S) first.
    MS2_ML = Counter(zip(MS2,ML))
    N = len(microstates)

    # Extract the term symbols by starting at the minimum (ML, MS) value and
    # removing microstates corresponding to the (L, S) term it belongs to.
    # Repeat until we're out of microstates.
    terms:list[str] = []
    while N>0:
        S, L = min(MS2_ML)

        ## Calculando os termos de acoplamento spin-órbita:
        Js = []
        for i in np.arange(abs(abs(S/2)-abs(L)),abs(abs(S/2)+abs(L))+1):
            if i == int(i):
                i = int(i)
            Js.append(str(i))
        Js = ','.join(Js)
        
        ## Montando a lista de strings 
        terms.append("{}{}{}".format(-S+1, term_letters[-L], " "*(5-len(str(-S+1)))+f"({Js})" ))
        
        ## Retirando os microestados utilizados da tabela de microestados:
        for ML in range(L, -L+1):
            for MS in range(S, -S+1,2):
                MS2_ML[MS,ML] -= 1
                if MS2_ML[MS,ML] == 0:
                    del MS2_ML[MS,ML]
                N -= 1


    ## Formatando os repetidos
    terms = dict(Counter(terms))

    return terms


def main():
    orbital = list(term_letters.lower())
    while True:
        entrada = input("Insira a configuração que deseja calcular os termos (e- equivalentes apenas) -- Ex: 'd2': \n>>> ").lower()
        try:
            l = orbital.index(entrada[0])
            n = int(entrada[1:])
            ## Verificar se não ultrapassou o máximo de eletrons da camada
            if n>2*(2*l+1):
                print("Entrada inválida. \n")
                continue
            break
        except:
            os.system('cls')
            print("Entrada inválida. \n")
            entrada = ''

    termos = get_term_symbols(l,n)
    print(f"\nOs termos espectroscópicos são (1º corresponde ao E.F.): \n")

    ## Formatando
    N = max([len(i) for i in termos])
    s = " ___Termos" + "_"*int((N-2)/2-1) + "Js" + "_"*int((N-2)/2-1)
    print(s + "Repetições___ \n")

    for i,j in termos.items():
        print(f" ==>  {i}" + ' '*(N-len(i)+1) + f"  ({j}x)")

    print("\n Total:" + " "*(len(s)-5) + f"{sum(termos.values())}")


if __name__ == "__main__":
    while True:
        main()
        if input("\nAperte enter para rodar o programa novamente. \n"):
            break
        os.system('cls')