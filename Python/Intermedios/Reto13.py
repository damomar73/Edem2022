from datetime import datetime, timedelta

def obtener_tiempo_transcurrido(segundos):
    dias = int(segundos / 60 / 60 / 24)
    segundos -= dias * 60 * 60 * 24
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos"


ahora = datetime.now()
futuro = ahora + timedelta(hours=50, seconds=925)
diferencia = futuro-ahora

if __name__ == "__main__":
    difFecha = obtener_tiempo_transcurrido(diferencia.total_seconds())
    print(f"> La fecha actual es: {ahora}")
    print(f"> La fecha futura es: {futuro}")
    print(f"> La diferencia de fechas es: {difFecha}")
