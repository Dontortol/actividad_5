ventas = []

while True:
    print("Menu de analisis de ventas")
    print("1. Ingresar lis"
          "ta de ventas\n"
          "2. Mostrar todas las ventas ingresadas\n"
          "3. Calcular la ventas mas alta y mas baja\n"
          "4. Calcular promedio de ventas\n"
          "5. Contar cuantos dias superaron los Q. 1000\n"
          "6. Clasificar venta\n"
          "7. Salir\n")
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
                        print("Venta agregada")
                    case "2":
                        print("Regresando al menu")
                        break
                    case _:
                        print("Ingrese una opcion valida")
        case "2":
            print(f"\n{ventas}\n"
                  f"")
        case "3":
            for i in ventas:
                print(f"Venta mas alta: {max(ventas)}\n"
                      f"venta mas baja: {min(ventas)}\n ")
                break
        case "4":
            print(f"el promedio de ventas es: Q. {sum(ventas)/len(ventas)}\n"
                  f"")
        case "5":
            view_sells = 0
            for i in ventas:
                if not i >= 1000:
                    print("No hubieron ventas mayores a Q.1000")
                else:
                    view_sells += 1
                    print(f"cantidad de dias donde la venta fue mayor a Q.1000: dia {view_sells}")
        case "6":
            clacified = {
            "alto" : [],
            "medio" : [],
            "bajo" : []
            }

            for c in ventas:
                if c > 1000:
                    clacified["alto"].append(c)
                    print("Alto: ", clacified["alto"])
                elif c >= 500 and c <= 999:
                    clacified["medio"].append(c)
                    print("Medio: ", clacified["medio"])
                elif c >= 0 and c <= 499:
                    clacified["bajo"].append(c)
                    print("Bajo: ", clacified["bajo"])


        case "7":
            print("Saliendo")
            break