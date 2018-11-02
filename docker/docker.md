# docker

## docker for mac のインストール
https://qiita.com/digitalm/items/49b7099554bdbff5ed8e

## docker hub
https://hub.docker.com/
https://hub.docker.com/_/golang/

## コンテナをpull（centos:6）
docker pull centos:6

## イメージ一覧取得
docker images

## 起動中のdocker コンテナを確認
docker ps

## コンテナ確認
docker container ls -a

## コンテナ削除
docker container rm <コンテナ名>

## ip を確認（nginx 等で接続する際に利用）
docker-machine ip default

## コンテナ起動・終了
### 初回の例
例えば、mysql コンテナを立てる場合。
local にイメージがない場合には、自動でpull してくれる。
docker run -it --name mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest

### 二回目以降
$docker start (コンテナ名)
$docker stop (コンテナ名)

## コンテナに接続
### 例
例えば、上で作成したコンテナにはいかのようにつなぐ
docker exec -it mysql bash

## docker compose
複数コンテナの管理が便利に扱える
https://qiita.com/y_hokkey/items/d51e69c6ff4015e85fce


## エラーメモ
http://48n.jp/blog/2016/10/05/fix-unable-to-connect-to-docker-daemon/