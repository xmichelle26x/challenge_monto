# Challenge técnico
Programa que permita calcular el monto máximo para un crédito, dados el sueldo, la categoría del cliente y plazo (en meses) 

## -------->Datos de entrada

Sueldo: valor numérico de hasta 2 decimales ----> Ejemplo: 1000

Categoría: Enum (MALO, BUENO o REGULAR) ----> Ejemplo: MALO

Rangos de plazo: 12 meses, 24 meses, 36 meses o 48 meses ----> Ejemplo: 48



## -------->Parámetros del programa:

Capacidad de PAGO:

CATEGORIA CLIENTE	% de sueldo DISPONIBLE para cuota
BUENO	50
MALO	12,5
REGULAR	25

Ejemplo: si el sueldo es 1000 y la categoria es MALO, puede pagar una cuota de hasta 125 USD

## ------->Datos de salida:

Monto del crédito: 4491.44 USD

Cuota : 125 USD (no debe exceder el valor definido con la tabla: Capacidad de PAGO:)

Plazo: 48 meses


## Consideraciones:
Amortización: siempre FRANCESA

Interés: 15% anual

Todos los decimales ajustados a 2 dígitos

## Ejemplo 
![Ejemplo práctico](https://github.com/xmichelle26x/challenge_monto/blob/main/ejemplo/ejemplo.JPG)
