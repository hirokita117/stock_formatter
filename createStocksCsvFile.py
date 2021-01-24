import csv
import codecs
import re

file = codecs.open('data_j_testCsv.csv', 'r', 'utf-8', 'ignore')
csv_reader = csv.reader(file)
datas = list(csv_reader)
datas.pop(0) # ヘッダーを削除

stock_code = 1
company_name = 2
market = 3
business_format = 5
industry = 7

pattern = '^市場|^JASDAQ|^マザーズ'
repatter = re.compile(pattern)

output_file = open('stocks.csv', 'w', newline='', encoding='utf-8')
output_file_writer = csv.writer(output_file)

for data in datas:
    result = repatter.match(data[market])
    if not result:
        continue

    output_file_writer.writerow([
        data[stock_code], data[company_name], data[market], data[business_format], data[industry].strip()
    ])


output_file.close()