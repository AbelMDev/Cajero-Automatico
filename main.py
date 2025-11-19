def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir")

# ----------------------------------------------------
# SOLICITUD DE DINERO
# ----------------------------------------------------
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
    monto = solicitar_monto("Ingrese el monto a depositar: ")
    saldo += monto
    movimientos.append(f"Depósito: +${monto:.2f}")
    print(f"✔ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    return saldo


# ----------------------------------------------------
# RETIRO DE DINERO
# ----------------------------------------------------
def retirar_dinero(saldo, movimientos):
    monto = solicitar_monto("Ingrese el monto a retirar: ")

    if monto > saldo:
        print("❌ Saldo insuficiente.")
        return saldo

    saldo -= monto
    movimientos.append(f"Retiro: -${monto:.2f}")
    print(f"✔ Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    return saldo


# ----------------------------------------------------
# CAJERO PRINCIPAL
# ----------------------------------------------------
def cajero():

    # Múltiples usuarios: PIN → datos
    usuarios = {
        1234: {"saldo": 1000.0, "movimientos": []},
        4567: {"saldo": 550.0, "movimientos": []},
        7890: {"saldo": 2500.0, "movimientos": []},
    }

    print("💰 Bienvenido a tu Cajero Automático")

    # --- Validación de PIN ---
    intentos = 3
    usuario_actual = None

    while intentos > 0:
        try:
            pin = int(input("Ingrese su código PIN: "))
        except ValueError:
            intentos -= 1
            print(f"❌ Solo números. Intentos restantes: {intentos}")
            continue

        if pin in usuarios:
            usuario_actual = usuarios[pin]
            print("✔ Acceso concedido.")
            break
        else:
            intentos -= 1
            print(f"❌ PIN incorrecto. Intentos restantes: {intentos}")

    if intentos == 0:
        print("🔒 Cuenta bloqueada por seguridad.")
        return

    saldo = usuario_actual["saldo"]
    movimientos = usuario_actual["movimientos"]

    # --- Menú principal ---
    opcion = 0
    while opcion != 5:
        mostrar_menu()

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("❌ Debes ingresar un número del 1 al 5.")
            continue

        if opcion == 1:
            print(f"💳 Tu saldo es: ${saldo:.2f}")

        elif opcion == 2:
            saldo = depositar_dinero(saldo, movimientos)

        elif opcion == 3:
            saldo = retirar_dinero(saldo, movimientos)

        elif opcion == 4:
            print("\n🧾 HISTORIAL DE MOVIMIENTOS:")
            if not movimientos:
                print("No hay movimientos registrados.")
            else:
                for mov in movimientos:
                    print(" -", mov)

        elif opcion == 5:
            print("👋 Gracias por usar el cajero. ¡Hasta luego!")

        else:
            print("❌ Opción inválida.")

    # Guardar cambios
    usuario_actual["saldo"] = saldo


if __name__ == "__main__":
    cajero()
