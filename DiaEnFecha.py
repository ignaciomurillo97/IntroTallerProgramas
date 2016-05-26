# Calcular el dia a partir de la fecha

diasPorMes = [31,28,31,30,31,30,31, 31, 31, 31, 30, 31]
diasDeLaSemana = ["Lunes", "Martes", "Mercoles","Jueves","Viernes",]

def diaEnFecha(dia, mes, año):
    totalDias = dia
    año -=1
    totalDias += (año - año // 4) * 365 + (año//4)*366
    
    if (año%4 == 0 and mes == 2):
        totalDias += 29
        print("Viciesto!")

    else:
        totalDias += diasPorMes[mes - 1]
    print(totalDias)
    print(diasDeLaSemana[totalDias%7 - 1])
