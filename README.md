# retweet_machine.py
リツイートしたいツイートをリツイートするツールです。
リツイート対象URLリストの中からランダムにURLを選択してリツイートします。

## Requirements
-Python 3.5 +

-[Tweepy](http://docs.tweepy.org/en/latest/install.html)

## Setting
1.自分が使っている Twitter アカウントについて [Developper登録](http://docs.tweepy.org/en/latest/install.html)を行い、 API key, API secret key, Access Token, Access Token Secret を取得します。

2.自分のTwitterアカウント名と取得した API key, API secret key, Access Token, Access Token Secret を credential.py に記載します。

credential.py 記載例
```
user_id = 'goodchi_spot'
consumer_key = '8sasd89fDhfjweq24tr&DSAd2'
consumer_secret = 'h6928fyS2YLjRaNJgtkva7c0whhHqyutqYxra6P9EesU0w0goC'
consumer_secret = 'e6sdgsEW32532tgklsjh6928fyk343jlkljSDFgsdsS2rsdfgN'
access_token = '8746464507-Ndsr3tt4S1kyfHdr43sdfsMCGHJ265DFGdsdtFD'
access_token_secret = 'M1s4FHsaw67HXssaerszR42FDXHdsgFjdrDTNxcDEol81'
```

3.retweet_machine.py と credential.py を同じディレクトリに置きます。

4.リツイートしたいURLのリストを用意します（デフォルトのファイル名は、url_list.txt です）。

## Usage

```
usage: retweet_machine.py [-h] [-u URLLIST_FILENAME] [-t TWEET_TITLE]
                          [-s SLEEP_SEC]

This is retweet_machine.py.

optional arguments:
  -h, --help            show this help message and exit
  -u URLLIST_FILENAME, --urllist URLLIST_FILENAME
                        This option is urllist filename. Default urllist
                        filename is "url_list.txt".
  -t TWEET_TITLE, --title TWEET_TITLE
                        This option is tweet title (if you'd like to show).
  -s SLEEP_SEC, --sleep SLEEP_SEC
                        This option is sleep time [s]. Default sleep time is
                        40[s]
```

## example

-url_list.txtのURLリストを60秒間隔でリツイートし続け、コマンドラインにタイトルを表示させて実行する場合。

```
$ ./retweet_machine.py -t "my select" -s 60 
my select
https://twitter.com/kikou_mewan/status/1227095093896609793?s=21
my select
https://twitter.com/kikou_mewan/status/1242641260197761024?s=21
...```
