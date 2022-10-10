#reto 16 - NIVEL FACIL
def retof16():
  from datetime import date, timedelta
  current_date = date.today()
  print("Dia actual: ", current_date)
  print("Hace una semana : ", current_date - timedelta(7))