import pvlib
from datetime import datetime, timedelta
import pytz
import pandas as pd

# Define la ubicación con sus coordenadas y la zona horaria
latitude = 6.0670
longitude = -75.5784
tz = 'America/Bogota'

# Crear un objeto de ubicación
location = pvlib.location.Location(latitude, longitude, tz=tz)

# Crear un rango de horas en un día específico
start = datetime(2024, 4, 18, 6, 0, tzinfo=pytz.timezone(tz))  # Desde las 6 AM
end = datetime(2024, 4, 18, 18, 0, tzinfo=pytz.timezone(tz))   # Hasta las 6 PM
daterange = pd.date_range(start, end, freq='0.5h')


# Obtener la posición solar para cada hora en el rango
solar_positions = location.get_solarposition(daterange)

# Imprimir los resultados
print(solar_positions[['apparent_zenith', 'azimuth']])
