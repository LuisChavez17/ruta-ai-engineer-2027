hrs = input("Ingrese las horas: ")
tarifa = input("Ingrese la tarifa por hora: ")

h = float(hrs)
t = float(tarifa)

if h <= 40:
    pago = h * t
else:
    horas_normales = 40 * t
    horas_extra = (h - 40) * (t * 1.5)
    pago = horas_normales + horas_extra

print(pago)
