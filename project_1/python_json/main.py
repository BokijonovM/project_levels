import json
from datetime import datetime
import csv
import pickle


# METHODS OF HANDLERS:
# TRIM :
def trim(sensor):
    sensor["payload"] = "".join(sensor["payload"].rstrip().lstrip())
    return sensor


# PAD TO MULTIPLE:
def padToMultiple(sensor, output):
    ch = input("Choose char: ")
    n = input("Write number:")
    sensor["payload"] = sensor["payload"] + "".join([ch for i in range(int(n))])
    if output == 1:
        print(sensor)
    elif output == 2:
        saveToFile(sensor)


# TIME STAMP:
def addTimestamp(sensor, output):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    sensor["payload"] = sensor["payload"] + str(ts)
    if output == 1:
        print(sensor)
    elif output == 2:
        saveToFile(sensor)


# METHOD SAVING RECORD TO A FILE
def saveToFile(item):
    try:
        name = "sensor_ID" + item['sensor_id']
        file = open(name, 'wb')  # Trying to create a new file or open one
        pickle.dump(item, file)
        file.close()
    except:
        print('Something went wrong! Can\'t tell what?')


# MAIN PROGRAM:
# open a json db:
with open('sensors.json', 'r') as result:
    source = result.read()
    sensors = json.loads(source)

# enumeration a sensors json file( choose a property handler and output):
for item in sensors['sensor']:
    model = item['model']

    # WS-0001:
    if model == 'WS-0001':
        print("Found Model WS-0001:")
        print(item)

    # WS-0002:
    if model == 'WS-0002':
        print("Found Model WS-0002:")
        padToMultiple(item, 1)

    # WS-0003:
    if model == 'WS-0003':
        print("Found Model WS-0003:")
        # choosing handler and output
        handler = input("[1] Trim, [2] padMultiple:")
        if handler == '1':
            trim(item)
        elif handler == '2':
            padToMultiple(item, 2)

    # WS-0004:
    if model == 'WS-0004':
        print("Found Model WS-0004:")
        # choosing handler and output
        handler = input("[1] trim, [2] padToMultiple, [3]timestamp:")
        output = input("[1] console, [2] File:")

        if handler == '1' and output == '1':
            trim(item)
            # it should be something like trim(item,int(output)) instead of this:
        elif handler == '1' and output == '2':
            trim(item)
        elif handler == '2' and output == '1':
            padToMultiple(item, 1)
        elif handler == '2' and output == '2':
            padToMultiple(item, 2)
        elif handler == '3' and output == '1':
            addTimestamp(item, 1)
        elif handler == '3' and output == '2':
            addTimestamp(item, 2)

if __name__ == '__main__':
    print("a")
