ventas = []

while True:
    print("Menu de analisis de ventas")
    print("1. Ingresar lista de ventas\n"
          "2. Mostrar todas las ventas ingresadas\n"
          "3. Calcular la ventas mas alta y mas baja\n"
          "4. Calcular promedio de ventas\n"
          "5. Contar cuantos dias superaron los Q. 1000\n"
          "6. Buscar si una venta existe\n"
          "7. Clasificar venta\n"
          "8. Salir")
    select = input("Selecciona una opcion: ")
    match select:
        case "1":
            while True:
                print("Ingresar ventas: \n"
                      "1. Ingresar ventas\n"
                      "2. Regresar al menu")
                select1 = input("Ingresar una opcion: ")
                match select1:
                    case "1":
                        sell = int(input("Ingresar precio de venta: "))
                        ventas.append(sell)
                    case "2":
                        print("Regresando al menu")
                        break
        case "2":
            print(f"\nventas")
        case "8":
            print("Saliendo")
            break