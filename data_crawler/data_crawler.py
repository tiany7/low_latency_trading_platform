import tushare as ts
import os
import datetime
# 初始化pro接口
class DataCrawler:
    def __init__(self):
        token = None
        try:
            token = os.environ['TUSHARE_TOKEN']
        except KeyError:
            print('请设置环境变量TUSHARE_TOKEN')
            exit(1)
        ts.set_token(token)
        self.pro = ts.pro_api()
        self.data_path = os.path.join(os.path.dirname(__file__), 'data')
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)

    def get_daily_data(self, ts_code, start_date, end_date):
        df = self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        try:
            is_open = os.environ['IS_CSV_FORMAT']
            if is_open == '1':
                df.to_csv(os.path.join(self.data_path, ts_code + '.csv'),mode='a', header=False)
            print("获取数据成功, 以csv格式保存在data目录下")
            return df
        except KeyError:
            print("获取数据成功, 以mysql格式保存在fund_raw_data表内")
            return df.to_json(orient='records', date_format='epoch')

    def get_today_data(self, ts_code):
        print("获取今日数据")

        df = self.get_daily_data(ts_code, get_today(), get_today())
        print(df)
        return df

def get_today():
    return datetime.datetime.now().strftime('%Y%m%d')
