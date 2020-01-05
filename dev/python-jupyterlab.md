# JupyterLabの使い方

## 起動

- [Anacondaをインストールする](pc-anaconda.md)
- `スタート` > `Anaconda3 (64-bit)` > `Anaconda Prompt (Anaconda 3)`を選択
- 端末が表示されたら、以下のコマンドを実行

```
(base) C:\Users\アカウント名> jupyter lab
```

- 端末に表示される`http://localhost:8888/?token=......`の行を選択、`Enterキー`
- ブラウザのアドレスバーにコピペして、`JupyterLab`にアクセス

## 停止

- 起動中の端末で、`Ctrl+C`を入力

## 拡張機能のインストール

- JupyterLabを停止する
- `Anaconda Prompt (Anaconda 3)`の端末で以下のコマンドを実行

```
(base) C:\Users\アカウント名> conda install nodejs
...
Proceed ([y]/n)? y
```
- JupyterLabを起動する
- Settings > Enable Extension Manager (experimental)
- 左パネル追加されたパズルピースのようなアイコンを選択
- 検索ボックスに`toc`と入力し、検索結果に表示される`@jupyterlab/toc`の`Install`
- `A build is needed to include ...`と表示されたら、`Rebuild`を選択
- ビルドが完了するまでしばらく待つ
