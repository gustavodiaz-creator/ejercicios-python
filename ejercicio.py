print("--- Sistema de Acceso a la Montaña Rusa --- \n")

edad = int(input("¿Cuál es tu edad?: "))
estatura = int(input("¿Cuál es tu estatura en cm?: "))
pase_vip = input("¿Tienes pase VIP? (si/no): ").lower()

if edad >= 12 and estatura >= 150:
    print("\n¡Puedes ingresar solo a la atracción!")

elif edad >= 8 or pase_vip == "si":
    print("\nPuedes ingresar, pero debes ir acompañado de un adulto.")

else:
    print("\nLo sentimos, no cumples con los requisitos mínimos para ingresar.")

if not pase_vip == "si":
    print("Nota: Te recomendamos adquirir el pase VIP para evitar filas y obtener ingresos especiales.")

print("\nFin del programa.")