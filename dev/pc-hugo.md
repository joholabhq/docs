# Hugo

## 所要時間

- 10分

## 手順

- Hugoの[ダウンロードページ]()にいき、hugo_extended_0.xx.x_Windows-64bit.zip`を選択 > ダウンロード
- ダウンロードしたzipファイルを右クリック > すべて展開
- `Windows Powershell (x86)`を起動し、以下のコマンドを実行（エクスプローラーで作業しても良い）
```
PS C:\Users\アカウント名>cd C:
PS C:>mkdir Hugo; cd Hugo
PS C:\Hugo>mkdir bin
```
- 展開したフォルダにある`Hugo.exe`を作成した`C:\Hugo\bin`フォルダに移動
- `Windowsキー+S`で検索窓を出して「環境」で検索 > 環境変数を編集 を選択
- ユーザ環境変数の`Path`をダブルクリック
- 右のボタンから「新規」を選択
- `C:\Hugo\bin`と入力 > OK > OK
- PCを再起動
