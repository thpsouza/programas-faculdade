import math
import sympy as sp


class Cubicas:
    def __init__(self, num_atomos, massa_molar, raio=sp.Symbol('r'), volume=None) -> None:
        ''' Classe para criar células unitárias cúbicas '''
        self.atomos = num_atomos
        self.volume = volume
        self.r = raio
        self.MM = massa_molar
        
    def densidade(self):
        NUMERO_AVOGADRO = 6.022 * 10**23
        return (self.atomos * self.MM)/(NUMERO_AVOGADRO * self.volume)


class CFC(Cubicas):
    def __init__(self, massa_molar, raio=sp.Symbol('r')) -> None:
        super().__init__(4, massa_molar, raio, 16*raio**3*2**(1/2))


class CCC(Cubicas):
    def __init__(self, massa_molar, raio=sp.Symbol('r')) -> None:
        super().__init__(2, massa_molar, raio, 64*raio**3*3**(1/2)/9)


class Plano:
    def __init__(self, num_atomos, area_plano, r = sp.Symbol('r'), pi = math.pi):
        ''' Essa classe inicializa um plano, dados quantidade de átomos e área '''
        self.atomos = num_atomos
        self.area = area_plano
        self.r = r
        self.pi = pi

    def densidade_ad(self):
        ''' Esse método retorna o valor adimensional da densidade do plano '''
        return self.atomos*self.pi*self.r**2 / self.area


class Plano100(Plano):
    def __init__(self, celula_unitaria, r=sp.Symbol('r'), pi=math.pi):
        if celula_unitaria == "CFC":
            super().__init__(1 + 4/4, (2*math.sqrt(2)*r)**2, r, pi)
        elif celula_unitaria == "CCC":
            super().__init__()



def main():
    r = sp.Symbol('r')
    
    ## Plano 100 CFC
    atomos_100 = 1 + 4/4 #2 atomos
    area_100 = (2*math.sqrt(2)*r)**2
    plano100 = Plano(atomos_100, area_100)

    ## Plano 110 CFC
    atomos_110 = 4/4 + 2/2 #2 atomos
    area_110 = 4*r * 2*r*math.sqrt(2) #lado maior * lado menor
    plano110 = Plano(atomos_110, area_110)

    ## Plano 111 CFC
    atomos_111 = 3/2 + 3/6 #2 atomos
    area_111 = (4*r)**2 * math.sqrt(3)/4
    plano111 = Plano(atomos_111, area_111)

    print("Células unitárias CFC: \n")
    print(f"Densidade do Plano (100) = {plano100.densidade_ad()}")
    print(f"Densidade do Plano (110) = {plano110.densidade_ad()}")
    print(f"Densidade do Plano (111) = {plano111.densidade_ad()}")    

    input("\nEncerrando...")


if __name__ == "__main__":
    main()
