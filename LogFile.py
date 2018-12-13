import json


class LogFile(object):
    def __init__(self, folder):
        self.folder = folder

    @staticmethod
    def log_map(data, idx, len_):
        return {
            'lat': data['position']['latitude'],
            'lon': data['position']['longitude'],
            'flyingState': data['flyingState']
        }

    @staticmethod
    def valid(data):
        return data['position']['latitude'] is not None

    def data(self):
        with open(f'logs/{self.folder}/flight_log.json', 'r') as f:
            points = json.loads(f.read())
            return [self.log_map(point, idx, len(points)) for idx, point in enumerate(points) if self.valid(point)]
