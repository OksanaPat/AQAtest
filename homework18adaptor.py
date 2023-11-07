import csv
import json


class JSONConverter:
    def __init__(self):
        self.__data = []

    def read_file(self, filename):
        with open(filename, 'r') as json_file:
            self.__data = json.load(json_file)

    def write_file(self, filename):
        with open(filename, 'w') as writer:
            headers = self.__data[0].keys() if self.__data else []
            csv_writer = csv.DictWriter(writer, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(self.__data)
            self.cleanup()

    def cleanup(self):
        self.__data = []


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example_reverse.csv')
converter.read_file('example2.json')
converter.write_file('example2_reverse.csv')