entrada = input("¿Me prestarias una feria?")
while entrada.lower()  == "si":
 print("muchas gracias por hacerme valer hermano")
 entrada = input("Quieres prestarme otra vez una feria")
 if entrada == "no":
  print("Arre, ahi se ven los canales")
  
  

#Usted realizará una fiesta, e invitará un nombre de invitados, no sabe cuales, entonces cree un programa para 
#agregar invitados, y deten el programa hasta que el usuario decida no agregar más invitados.

invitados = []

print("¡Bienvenido al programa para agregar invitados a tu fiesta!")

while True:
  
    invitado = input("Ingresa el nombre del invitado: ")
    invitados.append(invitado)
    
    continuar = input("¿Quieres agregar otro invitado? (si/no): ").strip().lower()
    if continuar == 'no': 
        break

print("\nLista de invitados:")
for i, nombre in enumerate(invitados, start=1):
    print(f"{i}. {nombre}")

print("\n¡El programa ha terminado!")


#Pida al usuario un numero entre 5 y 10, si el numero que dio el usuario no esta en el rango, 
#dile al usuario que no esta en ese rango y pida que ingrese un valor en el rango. repita hasta que se cumpla la condición.

def pedir_numero_en_rango():
    # Iniciando un bucle
    while True:
  
        numero = input("Ingresa un número entre 5 y 10: ")
        try:
          
            numero = int(numero)
          
            if 5 <= numero <= 10:
                print("¡Chido hermanito, si sabes leer!")
                break
            else:
                print("No manches carnal, no te pases de vivo te voy a filerar, agrega un  numero bueno, last chance.")
        except ValueError as e:
            
            print("Eso no es un número válido. Por favor, intenta de nuevo.")
            print(f"ERROR: {e}")
        finally:
            print("Esto se ejecuta siempre.")

    return numero

print(f"El número ingresado es: {pedir_numero_en_rango()}")


#Escriba la diferencia entre el ciclo for y el ciclo while.

def definicion_for():
    print("El ciclo 'for' se usa cuando sabes cuántas veces quieres repetir algo. Por ejemplo, recorrer una lista o un rango definido.")

def definicion_while():
    print("El ciclo 'while' se usa cuando no sabes cuántas veces repetir algo, pero tienes una condición que debe cumplirse para continuar.")

opcion = input("Escribe 'for' o 'while' para conocer su definición: ").strip().lower()

# Mostrar la definición según la elección
if opcion == "for":
    definicion_for()
elif opcion == "while":
    definicion_while()
else:
    print("Opción no válida. Por favor, elige entre 'for' o 'while'.")


  