def Suma_B_N(Num1, Num2, Base): #suma dos numeros en cualquier base
    if not (isinstance(Num1, list) and isinstance(Num2, list)):
        return "Error: ambos numeros deben ser listas"
    elif len(Num1) != len(Num2):
        return "Error: Numeros de laongitud distinta"
    elif not isinstance(Base, int):
        return "Error: la base debe ser un numero entero"
    else:
        return Suma_B_N_aux(Num1, Num2, Base, 0)

def Suma_B_N_aux(Num1, Num2, Base, acarreo):
    if Num1 == []:
        if acarreo == 0:
            return []
        else:
            return [acarreo]
    elif (Num1[-1]+Num2[-1]+acarreo) >= Base:
        return Suma_B_N_aux(Num1[:-1], Num2[:-1], Base, 1)+[(Num1[-1]+Num2[-1]+acarreo)-Base]
    else:
        return Suma_B_N_aux(Num1[:-1], Num2[:-1], Base, 0)+[(Num1[-1]+Num2[-1]+acarreo)]
