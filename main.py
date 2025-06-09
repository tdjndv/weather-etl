import util
import pandas as pd
from datetime import datetime, timezone
import sqlite3

api_key = 'f6ef13ecdb369e587a438ee1a3a1465f'

l = []

postal_prefix = ""

print("This application is to tract weather reports from around the world using postal prefix and ISO 3166-1 A-2 country code")
print("For more information visit https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes")
print("Type *** when asked to enter location postal prefix to quit the program")
print("List of data is stored in a database SQLite that will be created when program terminates")

while True:
    postal_prefix = input("Enter location postal prefix: ")

    if postal_prefix == '***':
        break

    country_code = input("ISO 3166-1 A-2 country code: ")

    info = util.get_lat_lon(postal_prefix, country_code, api_key, False)

    data = util.get_weather(info, api_key, False, "metric")
    l.append(util.default_format(data))

    df = pd.DataFrame(l)
    print(df)

conn = sqlite3.connect('location.db')
df.to_sql('weather', conn, if_exists='replace', index=False)
conn.close()

print(df)
print("All data has been output to location.db")
print("Have a great day!")