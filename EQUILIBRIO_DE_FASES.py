#                       Funções Equilíbrio de fases

linhas = lambda n: print ("\n" * n)


#0) CONVERSÕES

def conversoes():
    print("Qual deseja acessar? - (Basta digitar o número) ")
    print("(0) Conversão de pressões ")
    print("(1) Conversão de temperaturas")
    print("")
    print("Para sair basta apertar deixar em branco")
    choose_0 = input()
    print("")
    if choose_0 == '':
        return
    else:
        if int(choose_0) == 0:
            return conv_press()
        if int(choose_0) == 1:
            return conv_temp()

    

def conv_press():
    print("Qual unidade de partida? - (Basta digitar o número)")
    print("(0) atm")
    print("(1) bar")
    print("(2) torr")
    choose_i = input()
    if choose_i == '':
        print("")
        return conversoes()
    else:
        choose_1 = int(choose_i)
        unidades_partida = {0: "atm", 1: "bar", 2: "torr"}
        texto = "E qual é essa pressão em {}'s? ".format(unidades_partida[choose_1])
        print("")
        press_partida = input(texto)
        print("")
        if choose_1 == 0:
            A = float(press_partida)
            B = A*(1.01325)
            T = A*760
            press_convertida = {0: B, 1:T}
            unidade_convertida = {0: "bar", 1: "torr"}
        if choose_1 == 1:
            B = float(press_partida)
            A = B*0.986923
            T = B*750.062
            press_convertida = {0: A, 1:T}
            unidade_convertida = {0: "atm", 1: "torr"}
        if choose_1 == 2:
            T = float(press_partida)
            A = T*0.00131579
            B = T*0.00133322
            press_convertida = {0: A, 1: B}
            unidade_convertida = {0: "atm", 1: "bar"}

        print("")
        print("{} {} de pressão equivale(m) a: ".format(press_partida,unidades_partida[choose_1]))
        print("")
        print(" {} {} de pressão".format(press_convertida[0],unidade_convertida[0]))
        print(" {} {} de pressão".format(press_convertida[1],unidade_convertida[1]))
        input()
        print("-------------------------------------------------------------------------------")
        print("")
        return conversoes()

def conv_temp():
    print("Qual unidade de partida? - (Basta digitar o número)")
    print("(0) Celsius")
    print("(1) Kelvin")
    print("(2) Fahrenheit")
    choose_ii = input()
    if choose_ii == '':
        print("")
        return conversoes()
    else:
        choose_2 = int(choose_ii)
        unidades_partida = {0: "Celsius", 1: "Kelvin", 2: "Fahrenheit"}
        print("")
        temperatura_partida = input("E qual é essa temperatura em graus {}? ".format(unidades_partida[choose_2]))
        print("")
        if choose_2 == 0:
            C = float(temperatura_partida)
            K = C + 273.15
            F = (C*1.8)+32
            temp_convertida = {0: K, 1: F}
            unidade_convertida = {0: "Kelvin", 1: "Fahrenheit"}
        if choose_2 == 1:
            K = float(temperatura_partida)
            C = K - 273.15
            F = (C*1.8)+32
            temp_convertida = {0: C, 1: F}
            unidade_convertida = {0: "Celsius", 1: "Fahrenheit"}
        if choose_2 == 2:
            F = float(temperatura_partida)
            C = (F-32)*1.8
            K = C + 273.15
            temp_convertida = {0: C, 1: K}
            unidade_convertida = {0: "Celsius", 1: "Kelvin"}

        print("")
        print("{} grau(s) {} equivale(m) a: ".format(temperatura_partida,unidades_partida[choose_2]))
        print("")
        print(" {} graus {}".format(temp_convertida[0],unidade_convertida[0]))
        print(" {} graus {}".format(temp_convertida[1],unidade_convertida[1]))
        input()
        print("-------------------------------------------------------------------------------")
        print("")
        return conversoes()





#1) Variança - Grau de liberdade
def variança(*arg):
    print("A variança, ou o número de graus de liberdade é o número de coordenadas")
    print("intensivas que precisamos conhecer a fim de definir o estado do sistema.")
    print("A variança também pode ser definida como o número de coordenadas intensivas")
    print("que se pode variar sem alterar o número de fases em equilíbrio")
    print("")
    print("V = C - P + 2")
    print("Onde: C = Número de componentes; P = Número de fases no equilíbrio")
    print("")
    if len(arg) == 2:
        V = arg[0] - arg[1] + 2
        return "Variança = ", V
    

