def Suma_B_N(Num1, Num2, Base): #suma dos numeros en cualquier base
    if not (isinstance(Num1, list) and isinstance(Num2, list)): #verifica si las dos primeras entradas son listas
        return "Error: ambos numeros deben ser listas"
    elif len(Num1) != len(Num2): #verifica si ambas litas tienen la misma longitud
        return "Error: Numeros de laongitud distinta"
    elif not isinstance(Base, int): #verifica si la base es un numero entero
        return "Error: la base debe ser un numero entero"
    else:
        return Suma_B_N_aux(Num1, Num2, Base, 0)

def Suma_B_N_aux(Num1, Num2, Base, acarreo):
    if Num1 == []:
        if acarreo == 0: #si el acarreo es 0 no concatena ningun elemento
            return []
        else:
            return [acarreo] #si el acarreo no es cero lo agrega a la pila y la retorna
    elif (Num1[-1]+Num2[-1]+acarreo) >= Base:
        return Suma_B_N_aux(Num1[:-1], Num2[:-1], Base, 1)+[(Num1[-1]+Num2[-1]+acarreo)-Base] #si la suma de los elementos mas el acarreo supera la base, concatena la suma de estos menos la base y llama la funcion con las listas cortadas y el acarreo en 1
    else:
        return Suma_B_N_aux(Num1[:-1], Num2[:-1], Base, 0)+[(Num1[-1]+Num2[-1]+acarreo)]
