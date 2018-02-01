source downloader
=================

公開されているjavascriptのSourceMapを展開して、元のソースコードを読めるようにします。

Python3が必要です。

## 使い方

ダウンロードして

```
$ git clone https://github.com/macrat/source_downloader.git && cd source_downloader
```

ファイルから読み込んだり

```
$ ./source_downloader.py path/to/javascript.js.map
```

URLから読み込んだり

```
$ ./source_downloader.py http://example.com/path/to/javascript.js.map
```

Web上のjavascriptからSourceMapの場所を見付ける機能もあります。

```
$ ./source_downloader.py http://example.com/path/to/javascript.js
```

## 注意

人のサイトに対するご利用はほどほどに。

おすしたべたい。
