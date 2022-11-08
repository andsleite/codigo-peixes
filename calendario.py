# Módulos do calendário
import calendar
from datetime import datetime


# Data atual
atual = datetime.datetime.now() 

# Variáveis armazenam data atual
ano =  atual.year
mes = atual.month
dia = atual.day
hora = atual.hour
# Imprime o calendário
print(ano, mes, dia, hora)
print(f'\n{calendar.month(ano, mes)}\n{atual}\n')
