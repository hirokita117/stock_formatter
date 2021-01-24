import mysql.connector as mydb
import csv
import codecs
import setting

conn = mydb.connect(
    host = setting.DB_HOST,
    port = setting.DB_PORT,
    user = setting.DB_USER,
    password = setting.DB_PASS,
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect = True)

# 接続できているかどうか確認
print(f'MySQL connect is {conn.is_connected()}.')

# DB操作用にカーソルを作成
cur = conn.cursor()

create_database_stmt = f"CREATE DATABASE IF NOT EXISTS {setting.DB_NAME};"

use_database_stmt = f"USE {setting.DB_NAME};"

create_table_stmt = """CREATE TABLE IF NOT EXISTS stocks (
    code int(11) primary key,
    name varchar(255) not null,
    market varchar(255) not null,
    business_format varchar(255) not null,
    industry varchar(255) not null
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

cur.execute(create_database_stmt)

cur.execute(use_database_stmt)

cur.execute(create_table_stmt)

file = codecs.open('stocks.csv', 'r', 'utf-8', 'ignore')
csv_reader = csv.reader(file)
datas = list(csv_reader)

stock_code = 0
company_name = 1
market = 2
business_format = 3
industry = 4

insert_stocks_stmt = "INSERT INTO stocks (code, name, market, business_format, industry) values (%s, %s, %s, %s, %s);"
for data in datas:
    cur.execute(insert_stocks_stmt, (data[stock_code], data[company_name], data[market], data[business_format], data[industry]))



# DB操作が終わったらカーソルとコネクションを閉じる
cur.close()
conn.commit()
conn.close()
