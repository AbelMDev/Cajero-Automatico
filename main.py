def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")


def solicitar_monto(mensaje):
    """Solicita un monto válido mayor a cero."""
    while True:
        try:
            monto = float(input(mensaje))
            if monto <= 0:
                print("❌ El monto debe ser mayor que cero.")
            else:
                return monto
        except ValueError:
            print("❌ Ingresa un valor numérico válido.")


# ----------------------------------------------------
# DEPÓSITO DE DINERO
# ----------------------------------------------------
def depositar_dinero(saldo, movimientos):
    try:
        monto = float(input("Ingrese el monto a depositar: "))
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        return saldo

    if monto <= 0:
        print("❌ El monto debe ser mayor que cero.")
        return saldo

    saldo += monto
    movimientos.append(monto)  # Registrar depósito

    print(f"✔ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    return saldo


# ----------------------------------------------------
# RETIRO DE DINERO
# ----------------------------------------------------
def retirar_dinero(saldo, movimientos):
    monto = solicitar_monto("Ingrese el monto a retirar: ")

    if monto > saldo:
        print("❌ Saldo insuficiente para realizar esta operación.")
        return saldo

    saldo -= monto
    movimientos.append(-monto)  # Registrar retiro como negativo

    print(f"✔ Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    return saldo


# ----------------------------------------------------
# CAJERO PRINCIPAL
# ----------------------------------------------------
def cajero():
    saldo = 1000.0
    pin_correcto = 1234
    intentos = 3
    movimientos = []

    print("💰 Bienvenido a tu Cajero Automático")
    
    # Validación de PIN
    while intentos > 0:
        try:
            pin_ingresado = int(input("Ingrese su código PIN: "))
        except ValueError:
            intentos -= 1
            print(f"❌ Solo se permiten números. Te quedan {intentos} intentos.")
            continue

        if pin_ingresado != pin_correcto:
            intentos -= 1
            print(f"❌ PIN incorrecto. Te quedan {intentos} intentos.")
        else:
            break

        if intentos == 0:
            print("🔒 Tarjeta bloqueada por seguridad.")
            return
    
    # Menú principal
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
                print(movimientos)

            case 2:
                saldo = depositar_dinero(saldo, movimientos)

            case 3:
                saldo = retirar_dinero(saldo, movimientos)

            case 4:
                print("👋 Gracias por usar el cajero. ¡Hasta luego!")
                break

            case _:
                print("❌ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    cajero()
