import db_service
import data_crawler
import yaml
import json
import pymysql
def format_key(prefix = 'SZ', key = '000001'):
    if prefix == 'SZ':
        return str.zfill(str(key), 6) + '.SZ'
    elif prefix == 'SH':
        return str.zfill(str(key), 6) + '.SH'
    elif prefix == 'HK':
        return str.zfill(str(key), 5) + '.HK'
    else:
        return key


def main():
    crawler = data_crawler.DataCrawler()
    db = None
    try:
        is_open = os.environ['IS_CSV_FORMAT']
        print('IS_CSV_FORMAT: ', is_open)
        if is_open == '1':
            db = db_service.FundDataService()
            is_csv = True
        else:
            is_csv = False
    except:
        is_csv = True
    with open("stocks.yaml") as f:
        stock_base = yaml.load(f)["stocks"]
    for ts_code in stock_base['A-Share']['SZ']:
        data = crawler.get_today_data(format_key('SZ', ts_code))
        if not is_csv:
            data = json.loads(data)
            for item in data:
                db.insert_fund_data(item)
    for ts_code in stock_base['A-Share']['SH']:
        data = crawler.get_today_data(format_key('SH', ts_code))
        if not is_csv:
            data = json.loads(data)
            for item in data:
                db.insert_fund_data(item)


if __name__ == '__main__':
    main()

