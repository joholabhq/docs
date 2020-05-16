# Python

:bulb: 2020年5月現在では、[Anaconda](pc-anacoda.md)よりも、本ページで説明している実行環境を推奨します。

## 所要時間

- 30分

## インストール

- [Download Python](https://www.python.org/downloads/)にいく
- `Download Python 3.x.x`を選択しインストーラーをダウンロード → 起動
- インストーラーの初期画面で以下にチェックを入れる
  - [x] Install launcher for all users (recommended)
  - [x] Add Python 3.x to PATH
- Install Nowを選択
- `Setup was successful`が表示されたら、`Close`
- `Windows PowerShell`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> python -V
Python 3.8.2
PS　C:\Users\アカウント名>
```
- ↑のようにPythonのバージョンが表示されたら成功（バージョン番号はインストールする時期により異なります）

## パッケージのインストール

- Pythonには多数のパッケージが存在し、自分の目的に合わせてインストールします
- `Windows PowerShell`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> py -m pip install 【パッケージ名】
```
- Jupyter Labをインストールする場合
```
PS C:\Users\アカウント名> py -m pip install jupyterlab
```

## 代表的なパッケージ

|パッケージ名|内容|
|:--|:--|
|`jupyterlab`|Python実行環境ノートブック|
|`matplotlib`|グラフ描画|
|`numpy`|数値計算（`matplotlib`と一緒にインストールされる）|