#2) Lei de Raoult
def raoult(*arg):
    print("Em um sistema multicomponente, a pressão parcial de um componente i na fase")
    print("vapor é linearmente proporcional a sua fração molar em fase líquida;")
    print("sendo a constante de proporcionalidade igual a pressão de vapor do componente")
    print("puro na mesma temperatura da mistura (Pi0)")
    print("")
    print("Lei de Raoult:  Pi = Xi Pi0")
    print("Onde: Pi é a pressão parcial do componente i")
    print("      Xi é a fração molar do componente i no sistema")
    print("      Pi0 é a pressão de vapor de i puro, na mesma temperatura do sistema")
    print("")
    if len(arg) == 2:
        Pi = arg[0]*arg[1]
        return "Pressão parcial de i =", Pi

#3) Lei de Dalton das pressões parciais
def Ptot(*arg):
    print("A pressão total é a soma das pressões parciais")
    print("")
    i = 0
    Ptot = 0
    while i < len(arg):
        Ptot = Ptot + arg[i]
        i+=1
    return "Pressão total do sistema = ", Ptot


#4) Equação do ponto de bolha
def P_bolha(*arg):
    print("A equação do ponto de bolha relaciona a pressão total na fase vapor")
    print("com a composição da fase líquida.")
    print("")
    print("Eq do ponto de bolha:  P = Pb0 + (Pa0 - Pb0)*Xa")
    print("Onde: P é a pressão do sistema na fase vapor;")
    print("Pi0 é a pressão de vapaor de i puro")
    print("e Xa é fração molar de a na fase líquida")
    print("")
    print("Por convenção, o componente A é aquele com a maior pressão de vapor")
    print("")
    if len(arg) == 0:
        print("Pa0 tem que ser maior que Pb0")
        print("E as frações molares devem ser entre 0 e 1")
        print("")
        m = input("Quer a resposta em quantas casas decimais? -- Enter = abortar função.")
        if m == '':
            return "Abortado."
        else:
            n = int(m)
            Pa0 = float(input("Insira a pressão de vapor de a:"))
            Pb0 = float(input("Insira a pressão de vapor de b:"))
            P = input("Insira a pressão total do sistema:")
            if P == '':
                Xa = input("Insira a fração molar Xa:")
                if Xa == '':
                    Ya = input("Insira a fração molar Ya:")
                    if Ya == '':
                        return "É necessário inserir informações além das pressões de vapor"
                    else:
                        Xa = (float(Ya)*Pb0)/(Pa0+(Pb0-Pa0)*float(Ya))
                        P = Pb0 + (Pa0 - Pb0)*Xa
                        print("")
                        print("--------------------------------------")
                        print("Pressão da fase vapor do sistema = ", round(P,n))
                        print("")
                        print("Fração molar Xa = ", round(Xa,n))
                        print("")
                        print("Fração molar Xb = ", round(1-Xa,n))
                        print("")
                        print("Fração molar Yb = ", round(1-float(Ya),n))
                        print("")
                        print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
                        print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor,")
                        print("se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
                        print("") 
                        print("----------------------------------------------------------------------------")
                else:
                    P = Pb0 + (Pa0 - Pb0)*float(Xa)
                    Ya = (float(Xa)*Pa0)/(Pb0+(Pa0-Pb0)*float(Xa))
                    print("")
                    print("--------------------------------------")
                    print("Pressão da fase vapor do sistema = ", round(P,n))
                    print("")
                    print("Fração molar Xb = ", round(1-float(Xa),n))
                    print("")
                    print("Fração molar Ya = ", round(Ya,n))
                    print("")
                    print("Fração molar Yb = ", round(1-Ya,n))
                    print("")
                    print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
                    print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor,")
                    print("se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
                    print("")                    
                    print("----------------------------------------------------------------------------")
            else:
                Xa = (float(P) - Pb0)/(Pa0-Pb0)
                Ya = (Xa*Pa0)/(Pb0+(Pa0-Pb0)*Xa)
                print("")
                print("--------------------------------------")            
                print("Fração molar Xa = ", round(Xa,n))
                print("")
                print("Fração molar Xb = ", round(1-Xa,n))
                print("")
                print("Fração molar Ya = ", round(Ya,n))
                print("")
                print("Fração molar Yb = ", round(1-Ya,n))
                print("")
                print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
                print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor,")
                print("se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
                print("")                 
                print("----------------------------------------------------------------------------")



#5) Equação do ponto de orvalho
def P_orvalho(*arg):
    print("A equação do ponto de bolha relaciona a pressão total na fase vapor")
    print("com a composição da fase vapor.")
    print("")
    print("Eq do ponto de bolha:  P = (Pa0*Pb0)/(Pa0+(Pb0-Pa0)*Ya)")
    print("Onde: P é a pressão do sistema na fase vapor;")
    print("Pi0 é a pressão de vapaor de i puro")
    print("e Ya é fração molar de a na fase vapor")
    print("")
    print("Por convenção, o componente A é aquele com a maior pressão de vapor")
    print("")
    if len(arg) == 0:
        print("Pa0 tem que ser maior que Pb0")
        print("E as frações molares devem ser entre 0 e 1")
        print("")
        m = input("Quer a resposta em quantas casas decimais? -- Enter = abortar função.")
        if m == '':
            return "Abortado."
        else:
            n = int(m)
            Pa0 = float(input("Insira a pressão de vapor de a:"))
            Pb0 = float(input("Insira a pressão de vapor de b:"))
            P = input("Insira a pressão total do sistema:")
            if P == '':
                Ya = input("Insira a fração molar da fase vapor - Ya:")
                if Ya == '':
                    Xa = input("Insira a fração molar da fase líq - Xa:")
                    if Xa == '':
                        return "É necessário inserir informações além das pressões de vapor"
                    else:
                        Ya = (float(Xa)*Pa0)/(Pb0+(Pa0-Pb0)*float(Xa))
                        P = (Pa0*Pb0)/(Pa0+(Pb0-Pa0)*Ya)
                        print("")
                        print("--------------------------------------")
                        print("Pressão da fase vapor do sistema = ", round(P,n))
                        print("")
                        print("Fração molar Ya = ", round(Ya,n))
                        print("")
                        print("Fração molar Xb = ", round(1-float(Xa),n))
                        print("")
                        print("Fração molar Yb = ", round(1-Ya,n))
                        print("")
                        print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
                        print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor,")
                        print("se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
                        print("") 
                        print("----------------------------------------------------------------------------")
                else:
                    P = (Pa0*Pb0)/(Pa0+(Pb0-Pa0)*float(Ya))
                    Xa = (float(Ya)*Pb0)/(Pa0+(Pb0-Pa0)*float(Ya))
                    print("")
                    print("--------------------------------------")
                    print("Pressão da fase vapor do sistema = ", round(P,n))
                    print("")
                    print("Fração molar Xa = ", round(Xa,n))
                    print("")
                    print("Fração molar Xb = ", round(1-Xa,n))
                    print("")
                    print("Fração molar Yb = ", round(1-float(Ya),n))
                    print("")
                    print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
                    print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor,")
                    print("se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
                    print("")                
                    print("----------------------------------------------------------------------------")
            else:
                Pp = float(P)
                Ya = ((Pa0*Pb0)/Pp - Pa0)/(Pb0-Pa0)
                Xa = (Ya*Pb0)/(Pa0+(Pb0-Pa0)*Ya)           
                print("")
                print("--------------------------------------")            
                print("Fração molar Xa = ", round(Xa,n))
                print("")
                print("Fração molar Xb = ", round(1-Xa,n))
                print("")
                print("Fração molar Ya = ", round(Ya,n))
                print("")
                print("Fração molar Yb = ", round(1-Ya,n))
                print("")
                print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
                print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor,")
                print("se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
                print("")                
                print("----------------------------------------------------------------------------")


#6) Descobrir Xa/Ya um com o outro:

def Ya(*args):
    Xa = float(input("Insira a fração molar Xa:"))
    Pa0 = float(input("Insira a pressão de vapor de a:"))
    Pb0 = float(input("Insira a pressão de vapor de b:"))
    Ya = (Xa*Pa0)/(Pb0+(Pa0-Pb0)*Xa)
    print("")
    print("--------------------------------------")            
    print("Fração molar Ya = ", Ya)
    print("")
    print("Fração molar Xb = ", 1-Xa)
    print("")
    print("Fração molar Yb = ", 1-Ya)
    print("")
    print("----------------------------------------------------------------------------")
    

def Xa(*args):
    Ya = float(input("Insira a fração molar Ya:"))
    Pa0 = float(input("Insira a pressão de vapor de a:"))
    Pb0 = float(input("Insira a pressão de vapor de b:"))
    Xa = (Ya*Pb0)/(Pa0+(Pb0-Pa0)*Ya)
    print("")
    print("--------------------------------------")            
    print("Fração molar Xa = ", Xa)
    print("")
    print("Fração molar Xb = ", 1-Xa)
    print("")
    print("Fração molar Yb = ", 1-Ya)
    print("")
    print("----------------------------------------------------------------------------")



#7) Regra da alavanca:

regra_alavanca = lambda *num: Regra_alavanca(*num)

regra_da_alavanca = lambda *num: Regra_alavanca(*num)
    
Regra_da_alavanca = lambda *num: Regra_alavanca(*num)

def Regra_alavanca(*num):
    '''Retorna a função de regra da alavanca desejada.
    0 - Regra da alavanca para mols e frações molares
    1 - Regra da alavanca para massa
    2 - Regra da alavanca para sistemas sólidos eutéticos
    3 - Regra da alavanca para sistemas sólidos com intermediário'''

    if len(num) > 0:
        if num[0] == 0:
            return Regra_alavanca_mol()
        elif num[0]== 1:
            return Regra_alavanca_massa()
        elif num[0] == 2:
            return Regra_alavanca_eutetico()
        elif num[0] == 3:
            return Regra_alavanca_intermediario()

    print("Qual deseja acessar? - (Basta digitar o número) ")
    print("(0) Regra da alavanca para mols e frações molares ")
    print("(1) Regra da alavanca para massa")
    print("(2) Regra da alavanca para sistemas sólidos eutéticos ")
    print("(3) Regra da alavanca para sistemas sólidos com intermediário")
    print("")
    print("Para sair basta deixar em branco")
    choose_7 = input()
    print("")
    if choose_7 == '':
        return
    try:
        int(choose_7)
    except ValueError:
        return Regra_alavanca()
    if int(choose_7) not in [i for i in range(3+1)]:
        return Regra_alavanca()
    
    if int(choose_7) == 0:
        return Regra_alavanca_mol()
    if int(choose_7) == 1:
        return Regra_alavanca_massa()
    if int(choose_7) == 2:
        return Regra_alavanca_eutetico()
    if int(choose_7) == 3:
        return Regra_alavanca_intermediario()
    

def Regra_alavanca_mol(*arg):
    print("A regra da alavanca nos fornece o número de mols totais do sistema em cada fase")
    print("")
    print(" N^L + N^V = N")
    print(" N^L * (Za - Xa) = N^V * (Ya - Za)")
    print("Onde: N^L = Número de mols totais na fase líquida")
    print("e,    N^V = N^L = Número de mols totais na fase vapor")
    print("")
    if len(arg) == 4:
        N = float(arg[0])
        Xa = float(arg[1])    
        Ya = float(arg[2])
        Za = float(arg[3])
        N_V = N*(Za-Xa)/((Za-Xa)+(Ya-Za))
        N_L = N - N_V
        N_L_a = N_L*Xa
        N_L_b = N_L*(1-Xa)
        N_V_a = N_V*Ya
        N_V_b = N_V*(1-Ya)
        print("")
        print("-------------------------------------------------------------")            
        print("Número de mols totais na fase líquida N^L = ", N_L)
        print("")
        print("Número de mols de a na fase líquida Na^L = ", N_L_a)
        print("Número de mols de b na fase líquida Nb^L = ", N_L_b)
        print("")
        print("")
        print("Número de mols totais na fase vapor N^V = ", N_V)
        print("")
        print("Número de mols de a na fase vapor Na^V = ", N_V_a)
        print("Número de mols de b na fase vapor Nb^V = ", N_V_b)
        print("")
        print("N_L + N_V = N. Caso contrário, tem algo errado.")
        print("{} + {} = {}".format(N_L,N_V,N))
        print(N_L + N_V == N)
        print("-------------------------------------------------------------")
        print("")
        print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
        print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor, se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
        print("")
        print("----------------------------------------------------------------------------")
    else:     
        Nn = input("Insira o números de mols total do sistema: ")
        Xaa = input("Insira a fração molar Xa: ") 
        Yaa = input("Insira a fração molar Ya: ")
        Zaa = input("Insira a fração molar Za: ")
        if Nn == '' or Xaa == '' or Yaa == '' or Zaa == '':
            print("")
            print("Abortado. Todos os dados devem ser inseridos.")
            print("")
            print("")
            return Regra_alavanca()
        else:
            N = float(Nn)
            Xa = float(Xaa)    
            Ya = float(Yaa)
            Za = float(Zaa)              
            N_V = N/(1+((Ya-Za)/(Za-Xa)))
            N_L = N - N_V
            N_L_a = N_L*Xa
            N_L_b = N_L*(1-Xa)
            N_V_a = N_V*Ya
            N_V_b = N_V*(1-Ya)          
            print("")
            print("-------------------------------------------------------------")            
            print("Número de mols totais na fase líquida N^L = ", N_L)
            print("")
            print("Número de mols de a na fase líquida Na^L = ", N_L_a)
            print("Número de mols de b na fase líquida Nb^L = ", N_L_b)
            print("")
            print("")
            print("Número de mols totais na fase vapor N^V = ", N_V)
            print("")
            print("Número de mols de a na fase vapor Na^V = ", N_V_a)
            print("Número de mols de b na fase vapor Nb^V = ", N_V_b)
            print("")
            print("N_L + N_V = N. Caso contrário, tem algo errado.")
            print("{} + {} = {}".format(N_L,N_V,N))
            print(N_L+N_V == N)
            print("-------------------------------------------------------------")
            print("")
            print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
            print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor, se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
            print("")
            print("----------------------------------------------------------------------------")
            Regra_alavanca()
    


def Regra_alavanca_massa():
    print("")
    print("A regra da alavanca nos fornece a massa (percentagem ou kg) de cada fase do sistema")
    print("")
    print("Balanço de massa: ")
    print(" m(a) + m(b) = 100% ")
    print(" m_L + m_α = 100% ")
    print("")
    print("Onde: m(a,b) = massa do componente a,b ")
    print("e,    m_(L, α) = massa das fases líquida(L) e solida(α) ")
    print("")
    print("Regra da alavanca:")
    print(" m_L * (C_L - C_o) = m_α * (C_o - C_α) ")
    print(" m_L + m_α = 100% ")
    print("")
    print("Onde: C_o,L,α = Composição total, do liquido, do sólido ")
    print("")
    
    C_OO = input("Insira a massa/composição global de um componente (kg/%): ")
    C_LL = input("Insira a massa/composição na fase líquida desse componente (kg/%): ") 
    C_αα = input("Insira a massa/composição na fase sólida desse componente (kg/%): ")
    if C_LL == '' or C_OO == '' or C_αα == '':
        print("")
        print("Abortado. Todos os dados devem ser inseridos.")
        print("")
        print("")
        return Regra_alavanca()
    else:
        C_L = float(C_LL)
        C_O = float(C_OO)    
        C_α = float(C_αα)        
        m_L___m_α = (C_O - C_α)/(C_L - C_O)
        
        m_α = 100/(1+m_L___m_α)
        m_L = 100-m_α

        print('')
        print('')
        print("-------------------------------------------------------------")            
        print("Percentagem de massa na fase sólida (α) = ", m_α)
        print("")
        #print("Número de mols de a na fase líquida Na^L = ", N_L_a)
        #print("Número de mols de b na fase líquida Nb^L = ", N_L_b)
        #print("")
        print("Percentagem de massa na fase líquida (L) = ", m_L)
        print("")
        #print("Número de mols de a na fase vapor Na^V = ", N_V_a)
        #print("Número de mols de b na fase vapor Nb^V = ", N_V_b)
        #print("")
        print("m_L + m_α = 100%. Caso contrário, tem algo errado.")
        print("{} + {} = {}".format(m_L,m_α,'100%'))
        print(m_L+m_α == 100)
        print("-------------------------------------------------------------")
        print("")
        #print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
        #print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor, se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
        #print("")
        print("----------------------------------------------------------------------------")
        print('')
        return Regra_alavanca()




def Regra_alavanca_eutetico():
    linhas(5)
    print("")
    print("A regra da alavanca nos fornece a massa (% ou kg) de cada fase do sistema")
    print("")
    print("Balanço de massa: ")
    print(" m(a) + m(b) = 100% ")
    print(" m_L + m_α = 100% ")
    print("")
    print(" Onde: m(a,b) = massa do componente a,b --> OBS: diagrama em % de massa de b")
    print(" e,    m_(L, α) = massa das fases líquida(L) e solida(α) ")
    print("")
    print("Regra da alavanca:")
    print(" m_L * (C_L - C_O) = m_α * (C_O - 0)  -->  Se C_O < C_Ponto_eutético ")
    print(" m_L * (C_O - C_L) = m_α * (100 - C_O)  -->  Se C_O > C_Ponto_eutético ")    
    print(" m_L + m_α = 100% ")
    print("")
    print(" Onde: C_o,L,α = Composição total, do liquido, do sólido ")
    print(" C_O,L,α, bem como o ponto eutético, devem ser obtidos diretamente do diagrama")
    print('')
    print('')

    m = 4  # NÚMEROS CASA DECIMAIS NA RESPOSTA
    
    aa = input(" Opcional - Insira o componente a: ")
    bb = input(" Opcional - Insira o componente b: ")
    a = 'a' if aa == '' else aa
    b = 'b' if bb == '' else bb
    C_OO = input("Insira a massa/composição global do componente {} (kg/%): ".format(b))
    C_EE = input("Insira a massa/composição do ponto eutético da mistura (kg/%): ")
    C_LL = input(" Insira a massa/composição na fase líquida de {} (kg/%): ".format(b))

    try:
        C_O = float(C_OO)
        C_E = float(C_EE)
        C_L = float(C_LL)
    except ValueError:
        print("")
        print(" Abortado. Todos os dados devem ser inseridos.")
        print("")
        print("")
        return Regra_alavanca()
    
    if C_O == C_E:
        print('')
        print(" O sistema se encontra na concentração do ponto eutético, portanto ")
        print(" a regra da alavanca não é útil aqui; uma vez que a mudança de fase ")
        print(" será repentina.")
        linhas(4)
        return Regra_alavanca()

    elif C_O > C_E:
        k = (100)/(C_O - C_L)
        cristalprimario = b
    elif C_O < C_E:
        k = (C_O)/(C_L - C_O)
        cristalprimario = a
    
    m_α = 100/(1+k)
    m_L = 100-m_α

    mq = maxima_quantidade(C_O,C_E,m)
    max_m_α = mq[0]
    max_m_L = mq[1]

    if C_O < C_E: #À esquerda do ponto de eutético
        
        m_L_b = C_O
        m_L_a = C_O*100/C_L - C_O
        m_α_b = 0   
        m_α_a = m_α

    elif C_O > C_E: #À direita do ponto de eutético

        m_α_a = 0  
        m_α_b = m_α
        m_L_a = 100 - C_O if C_O > 1 else 1 - C_O
        m_L_b = m_L - m_L_a

    linhas(2)
    print("  {} É O CRISTAL PRIMÁRIO ".format(cristalprimario))
    print("  (a fase sólida é pura no cristal primário até a temperatura de eutético) ")
    print('')
    print(" A maior quantidade de {} que pode ser obtida é = {} (kg/%) ".format(cristalprimario,round(max_m_α,m)))
    linhas(1)
    print(" Então, a fase líquida residual seria = {} (kg/%) ".format(round(max_m_L,m)))
    linhas(1)
    print("------------------------------------------------------------------")            
    print('')
    print("            - - - ANÁLISE GERAL DO SISTEMA - - - ")
    print('')
    print("Massa/Percentagem de massa na fase sólida (α) = ", round(m_α,m))
    print('')
    print(" Massa/% de",a,"na fase sólida para composição de liquido {}% de {} = ".format(round(C_L,1),b), round(m_α_a,m))
    print(" Massa/% de",b,"na fase sólida para composição de liquido {}% de {} = ".format(round(C_L,1),b), round(m_α_b,m))
    print('')
    print("Massa/Percentagem de massa na fase líquida (L) = ", round(m_L,m))
    print('')
    print(" Massa/% de",a,"na fase líquida para composição de liquido {}% de {} = ".format(round(C_L,1),b), round(m_L_a,m))
    print(" Massa/% de",b,"na fase líquida para composição de liquido {}% de {} = ".format(round(C_L,1),b), round(m_L_b,m))
    print('')
    print('')
    print(" m_L + m_α = 100%. Caso contrário, tem algo errado.")
    print(" {} + {} = {}".format(m_L,m_α,'100%'))
    print( m_L+m_α == 100)
    print('')
    #print("------------------------------------------------------------------")
    print('')
    #print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
    #print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor, se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
    #print('')
    print("----------------------------------------------------------------------------")
    input('')
    return Regra_alavanca()



def Regra_alavanca_intermediario():
    linhas(5)
    print("")
    print("A regra da alavanca nos fornece a massa (% ou kg) de cada fase do sistema")
    print("")
    print("Balanço de massa: ")
    print(" m(a) + m(b) = 100% ")
    print(" m_L + m_α = 100% ")
    print("")
    print(" Onde: m(a,b) = massa do componente a,b --> OBS: diagrama em % de massa de b")
    print(" e,    m_(L, α) = massa das fases líquida(L) e solida(α) ")
    print("")
    print("Regra da alavanca:")
    print(" m_L * (C_L - C_O) = m_α * (C_O - 0)  -->  Se C_O < C_Ponto_eutético ")
    print(" m_L * (C_O - C_L) = m_α * (100 - C_O)  -->  Se C_O > C_Ponto_eutético ")    
    print(" m_L + m_α = 100% ")
    print("")
    print(" Onde: C_o,L,α = Composição total, do liquido, do sólido ")
    print(" C_O,L,α, bem como o ponto eutético, devem ser obtidos diretamente do diagrama")
    print('')
    print('')

    m = 4  # NÚMEROS CASA DECIMAIS NA RESPOSTA
    
    aa = input(" # Opcional - Insira o componente a: ")
    bb = input(" # Opcional - Insira o componente b: ")
    ii = input(" # Opcional - Insira o intermediário: ")
    print('')
    massaa = input(" # Opcional - Insira a massa total do sistema: ")

    a = 'a' if aa == '' else aa
    b = 'b' if bb == '' else bb
    interm = 'intermediario' if ii == '' else ii
    massa_total = float(massaa) if massaa != '' else 100
    
    C_OO = input(" Insira a massa/composição global do componente {} (kg/%): ".format(b))
    intermediarioo = input(" Insira a massa/composicao do intermediário:  (kg/%): ")
    print('')
    if intermediarioo == '' or C_OO == '':
        linhas(1)
        print(" Abortado. Todos os dados devem ser inseridos.")
        linhas(2)
        return Regra_alavanca()
    
    C_O = float(C_OO)
    intermediario = float(intermediarioo)
    if C_O > intermediario:
        E1 = interm
        E2 = b
    elif C_O < intermediario:
        E1 = a
        E2 = interm

    C_EE = input(" Insira a massa/composição do ponto eutético {} (kg/%): ".format(E1+'-'+E2))
    try:
        C_e = C_E = float(C_EE)
        if C_E < C_O:
            C_E = 'd'
            cristalprimario = E2
        elif C_E > C_O:
            C_E = 'e'
            cristalprimario = E1
        else:
            print('')
            print(" O sistema se encontra na concentração do ponto eutético, portanto ")
            print(" a regra da alavanca não é útil aqui; uma vez que a mudança de fase ")
            print(" aconterá de maneira invariante (composições e temperatura consatntes).")
            linhas(4)
            return Regra_alavanca()
    except ValueError:
        linhas(1)
        print(" Abortado. Todos os dados devem ser inseridos.")
        linhas(2)
        return Regra_alavanca()
    
    mq = maxima_quantidade_intermed(C_O,intermediario,C_e,m)
    max_m_α = mq[0]
    max_m_L = mq[1]
    C = mq[2] 

    print('')
    C_LL = input(" # Opcional - Insira a massa/composição na fase líquida (kg/% de {} ): ".format(b))
    restante = False
    
    try:
        C_L = float(C_LL)

        if C == 1: 
            k = C_O/(C_L - C_O)
            m_α = 100/(1+k)
            m_L = 100-m_α
            MB = 1
            m_L_b = ((100-intermediario)/m_L)*100
            m_L_a = 100 - m_L_b
            return 'não funcional'
        elif C == 2: #FUNCIONAL
            k = (intermediario - C_O)/(C_O - C_L)
            m_α = 100/(1+k)
            m_L = 100-m_α
            MA = (1-(C_O/intermediario))*100
            m_L_a = MA/m_L*100
            m_L_b = 100 - m_L_a
            
        elif C == 3:
            k = (C_O - intermediario)/(C_L - C_O)
            m_α = 100/(1+k)
            m_L = 100-m_α
            MB = (1-(C_O/intermediario))*100
            m_L_b = 1
            m_L_a = 100 - m_L_b
            return 'não funcional'
        elif C == 4: #FUNCIONAL
            k = (100 - C_O)/(C_O - C_L)
            m_α = 100/(1+k)
            m_L = 100-m_α
            MA = (100-C_O)/(100-intermediario)*100
            m_L_a = MA/m_L*100
            m_L_b = 100 - m_L_a

        massa_L = massa_total * m_L/100
        massa_L_a = massa_L * m_L_a/100
        massa_L_b = massa_L * m_L_b/100
        restante = True
        
    except ValueError:
        pass


    linhas(2)
    print("------------------------------------------------------------------")            
    print('')
    print("  {} É O CRISTAL PRIMÁRIO ".format(cristalprimario))
    print("  (a fase sólida é pura no cristal primário até a temperatura de eutético) ")
    print('')
    print(" A maior quantidade de {} que pode ser obtida é = {} (kg/%) ".format(cristalprimario,round(max_m_α,m)))
    linhas(2)
    print(" Então, a fase líquida residual seria = {} (kg/%) ".format(round(max_m_L,m)))
    linhas(2)

    if restante == True:
        print("------------------------------------------------------------------") 
        print('')
        print("            - - - ANÁLISE GERAL DO SISTEMA - - - ")
        print('')
        print("Massa/Percentagem de massa na fase sólida (α) = ", round(m_α,m))
        linhas(2)
        print("Massa/Percentagem de massa na fase líquida (L) = ", round(m_L,m))        
        print('')
        print(" Percentagem (%) de",E1,"na fase líquida = ", round(m_L_a,m))
        print(" Massa (kg) de",E1,"na fase líquida = ", round(massa_L_a,m))
        print('')
        print(" Percentagem (%) de",E2,"na fase líquida = ", round(m_L_b,m))
        print(" Massa (kg) de",E2,"na fase líquida = ", round(massa_L_b,m))
        linhas(2)
        print(" m_L + m_α = 100%. Caso contrário, tem algo errado.")
        print(" {} + {} = {}".format(m_L,m_α,'100%'))
        print( m_L+m_α == 100)
        print('')
    #print("------------------------------------------------------------------")
    print('')
    #print("OBS.: Números sem sentido podedm indicar que o sistema é monofásico.")
    #print("E portanto as equações não serão válidas, pois uma das frações molares, líquida ou vapor, se iguala à fração molar global (afinal, só há uma fase), e a outra fica indefinida.")
    #print('')
    print("----------------------------------------------------------------------------")
    input('')
    return Regra_alavanca()






#8)


def maxima_quantidade(CO,CE,m):
    '''Função que descobre a quantidade máxima de um composto puro que pode ser cristalizado'''

    if CO < CE:
        #ms(CO - 0) = ml(CE - CO)
        #ms/ml = k
        k = (CE - CO)/(CO - 0)
        c = 1
    elif CO > CE:
        #ms(100 - CO) = ml(CO - CE) 
        #ms/ml = k
        k = (CO - CE)/(100 - CO)
        c = 2
    m_L = 100/(1+k)
    m_α = 100-m_L    
    return m_α,m_L,c



def maxima_quantidade_intermed(CO,CI,CE,m):
    '''Função que descobre a quantidade máxima de um composto puro que pode ser cristalizado'''

    if CO < CI:
        if CO < CE:
            #ms(CO - 0) = ml(CE - CO)
            #ms/ml = k
            k = (CE - CO)/(CO - 0)
            c = 1
        elif CO > CE:
            #ms(CI - CO) = ml(CO - CE) 
            #ms/ml = k
            k = (CO - CE)/(CI - CO)
            c = 2
    elif CO > CI:
        if CO < CE:
            #ms(CO - CI) = ml(CE - CO)
            #ms/ml = k
            k = (CE - CO)/(CO - CI)
            c = 3
        elif CO > CE:
            #ms(100 - CO) = ml(CO - CE)
            #ms/ml = k
            k = (CO - CE)/(100 - CO)
            c = 4
    m_L = 100/(1+k)
    m_α = 100-m_L    
    return m_α,m_L,c




def sistema_com_intermediario(*arg):
    linhas(3)

    m = 4  # NÚMEROS CASA DECIMAIS NA RESPOSTA
    
    aa = input(" Opcional - Insira o componente a: ")
    bb = input(" Opcional - Insira o componente b: ")
    ii = input(" Opcional - Insira o intermediário: ")
    massaa = input(" Opcional - Insira a massa total do sistema: ")
    print('')
    a = 'a' if aa == '' else aa
    b = 'b' if bb == '' else bb
    interm = 'intermediario' if ii == '' else ii
    massa_total = float(massaa) if massaa != '' else 100
    
    C_OO = input(" Insira a massa/composição global do componente {} (kg/%): ".format(b))
    intermediarioo = input(" Insira a massa/composicao do intermediário:  (kg/%): ")

    if intermediarioo == '' or C_OO == '':
        print("")
        print(" Abortado. Todos os dados devem ser inseridos.")
        print("")
        print("")
        return sistema_com_intermediario()

    C_O = float(C_OO)
    intermediario = float(intermediarioo)
    inv_int = (100 - intermediario) if intermediario >= 1 else (1 - intermediario)
    
    if C_O < intermediario:
        cimabaixo = "à esquerda"
        componente = a
        C_b = (100 - C_O) if C_O >= 1 else (1 - C_O)
        C_a = (C_b * (inv_int)/intermediario)
        
    elif C_O > intermediario:
        componente = b
        cimabaixo = "à direita"
        C_a = (100 - C_O) if C_O >= 1 else (1 - C_O)
        C_b = (C_a * (inv_int)/intermediario)
        
    elif C_O == intermediario:
        C_b = intermediario
        linhas(5)
        print(" Massa/Composição de {} = ".format(a), round(C_a,m))
        print(" Massa/Composição de {} = ".format(b), round(C_b,m))
        print('')
        print(" Reagem e formama 100% de {}".format(interm))
        return
    
    C_I = C_a + C_b
    comp_componente = C_O - C_a if componente == a else C_O - C_b

    linhas(3)
    print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
    print('')
    print(" O sistema se encontra {} do intermediário ({})".format(cimabaixo,interm))
    print(" Para sua formação, reagem: \n\n {} (massa/%) de {} \n         com \n {} (massa/%) de {} ".format(round(C_a,m),a,round(C_b,m),b))
    print('')
    print(" E se forma {} (massa/%) de {} ".format(round(C_I,m),interm))
    print('')
    print('')
    print(" LOGO, ")
    print("       O sistema é composto por uma mistura de: \n {} (massa/%) de {}      com      {} (massa/%) de {}".format(round(comp_componente,m),componente,round(C_I,m),interm))
    
    













    
