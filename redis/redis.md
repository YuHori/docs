# redis

## 永続化
- AOF 永続化
  コマンドを記憶
- RDB 永続化
  スナップショットを記憶
https://redis-documentasion-japanese.readthedocs.io/ja/latest/topics/persistence.html

## blocking
https://redis.io/commands/blpop
https://redis.io/commands/brpop

## key をすべて削除
flushall

## hincrbyfloat
https://redis.io/commands/hincrbyfloat

## redis stream
※ redis 5 からの機能。メッセージングに利用できそうなので、一応おさえておくのが良さそう。
http://pocapocaunty.hateblo.jp/entry/2018/06/16/171830