import logging
import pickle
from datetime import datetime
from flask_mysqldb import MySQL
from flask import Flask
import MySQLdb

app = Flask(__name__)
app.secret_key = "12345"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "test"

db = MySQL(app)


def trim(sensor, output):
    sensor["payload"] = "".join(sensor["payload"].rstrip().lstrip())
    if output == 'console':
        logging.error(sensor)
        return "Created", 201;
        return sensor
    elif output == 'file':
        savetofile(sensor)
        return "Created", 201;
    elif output == 'db':
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO sensors(model,payload) VALUES (%s,%s)", (sensor["model"], sensor["payload"]))
        info = cur.fetchone()
        db.connection.commit()
        return "Created", 201;
    elif output != 'file' and output != 'console' and output != 'db':
        return "Not found!", 404


# PADTOMULTIPLE:
def padToMultiple(sensor, output):
    ch = input("Choose your character: ")
    n = input("Write your number:")
    sensor["payload"] = sensor["payload"] + "".join([ch for i in range(int(n))]);
    if output == 'console':
        logging.error(sensor)
        return "Created", 201
    elif output == 'file':
        savetofile(sensor)
        return "Created", 201
    elif output == 'db':
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO sensors(model,payload) VALUES (%s,%s)", (sensor["model"], sensor["payload"]))
        info = cur.fetchone()
        db.connection.commit()
        return "Created", 201
    elif output != 'file' and output != 'console' and output != 'db':
        return "Not found!", 404


# TIMESTAMP:
def addTimestamp(sensor, output):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    sensor["payload"] = sensor["payload"] + str(ts)
    if output == 'console':
        logging.error(sensor)
        return "Created", 201
    elif output == 'file':
        savetofile(sensor)
        return "Created", 201
    elif output == 'db':
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO sensors(model,payload) VALUES (%s,%s)", (sensor["model"], sensor["payload"]))
        info = cur.fetchone()
        db.connection.commit()
        return "Created", 201
    elif output != 'file' and output != 'console' and output != 'db':
        return "Not found!", 404


def savetofile(item):
    try:
        logging.error(item)
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        name = item["model"] + str(ts)
        logging.error(name)
        file = open(name, 'wb')  # Trying to create a new file or open one
        pickle.dump(item, file)
        file.close()
        logging.error("saved to file!")
    except:
        logging.error("error!")
