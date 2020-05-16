# ngrok

:information_source: `ngrok`は`Slack`などのウェブサービスと手元の開発マシンとの間にセキュアな通信を確立するためのツールです。

## 所要時間

- 10分

## インストール

- [ngrok - download](https://ngrok.com/download) に行き、「Download for Windows」を選択
- ダウンロードされたzipファイルを解凍し、`ngrok.exe`を得る
- `ngrok.exe`の置き場はどこでも構わない（例：[個人フォルダ](../research/files-and-data.md)の`Development\ngrok`）

## 起動

- `Windows PowerShell`で、`ngrok.exe`の保存場所へ移動し、以下のコマンドを実行
```
PS C:\Users\アカウント名\SynologyDrive\MyFolders\Development\ngrok > .\ngrok.exe http 3000
```
- 以下のようなステータス画面が表示される
```
ngrok by @inconshreveable                                                                               (Ctrl+C to quit)                                                                                                                        Session Status                online                                                                                    Session Expires               7 hours, 59 minutes                                                                       Version                       2.3.35                                                                                    Region                        United States (us)                                                                        Web Interface                 http://127.0.0.1:4040                                                                     Forwarding                    http://4cb4c535.ngrok.io -> http://localhost:3000                                         Forwarding                    https://4cb4c535.ngrok.io -> http://localhost:3000    
```
- ウェブ上の`https://4cb4c535.ngrok.io`に送られたリクエストは、手元のPCで起動するアプリに`3000`番ポートを経由して、送信されてくる
- ポート番号は変更可
- 本セッションの有効時間は、約8時間

## :warning: 有効時間

- `ngrok`を起動した際に作成されるセッションには有効期限があります。
- 有効期限が切れた場合は、`ngrok`を再起動し、新しく生成されるURLを使用する必要があります。

## `ngrok`の終了

- ステータス画面で、`Ctrl+C`

## 参考URL

- [ngrok - documentation](https://ngrok.com/docs)