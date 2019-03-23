#!/usr/bin/env python
# coding: utf-8

# csvファイルの読み込みを行う
import os
import sys
import csv
import configparser
import pymysql.cursors

if __name__ == '__main__':
  # 設定ファイルの読み込み
  root_dir = os.path.dirname(os.path.abspath(__file__))
  inifile = configparser.SafeConfigParser()
  inifile.read('%s/conf/config.ini' % root_dir)
  if not inifile or len(inifile.sections()) == 0:
    print("[err] can not read ini file")
    sys.exit()

  __db    = inifile.get('db', 'db')
  __table = inifile.get('db', 'table')
  __host  = inifile.get('db', 'host')
  __port  = inifile.get('db', 'port')
  __user  = inifile.get('db', 'user')
  __pass  = inifile.get('db', 'pass')


  # MySQLに接続する
  connection = pymysql.connect(host=__host,
                               user=__user,
                               password=__pass,
                               db=__db,
                               charset='utf8',
                               # cursorclassを指定することで
                               # Select結果をtupleではなくdictionaryで受け取れる
                               cursorclass=pymysql.cursors.DictCursor)


  with connection.cursor() as cursor:
    with open('%s/testdata/scriptures_60.csv' % root_dir, 'r') as f:
      reader = csv.reader(f)
      header = next(reader) 
  
      # csvを読みながら、インサートしていく
      for row in reader:
        sql = "INSERT INTO " + __table + " (place, text) VALUES (%s, %s)"
        r = cursor.execute(sql, (row[0], row[1]))

    # commit
    connection.commit()
