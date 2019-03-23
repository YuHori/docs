# -*- coding: utf-8 -*-
#
# 設定ファイル用クラス
# 

def main():
  filename = "1.いざ皆来たりて.md"

  # fileを開く
  chant_map = {}
  key_name = "tmp"
  with open(filename, 'r') as f:
    for row in f:
      # 空行は飛ばす
      if not row.strip():
        continue

      # 歌詞の始まり
      if row[0] == "#":
        key_name = row[1:].strip()
        chant_map[key_name] = []

      # それ以外はmapに詰める
      chant_map[key_name].append(row.strip())


  # mapの中をみる
  python(chant_map)


if __name__ == '__main__':
  main()
