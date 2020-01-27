# TeX Live

## 所要時間

- 2時間

## 手順

- [Installing TeX Live over the Internet](https://www.tug.org/texlive/acquire-netinstall.html)にいき、`install-tl.zip`をダウンロード
- TeXLiveのインストーラーは、パスに日本語があると正しく動作しないので、`C:\Home\sNNNNNNN\Downloads`というフォルダを作成し（[参考](pc-virtualbox-vagrant.md)）、ダウンロードしたZipファイルを保存
- Zipファイルを右クリック > ここに展開
- 展開した中に`install-tl-yyyymmdd`（yyyymmddの部分は自分の環境を確認）というフォルダを見つけ、その中にある`install-tl-windows.bat`を右クリック → 管理者として実行を選択
- TeX Liveインストーラーが起動したら、「インストール」を選択
- 4000近い数のパッケージがインストールされるまで待つ

## VSCodeでの使用方法

- [VSCode](pc-vscode.md)をインストールして、実行
- 左パネルのExtensionの検索窓に`latex workshop`と入力、検索
- 検索結果に表示さえる`LaTeX Workshop`の右下にある`Install`を選択
- LaTeX拡張機能のインストール後、VSCodeでTeXフィアルを開く
- 左パネルの`TeX`を選択
  - `Build LaTeX project`の中から適切なコンパイル方法を選択
- ソースコード右上にあるPDFアイコンをクリックして、結果を表示
