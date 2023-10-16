from typing import List
import requests


class Station:
    def __init__(self, id, name, availableStands, availableBike, address, longitude, latitude) -> None:
        self.id = id
        self.name = name
        self.availableStands = availableStands
        self.availableBike = availableBike
        self.address = address
        self.longitude = longitude
        self.latitude = latitude


def __create_station_from_data(data) -> List[Station]:
    return Station(data['id'], data['name'], data['availableStands'], data['availableBike'], data['address'], data['longitude'], data['latitude'])


def get_bicloo_stations() -> List[Station]:
    url = "https://nantesv3.smartappscenter.com/Bike/api/bike"
    res = requests.get(url)
    data = res.json()
    stations = [__create_station_from_data(
        data=station) for station in data['result']]
    return sorted(stations, key=lambda x: x.id)
