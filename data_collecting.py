from bicloo_wrapper import get_bicloo_stations, Station
import os
import time
from datetime import datetime


def get_date_and_hour():
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    hour = now.strftime("%H:%M")
    return date, hour


def append_to_file(path: str, content: str):
    with open(path, "a") as file:
        file.write(content)


def init_folder_and_station_file():
    bicloo_stations: list[Station] = get_bicloo_stations()

    with open("data/stations.yml", 'w', encoding="utf-8") as file:
        content = [f"{s.id}: {s.name}\n" for s in bicloo_stations]
        file.writelines(content)

    for s in bicloo_stations:
        os.makedirs(f"data/{s.id}", exist_ok=True)


def main():
    while True:
        date, hour = get_date_and_hour()
        key_moment = (':00', ':15', ':30', ':45')
        if hour.endswith(key_moment):
            print(f"{hour}: key moment")
            bicloo_stations: list[Station] = get_bicloo_stations()
            date, hour = get_date_and_hour()
            for s in bicloo_stations:
                append_to_file(
                    path=f"data/{s.id}/{date}.txt",
                    content=f"\n{hour} | {s.availableBike}/{s.capacity}"
                )
            print(f"{hour}: done\n")
            time.sleep(13*60)
        else:
            time.sleep(5)


if __name__ == "__main__":
    init_folder_and_station_file()
    main()
