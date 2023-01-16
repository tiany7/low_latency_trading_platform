import pymysql
import os
import sys
import yaml
import json
import time
import datetime

class DBService:
    def __init__(self):
        self.config = {}
        with open("./config.yaml", 'r') as stream:
            self.config = yaml.load(stream)['database']

        print(self.config)
        self.db = pymysql.connect(host=self.config['host'], port=self.config['port'], user=self.config['user'], passwd=self.config['password'], charset='utf8')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def select(self, sql):
        self.db.ping(reconnect=True)
        cur = self.db.cursor()
        cur.execute(sql)
        return self.cursor.fetchall()

    def insert(self, sql):
        self.db.ping(reconnect=True)
        self.db.begin()
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        return cur.lastrowid

if __name__ == '__main__':
    db = DBService()
    sql = "select * from user"
    result = db.select(sql)