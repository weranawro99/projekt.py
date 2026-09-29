from datetime import datetime
to_celsius = lambda temp: round( temp - 273.15 , 2)
#Utwórz funkcję, która przelicza m / s na km / h
to_kmh = lambda speed: round( speed * 3.6 , 2)
aktualna_data = lambda: datetime.now().strftime("%Y-%m-%d %H-%M-%S")
