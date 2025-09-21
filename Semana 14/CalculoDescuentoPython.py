def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento según el porcentaje especificado.
    :param monto_total: float - Monto total de la compra.
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto 10%).
    :return: float - Monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# ---- Programa Principal ----
# Primera llamada: usando el descuento por defecto (10%)
monto_compra1 = 150.0
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

print("Compra 1:")
print(f"Monto total: ${monto_compra1:.2f}")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}")
print("-" * 40)

# Segunda llamada: usando un descuento proporcionado por el usuario (por ejemplo, 20%)
monto_compra2 = 300.0
descuento2 = calcular_descuento(monto_compra2, 20)
monto_final2 = monto_compra2 - descuento2

print("Compra 2:")
print(f"Monto total: ${monto_compra2:.2f}")
print(f"Descuento aplicado: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
