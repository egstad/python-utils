import json
import os.path
import urllib.request
import time


# Edit vars below to adjust input location & name
DIR_NEW = 'database-new/'
DATA_NEW_NAME = 'database.json'
THROTTLE_TIME = 0.2

# Pipe old (input) database into var called data
with open(DIR_NEW + DATA_NEW_NAME, "r", encoding="utf-8") as database:
    data = json.load(database)


def init():
    """Loop through data and download the goods!"""
    for x in data:
        filename = os.path.join('exports', x["name"] + ' — ' + str(x["id"]) + '.jpg')

        if not os.path.isfile(filename):
            try:
                urllib.request.urlretrieve(x['image'], filename)
                print("✅ ID: " + str(x["id"])  + "(" + x["name"] + ") downloaded! ")
                time.sleep(THROTTLE_TIME)
            except NameError as inst:
                print("🛑 ID: " + str(x["id"])  + "(" + x["name"] + ") not downloaded! ")
                print(inst)
                # print('  Encountered unknown error. Continuing.')
