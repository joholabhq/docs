# Git

## 所要時間

- 10分

## インストール

- [ホームページ](https://gitforwindows.org/)にいく
- `Download`を選択して、セットアップアプリをダウンロード →　実行
- セットアップ画面が表示されたら、以下の設定をおこなう
  - `Choosing the dfault editor used by Git`画面が表示されるまでは、`Next`を選択
  - ↑の画面で`Use Visual Studio Code as Git's default editor`を選択 → `Next`
  - その後もずっと`Next`を選択し、インストールを実行する
  
## 初期設定

- `Windowsキー`+`S` → `git bash`入力 → `Git Bash`を選択
- 端末が表示されたら以下のコマンドを入力

```
$ git config --global user.name "sNNNNNNN" # 統一認証のユーザ名
$ git config --global user.email "sNNNNNNN@u.tsukuba.ac.jp" # @uのメールアドレス

```
