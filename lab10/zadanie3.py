from datetime import datetime
from zoneinfo import ZoneInfo

def time_zones_check(time):
    time_parts = time.split(":")
    dt = datetime.now(ZoneInfo('Europe/Warsaw')).replace(hour=int(time_parts[0]), minute=int(time_parts[1]), second=int(time_parts[2]), microsecond=0)
    
    print(f"Tokyo: {dt.astimezone(tz=ZoneInfo('Asia/Tokyo')).strftime('%H:%M:%S')}")
    print(f"Londyn: {dt.astimezone(tz=ZoneInfo('Europe/London')).strftime('%H:%M:%S')}")
    print(f"Sydney: {dt.astimezone(tz=ZoneInfo('Australia/Sydney')).strftime('%H:%M:%S')}")
    print(f"Waszyngton: {dt.astimezone(tz=ZoneInfo('Etc/GMT+4')).strftime('%H:%M:%S')}")

time_zones_check(input("Podaj godzinę w formacie HH:MM:SS: "))
