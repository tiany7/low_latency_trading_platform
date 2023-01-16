import tushare as ts
import os
import datetime
# 初始化pro接口
class DataCrawler:
    def __init__(self):
        ts.set_token(os.environ['TUSHARE_TOKEN'])
        self.pro = ts.pro_api()
        self.data_path = os.path.join(os.path.dirname(__file__), 'data')
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
    def get_daily_data(self, ts_code, start_date, end_date):
        df = self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        df.to_csv(os.path.join(self.data_path, ts_code + '.csv'), index=False)
        return df
    def get_today_data(self, ts_code):
        df = self.get_daily_data(ts_code, get_today(), get_today())
        return df

def get_today():
    return datetime.datetime.now().strftime('%Y%m%d')
