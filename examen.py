import os 
os.system("cls")

nompersona = input("ingrese su nombre: ")
apellpersona = input("ingrese su apellido: ")
fecha = input("ingrese la fecha: ")
rut = []
entradas = []
cantdisponible = []
Platinum = 120000
Gold = 80000
Silver = 50000
menu = """
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
"""
menucantidad = """
¿Cuantas Entradas Desea?
1. 1 Entrada
2. 2 Entrada
3. 3 Entrada
"""
menuentradas = """"
1. Platinum, $120.000. (Asientos del 1 al 20). 
2. Gold $80.000. (Asientos del 21 al 50). 
3. Silver $50.000. (Asientos del 51 al 100.)
"""
menudisponible = """"
 1  2  3  4  5  6  7  8  9 10
11 12 13  X  X  X 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40 
41 42 43 44 45 46 47 48 49 50
51 52 53 54 55 56 57 58 59 60 
61 62 63 64 65 66 67 68 69 70
71 72 73 74 75 76 77 78 79 80
81 82 83 84 85 86 87 88 89 90 
91 92 93 94 95 96 97 98 99 100
"""

while True:
    try:
        opc = int(input(menu))
        if menu == 5:  
            print(f"Ha deseado salir,{nompersona} {apellpersona} {fecha}, hasta pronto")
            break
        elif opc == 1:
            while True:
                try:
                    print(menucantidad)
                    entradas = int(input("Cuantas desea: "))
                    if entradas >= 1 and entradas < 4:                            
                        print(menudisponible)
                        print("97 asientos estan disponibles")
                        cantdisponible = int(input("¿Que asiento desea?: ")) 
                    if cantdisponible >= 1 or cantdisponible <=100:    
                        print("Asiento Disponible")
                        break
                    precios = print({menuentradas})
                    precios = int(input("Cual desea: "))
                    if entradas == 1:
                        Platinum >= 1 <= 20
                        totentradas = entradas * 120000
                        break
                    elif entradas == 2:
                        Gold >= 21 <= 50
                        totentradas = entradas * 80000
                        break
                    elif entradas == 3:
                        Silver >= 51 <= 100
                        totentradas = entradas * 50000
                        break
                    else:
                        print("opcion no valida")
                except:
                    print("ocurrio una excepcion")        

            while True:
                try:
                    rut = int(input("ingrese su rut sin puntos ni guion ni numero verificador: "))
                    if rut >= 10000000 and rut < 100000000:
                        break
                    elif print("Operacion realizada correctamente"):
                        break    
                    else:
                        print("opcion no valida")        
                except:
                    print("ocurrio una excepcion")    
        elif opc == 2:            
                while True:
                    try:
                        rut = int(input("ingrese su rut sin puntos ni guion ni numero verificador: "))
                        if rut >= 10000000 and rut < 100000000:
                            disponible = print(menudisponible)
                            print("97 asientos estan disponibles")
                            cantdisponible = int(input("¿Que asiento desea?: ")) 
                        if cantdisponible >= 1 or cantdisponible <=100:    
                            print("Asiento Disponible")
                            break
                        elif cantdisponible == 14 or 15 or 16:
                            print("No disponible")
                            break    
                        else:
                            print("numero de asiento incorrecto")
                    except:
                        print("ocurrio una excepcion")  
        elif opc == 3:
            busca = int(input("Código de 8 dígitos a buscar: "))
            print(f"Ha seleccionado buscar {busca} \n")
            print("|   Rut  |   Asiento   ")
            print("--+------------------+-") 
            for i in range(len(rut)):
                if busca == rut[i] and busca >= 10000000 and busca < 100000000:
                    print(f"|  {rut[i]:8d}     | {cantdisponible[i]:3s}   ")
                    print("--+------------------+------------+-----------+") 

    
    except:
        print("ocurrio una excepcion")    