# convertir soles a dolares.
# cambio:empresa Global Change

# 1. solicitar ingreso monto en moneda soles
monto_soles = float(input("Ingrese el monto en soles (PEN): "))

# 2. tasa actual en el peru (ejemplo: 1 USD = 3.85 PEN)
tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = X PEN): "))

# 3. Calcular el monto ingresado en dolares
monto_dolares = monto_soles / tasa_cambio

# 4. Mostrar el resultado solo considerando 02 decimales despues del punto
print("\n--- Conversión en Global Change ---")
print(f"Monto en soles: S/ {monto_soles:.2f}")
print(f"Tasa de cambio: 1 USD = {tasa_cambio:.2f} PEN")
print(f"Equivalente en dólares: $ {monto_dolares:.2f}")