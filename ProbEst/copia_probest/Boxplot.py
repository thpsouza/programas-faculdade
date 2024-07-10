## BOXPLOT - ESTATÍSTICA
## Plotar/imprimir boxplot de uma ou mais amostras

import matplotlib.pyplot as plt
from . import Medidas_Centralidade, Medidas_Dispersao, Quartis, Discrepancia

def boxplot(*amostras,plot=True,labels=[],mostrar_media=False,casas_decimais=3):
    '''Plota/Imprime o boxplot de uma ou mais amostras 
    
    plot: bool, opcional, padrao=True
        Se False, não plota, apenas imprime o boxplot no console
        OBS: (IMPRIMIR FUNCIONA ATÉ 6 DIGITOS)
    
    labels: list[str], opcional, padrao=[]
        Lista com a legenda para cada boxplot
        OBS: (Se vazio, define automaticamente as legendas)

    mostrar_media: bool, opcional, padrao=False
        Se True, mostra a média aritimética no boxplot
    
    casas_decimais: int, opcional, padrao=3
        Casas decimais para arredondar os dados, se o boxplot for impresso
    '''
    if plot:
        if not labels:
            for amostra in amostras:
                media = round(Medidas_Centralidade.media(amostra),4)
                desvpad = round(Medidas_Dispersao.desvio_padrao(amostra),4)
                quartis = Quartis.quartis(amostra)[:3]
                discrep = Discrepancia.valores_discrepantes(amostra)
                labels.append(f" Media = {media};   Desvio Padrão = {desvpad}; \n Quartis: {quartis};   Valores Discrepantes: {discrep}")
        
        fig,ax = plt.subplots(figsize=(12,6))
        bp = ax.boxplot(x=amostras,labels=labels,showmeans=mostrar_media)
        plt.legend()
        plt.show()
        return bp
        
    def string_6(string):
        '''Formata uma string, adicionando espaços em branco na frente até len = 6'''
        new_string = str(string)[::-1]
        while len(new_string) < 6:
            new_string += ' '
        return new_string[::-1]

    for amostra in amostras:
        # Centralidade
        media = Medidas_Centralidade.media(amostra)
        # Dispersão
        variancia = Medidas_Dispersao.variancia(amostra)
        desvpad = Medidas_Dispersao.desvio_padrao(amostra)
        # Quartis
        Q1,Q2,Q3,DIQ = Quartis.quartis(amostra)
        # Limites
        CI = Discrepancia.cerca_inferior(amostra)
        CS = Discrepancia.cerca_superior(amostra)
        discrep  = Discrepancia.valores_discrepantes(amostra)
        x_max = max(amostra) if max(amostra) > CS else ''#maior valor
        x_min = min(amostra) if min(amostra) < CI else ''#menor valor

        s1 = string_6(x_max)
        s2 = string_6(round((x_max+CS)/2,casas_decimais)) if x_max != '' else string_6(round(CS+desvpad,casas_decimais))
        s3 = string_6(round(CS,casas_decimais))
        s4 = string_6(round(float(Q3),casas_decimais))
        s5 = string_6(round(Q2,casas_decimais))
        s6 = string_6(round(float(Q1),casas_decimais))
        s7 = string_6(round(CI,casas_decimais))
        s8 = string_6(round((CI+x_min)/2,casas_decimais)) if x_min != '' else string_6(round(CI-desvpad,casas_decimais))
        s9 = string_6(x_min)    


        print(                                  '          _____________________________________________________')
        print(                                  '         |                                                     |')
        print(                                  '         |                      \u00d7{}'.format(s1),'                       |')
        print(                                  '         |                                                     |')
        print(' ',s2,                           '|_                                                    |')
        print(                                  '         |                                                     |')
        print(                                  '         |           ___________________________  {}'.format(s3),'      |', ' --> CS')
        print(                                  '         |                        |                            |')
        print(' ',s4,                           '|_       ________________|_________________           |', ' --> Q3')
        print(                                  '         |       |                                  |          |')
        print(                                  '         |       |                                  |          |')
        print(                                  '         |       |----------------------------------| \u2022{}  |'.format(s5), ' --> Q2 (Mediana)')
        print(                                  '         |       |                                  |          |')
        print(' ',s6,                           '|_      |__________________________________|          |', ' --> Q1')
        print(                                  '         |                        |                            |')
        print(                                  '         |           _____________|______________ {}'.format(s7),'      |', ' --> CI')
        print(                                  '         |                                                     |')
        print(' ',s8,                           '|_                                                    |')
        print(                                  '         |                                                     |')
        print(                                  '         |                      \u00d7{}'.format(s9),'                       |')
        print(                                  '         |_____________________________________________________|')


        return {'Média':media,'Variância':variancia,'Desvio Padrao':desvpad, 'Quartis':[Q1,Q2,Q3,DIQ], 'Cercas':[CI,CS], 'Valores Discrepantes':discrep}