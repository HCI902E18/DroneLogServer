import glob
from datetime import datetime


class LogFiles(object):
    def __init__(self, file=None):
        self.file = file

    def get_folder(self, file):
        _, folder, file = file.split('\\')
        return folder

    def folders(self):
        files = glob.glob('./logs/**/flight_log.json')
        return sorted([self.get_folder(file) for file in files], key=lambda day: datetime.strptime(
            day,
            '[%d-%m-%Y][%H.%M.%S]'
        ), reverse=True)
