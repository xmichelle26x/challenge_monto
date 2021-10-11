def pedir_salario():  
    while(True):
        try:
            valor = "{:.2f}".format(float(input()))
            break
        except ValueError:
            print('Error, introduce un numero')
    return valor
     

def pedir_numero():  
    while(True):
        try:
            numero = int(input())
            break
        except ValueError:
            print('Error, introduce un numero')
    return numero


def pedir_plazo(): 
	while(True):
		try:
			mes = int(input())
			if(mes==12 or mes==24 or mes==36 or mes==48):
				break
		except ValueError:
			print('Error, introduce una cantidad de meses de la lista')
	return mes

      
def calcular_cuota_por_categoria(salario):
	while True:
		print ("1. BUENO - 2. MALO - 3. REGULAR")
		print("Introduce un numero de categoría: ")
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
			print ("Introduce un numero entre 1 y 3")
	return cuota


def montoCrédito(cuota, meses):
    año = meses/12
    monto = cuota * (1-(1+0.15/12)**(-12*año)) / (0.15/12)
    return monto    
    

if __name__ == "__main__": 
	try:
		print ("Ingrese el valor de su salario:")
		salario = pedir_salario()
		print("\n")
		
		cuota = calcular_cuota_por_categoria(salario) 
		print("\nIngrese la cantidad de meses 12-24-36-48 meses:")
		meses = pedir_plazo()
		
		print("\n------------------------------------------------------\n")
		
		print("Monto del crédito: {:.2f} USD".format(montoCrédito(cuota, meses)),"\n")
		print("Cuota: {:.2f} USD".format(cuota),"\n")
		print("Plazo: ",meses, "meses")
		
	except Exception as error:
		print('error', error)
	
