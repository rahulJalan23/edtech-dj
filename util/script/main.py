import csv
import json
import os

os.chdir(r'C:\X1_Enter\Web Development\community projects\edtech_dj\util')

def convert_to_json_data(csvFileName, jsonFileName):
    with open(f'csv/{csvFileName}.csv', 'r') as myFile:
        csv_reader = csv.DictReader(myFile)
        data = []
        for item in csv_reader:
            data.append(item)

        with open(f'json/{jsonFileName}.json', 'w') as myFile:
            json.dump(data, myFile, indent=4)

if __name__ == '__main__':
    convert_to_json_data("colleges", "colleges")