#valida el salario ingresado
def pedir_salario():  
    while(True):
        try:
            valor = "{:.2f}".format(float(input()))
            break
        except ValueError:
            print('Error, introduzca un numero')
    return valor
     

#valida el número de categoría ingresado
def pedir_numero():  
    while(True):
        try:
            numero = int(input())
            break
        except ValueError:
            print('Error, introduzca un numero')
    return numero


#valida el valor del mes ingresado
def pedir_plazo(): 
	while(True):
		try:
			mes = int(input())
			if(mes==12 or mes==24 or mes==36 or mes==48):
				break
		except ValueError:
			print('Error, introduzca una cantidad de meses de la lista')
	return mes


#calcula el valor de la cuota según la categoría ingresada
def calcular_cuota_por_categoria(salario):
	while True:
		print ("1. BUENO - 2. MALO - 3. REGULAR")
		print("introduzca un numero de categoría: ")
		categoria = pedir_numero() 
		cuota = 0
		if categoria == 1:
			print ("El % de sueldo DISPONIBLE para cuota es de 50\n")
			cuota = float(salario) * 0.50
			break
		elif categoria == 2:
			print ("El % de sueldo DISPONIBLE para cuota es de 12,5\n")
			cuota = float(salario) * 0.125  
			break
		elif categoria == 3:
			print("El % de sueldo DISPONIBLE para cuota es de 25\n")
			cuota = float(salario) * 0.25
			break
		else:
			print ("introduzca un numero entre 1 y 3")
	return cuota


#calcula el monto total del crédito según los datos de entrada
#aplicando la fórmula de monto
#monto = cuota * (1-(1+interes_anual/compendios_por_año)**(-compendios_por_año*duracion_pago_en_años)) / (interes_anual/compendios_por_año) 
def calcular_monto_crédito(cuota, meses):
    año = meses/12
    monto = cuota * (1-(1+0.15/12)**(-12*año)) / (0.15/12)
    return monto 