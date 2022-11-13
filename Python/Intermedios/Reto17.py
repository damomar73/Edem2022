from datetime import datetime
import time
 
if __name__ == '__main__': 
    milliseconds = time.time() * 1000
    print(f"> La hora actual en milisegundo es: {milliseconds}")
    date = datetime.now()
    print(f"> La hora actual es:", date.time().strftime("%H:%M:%S"))
