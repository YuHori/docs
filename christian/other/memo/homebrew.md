# homebrew
### インストール先
```
/usr/local/Cellar/
```
以下に project ごとに dir が切られて、ファイルが置かれる（install される)
そのため、g++ 等で こちらにインストールした header を使って build する場合には、
こちらを -l で指定して build を実施すれば良い
```
g++ -std=c++11 -l/usr/local/Cellar/<略>/include <以下略>
```
など
