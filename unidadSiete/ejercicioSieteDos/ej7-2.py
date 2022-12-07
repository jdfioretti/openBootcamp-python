from datetime import datetime
from lib2to3.pgen2.token import MINUS

ahora = datetime.now()
fecha = datetime.date(ahora)
anio = int(fecha.strftime("%Y"))
mes = int(fecha.strftime("%m"))
dia = int(fecha.strftime("%d"))

ir_a_casa = datetime(year=anio, month=mes, day=dia, hour=19, minute=00, second=00)

consultar = datetime.now().time().strftime("%H:%M:%S")
fecha = datetime(year=anio, month=mes, day=dia, hour=19, minute=00).strftime('%H:%M:%S')

if consultar >= fecha:
    print('Es hora de ir a casa')

else:
    consultar = ir_a_casa - ahora
    consultar = consultar.total_seconds()
    horas, restante = divmod(consultar, 3600)
    minutos, segundos = divmod(restante, 60)

    print(f'Para terminar tu turno te quedan  {int(horas)}  horas y  {int(minutos)} minutos')
    
    
    
