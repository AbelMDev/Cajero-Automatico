Simula el funcionamiento básico de un cajero automático.

El programa debe mostrar un menú con opciones y permitir al usuario realizar operaciones hasta que decida salir.

Usar bucles while para mantener el menú activo.

Usar condicionales if, elif, else para manejar las opciones.

Practicar variables acumulativas y entrada de datos.

Ejemplo código base:
saldo = 1000  # saldo inicial
opcion = 0
print("💰 Bienvenido a tu Cajero Automático")
while opcion != 4:
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))
Cocnsideraciones:
Agregar un sistema de PIN: antes de acceder al menú, el usuario debe ingresar una contraseña correcta

Registrar movimientos: guardar una lista con los depósitos y retiros realizados.

Opción de “ver historial”: mostrar los movimientos registrados.

Múltiples usuarios: permitir que varios usuarios (con diferentes PIN) usen el cajero.
