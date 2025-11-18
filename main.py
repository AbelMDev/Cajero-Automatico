def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")


def solicitar_monto(mensaje):
    while True:
        try:
            monto = float(input(mensaje))
            if monto <= 0:
                print("❌ El monto debe ser mayor que cero.")
            else:
                return monto
        except ValueError:
            print("❌ Ingresa un valor numérico válido.")


# ----------------------------------------
# FUNCIÓN AGREGADA POR CRISTIAN (TU OPCIÓN 2)
# ----------------------------------------
def depositar_dinero(saldo):
    """Función creada por Cristian para manejar la opción 2: depósito de dinero."""
    try:
        monto = float(input("Ingrese el monto a depositar: "))
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        return saldo

    if monto <= 0:
        print("❌ El monto debe ser mayor que cero.")
        return saldo

    saldo += monto
    print(f"✔ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    return saldo
# ----------------------------------------


def cajero():
    saldo = 1000.0
    pin_correcto = 1234
    intentos = 3
    
    print("💰 Bienvenido a tu Cajero Automático")
    
    while intentos > 0:
        try:
            pin_ingresado = int(input("Ingrese su código PIN: "))
        except ValueError:
            intentos -= 1
            print(f"❌ Solo se permiten números. Te quedan {intentos} intentos.")
            if intentos == 0:
                print("🔒 Tarjeta bloqueada por seguridad.")
                return
            continue

        if pin_ingresado != pin_correcto:
            intentos -= 1
            print(f"❌ PIN incorrecto. Te quedan {intentos} intentos.")
            if intentos == 0:
                print("🔒 Tarjeta bloqueada por seguridad.")
                return
        else:
            break
    
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("❌ Debes ingresar un número del 1 al 4.")
            continue

        match opcion:
            case 1:
                print(f"💳 Tu saldo actual es: ${saldo:.2f}")

            case 2:
                saldo = depositar_dinero(saldo)  # <--- AQUI VA TU APORTACIÓN

            case 3:
                monto = solicitar_monto("Ingrese el monto a retirar: ")
                if monto > saldo:
                    print("❌ Saldo insuficiente para realizar esta operación.")
                else:
                    saldo -= monto
                    print(f"✔ Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

            case 4:
                print("👋 Gracias por usar el cajero. ¡Hasta luego!")
                break

            case _:
                print("❌ Opción inválida. Intente nuevamente.")
