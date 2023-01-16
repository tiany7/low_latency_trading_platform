# 数据仓库 Digital Data Warehouse
本仓库实现了一个简单爬虫，能够在本机上每日获取A股股票的日线数据（暂时不支持日线，只有天级别的交易，实习完有预算了计划开通港股和美股）
用户可以自己选股票并且加入到数据库当中

This repository implements a simple spider that can retrieve daily A-share stock data on a local machine. Currently, it only supports daily trading data, but plans to expand to Hong Kong and US stocks in the future. Users can choose their own stocks and add them to the database for use.


## 1. 环境 Environment
- Python 3.6.9
- MySQL 5.7.26
- Ubuntu 18.04.3 LTS

## 2.安装 Install
可以直接从requirements.txt中安装依赖包

You can install the dependencies directly from requirements.txt

```bash
pip install -r requirements.txt
```

## 配置 Configurations

首先需要选取自己想要的股票，可以在stocks.yaml里添加。股票代码不用和交易所上写的一模一样，比如0700可以写作700也没问题

First, you need to select the stocks you want. You can add them in stocks.yaml。
The stock code does not have to be exactly the same as what is written on the exchange. For example, 0700 can be written as 700. They are equivalent.



![image](https://user-images.githubusercontent.com/46698520/212778409-0fd87d12-2e3e-4ba1-a179-a02c957f8f01.png)

然后需要在config.yaml中配置数据库的连接信息（）

Then you need to configure the database connection information in config.yaml

```yaml
database:
  store_database:
        host: localhost
        port: 3306
        user: root
        password:
        database: fund_raw_data
```

本仓库默认采用csv文件存储数据，如果需要存储到数据库，需要在init.sh中将IS_CSV_FORMAT设置为False

This repository defaults to storing data in csv files. If you need to store data in a database, you need to set IS_CSV_FORMAT to False in init.sh

```bash
IS_CSV_FORMAT=False
```

*TOKEN* 
由于本项目使用了tushare的API，需要在本地配置token，可以在[这里](https://tushare.pro/register?reg=388838)注册

然后获取token之后，可以在.bashrc中配置token。强烈不建议在代码里或者yaml这些可能会被上传到github的地方配置token，因为这样会造成token泄露

Since this project uses the tushare API, you need to configure the token locally. You can register [here](https://tushare.pro/register?reg=388838)

After getting the token, you can configure the token in .bashrc or local terminals. It is strongly recommended not to configure the token in the code or yaml, or other places that may be uploaded to github, because this will cause the token to leak

```bash
export TUSHARE_TOKEN=your_token
```

## 3. 运行 Run

```bash
sh init.sh
```

## 定时任务 Scheduled Tasks
如果需要每日定时运行，可以在crontab中添加定时任务

If you need to run it daily, you can add a scheduled task in crontab

```bash
crontab -e
```

```bash
0 0 * * * sh /path/to/init.sh #比如这样，每天0点运行一次
```

# Acknowledgements
- [tushare](www.tushare.pro)
感谢提供免费的API，有预算了一定升级成付费用户