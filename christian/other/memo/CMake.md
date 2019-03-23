# CMake
環境に応じたMakefileを自動生成してくれる  
autoconfと同じような意味をもつツール  
使ってみた第一印象としては、設定項目がシンプルでわかりやすく、非常に使いかってが良い  

# 流れ
- CMakeLists.txtを作成
- CMakeLists.txtに設定をかく
- 以下コマンドを実行
```
cmake .
```
これでMakefileが作成される
