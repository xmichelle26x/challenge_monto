from functions import * 

if __name__ == "__main__": 
	try:
		print ("Ingrese el valor de su salario:")
		salario = pedir_salario()
		print("\n")
		
		cuota = calcular_cuota_por_categoria(salario) 
		print("\nIngrese la cantidad de meses 12-24-36-48 meses:")
		meses = pedir_plazo()
		
		print("\n------------------------------------------------------\n")
		
		print("Monto del crédito: {:.2f} USD".format(calcular_monto_crédito(cuota, meses)),"\n")
		print("Cuota: {:.2f} USD".format(cuota),"\n")
		print("Plazo: ",meses, "meses")
		
	except Exception as error:
		print('error', error)
	
