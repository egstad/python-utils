"""Module converts CSV to  JSON"""
import os
import csv
import json


DIR = "data-new/"
FILE_NAME_OLD = "database.csv"
FILE_NAME_NEW = "database.json"


with open(DIR + FILE_NAME_NEW, "r+", encoding="utf-8") as FILE_JSON:
    with open(DIR + FILE_NAME_OLD, "r", encoding="utf-8") as FILE_CSV:
        fieldnames = ["index", "title", "content", "description"]
        reader = csv.DictReader(FILE_CSV, fieldnames)

        # open array manually
        FILE_JSON.write("[\n")
        # create rows
        for row in reader:
            json.dump(row, FILE_JSON)
            FILE_JSON.write(",\n")

        # remove the last comma and new line
        FILE_JSON.seek(FILE_JSON.seek(0, os.SEEK_END) - 2)
        # close array manually
        FILE_JSON.write("\n]")
