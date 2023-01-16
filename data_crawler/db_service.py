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
            self.config = yaml.load(stream)['database']['store_database']

        print(self.config)
        self.db = pymysql.connect(host=self.config['host'], port=self.config['port'], user=self.config['user'], passwd=self.config['password'], charset='utf8', db=self.config['database'])
        self.cursor = self.db.cursor()
        # create table fund_data if not exists
        sql = 'CREATE TABLE IF NOT EXISTS fund_data(ts_code VARCHAR(20) NOT NULL, trade_date VARCHAR(20) NOT NULL, open_price FLOAT, high_price FLOAT, low_price FLOAT, close_price FLOAT, pre_close_price FLOAT, change_price FLOAT, pct_chg FLOAT, vol FLOAT, amount FLOAT, PRIMARY KEY (ts_code, trade_date))'
        self.db.ping(reconnect=True)
        self.db.begin()
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()

    def __del__(self):
        self.db.close()


    def select(self, sql):
        self.db.ping(reconnect=True)
        self.db.begin()
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        return cur.fetchall()

    def insert(self, sql):
        self.db.ping(reconnect=True)
        self.db.begin()
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        return cur.lastrowid

    def update(self, sql):
        self.db.ping(reconnect=True)
        self.db.begin()
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        return cur.rowcount
    def delete(self, sql):
        self.db.ping(reconnect=True)
        self.db.begin()
        cur = self.db.cursor()
        cur.execute(sql)
        self.db.commit()
        return cur.rowcount

class FundDataService:
    def __init__(self):
        self.db_service = DBService()

    def insert_fund_data(self, fund_data):
        ts_code = fund_data['ts_code']
        trade_date = fund_data['trade_date']
        open_price = fund_data['open']
        high_price = fund_data['high']
        low_price = fund_data['low']
        close_price = fund_data['close']
        pre_close_price = fund_data['pre_close']
        change_price = fund_data['change']
        pct_chg = fund_data['pct_chg']
        vol = fund_data['vol']
        amount = fund_data['amount']
        sql = 'INSERT INTO fund_data(ts_code, trade_date, open_price, high_price, low_price, close_price, pre_close_price, change_price, pct_chg, vol, amount) VALUES("%s", "%s", %f, %f, %f, %f, %f, %f, %f, %f, %f)' % (ts_code, trade_date, open_price, high_price, low_price, close_price, pre_close_price, change_price, pct_chg, vol, amount)
        self.db_service.insert(sql)

    def get_fund_data(self, ts_code, start_date, end_date):
        sql = 'SELECT * FROM fund_data WHERE ts_code = "%s" AND trade_date >= "%s" AND trade_date <= "%s"' % (ts_code, start_date, end_date)
        return self.db_service.select(sql)

# if __name__ == '__main__':
#     db = FundDataService()
#     fund_data = {'ts_code': '000001.SZ', 'trade_date': '20190101', 'open': 1.0, 'high': 1.0, 'low': 1.0, 'close': 1.0, 'pre_close': 1.0, 'change': 1.0, 'pct_chg': 1.0, 'vol': 1.0, 'amount': 1.0}
#     db.insert_fund_data(fund_data)
#     sql = "select * from fund_data"
#     result = db.get_fund_data('000001.SZ', '20190101', '20190101')
#     print(result)