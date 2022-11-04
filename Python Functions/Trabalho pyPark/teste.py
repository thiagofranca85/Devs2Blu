# Este arquivo foi criado SEPARADO apenas pra entender como fazer o calculo de horas e converter 
# o resultado das horas em um numero float pra calcular o valor
# As IDEIAS desse arquivo foram usadas no controller pra adaptar os calculos dentro do pyPark
from datetime import date, datetime, time

# Pega Data e Horário Atual do Sistema
horaAtual = datetime.now()

# Input de Hora e Minutos pra Hora de Entrada
EntradaHora = int(input("Digite a hora de entrada: "))
EntradaMinuto = int(input("E os minutos: "))

# Salva o Horário de Entrada em Horas e Minutos
horaEntrada = datetime.combine(date.today(), time(EntradaHora, EntradaMinuto)) 
# Salva o Horário de Saída em Horas e Minutos usando o horaAtual.hour e horaAtual.minute como parametros.
horaSaidaAtual = datetime.combine(date.today(), time(horaAtual.hour, horaAtual.minute))

# Hora de Saída recebe a Hora Atual menos a Hora de Entrada
horaSaida = horaSaidaAtual - horaEntrada

# Transforma a horaSaida em segundos e cria um numero float para trabalhar com valores
calcHora = (horaSaida.seconds/60)/60

# Aqui algumas tentativas de IFs somando valor
valor = 0
if calcHora < 1:
    valor = 5
    print(f"O carro ficou estacionado por {horaSaida.seconds/60} minutos.")
elif calcHora < 2:
    valor = 10
    print(f"O carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} hora(s).")
elif calcHora > 2:
    valor = ((round(calcHora) * 2) - 4) + 10
    print(f"O carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} horas.")

print(f"Valor R${valor:.2f}")

# Print do horario da Saída
print(f"Tempo Estacionado: {(horaSaida.seconds/60)/60:.1f} hora(s).")