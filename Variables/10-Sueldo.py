def calcular_salario(salario_diario, dias_trabajados):
    salario_final = salario_diario * dias_trabajados

    descuento_pension = salario_final * 0.10
    descuento_salud = salario_final * 0.15

    salario_neto = salario_final - descuento_pension - descuento_salud
    return salario_neto

def main():
    try:
        salario_diario = float(input("Ingrese el salario diario del empleado: "))
        dias_trabajados = int(input("Ingrese el número de días trabajados: "))

        if salario_diario <= 0 or dias_trabajados <= 0:
            print("Error: El salario diario y los días trabajados deben ser mayores a cero.")
            return
        
        salario_total = calcular_salario(salario_diario, dias_trabajados)

        print("El salario total a pagar al empleado es:", salario_total)

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
main()
