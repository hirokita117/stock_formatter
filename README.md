# stock_formatter
日本の東証上場銘柄をデータベース化するスクリプトです。
下記コマンド + envファイル編集で出来ます。

```
$ cp .env.example .env

$ vim .env # 設定を記述

$ python createStocksCsvFile.py && python createAndInsertStocksTable.py
```

東証上場銘柄のリストは下記からダウンロードできます。
（JPXのオフィシャルサイト: その他統計資料 > 東証上場銘柄一覧）
https://www.jpx.co.jp/markets/statistics-equities/misc/01.html