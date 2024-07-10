from fator_de_atrito import colebrook_white

class PerdaDeCarga():
    def __init__(self,L,D,v,g=9.81,chute_inicial=0.02,**kwargs):
        '''
        kwargs: 
        - Re
        - E_D
        - Fd
        '''
        self.L = L
        self.D = D
        self.g = g
        self.v = v
        self.Re = kwargs.get('Re')
        self.E_D = kwargs.get('E_D')
        if isinstance(self.Re,(float,int)) and isinstance(self.E_D,(float,int)):
            self.fator_de_atrito = colebrook_white(self.Re,self.E_D,chute_inicial)
        else:
            self.fator_de_atrito = kwargs.get('Fd')


    def localizada(self):
        return self.L/self.D * self.v**2/(2*self.g) * self.fator_de_atrito

    def acidentes(self):
        return

    def total(self):
        return