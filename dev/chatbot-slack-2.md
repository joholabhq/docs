# チャットボットの開発（Slack編）#2

[# チャットボットの開発（Slack編）#1](chatbot-slack-1.md)の続き


## チャットボットプログラム

- [goodbye-hello.py](chatbot-slack/goodbye-hello.py)を新規作成
- VSCodeのターミナルから以下のコマンドを実行
```
PS C:\Users\アカウント名 ... chatbot> py goodbye-hello.py
```
- ボットが起動した時の出力例
```
 * Serving Flask app "slackeventsapi.server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
 ...
```

## イベントの設定

:information_source: イベントとはSlackアプリ上でユーザが行う操作のことです。チャットボット開発では、このイベントを取得して、手元のPCに送信します。

- アプリ画面の左メニュー > `Event Subscriptions`を選択
- `Enable Events`をONにする
- `Request URL`に[ngrok](pc-ngrok.md)のURL+`/slack/events`を入力
    - `ngrok`のセッションがなければ、新規に立ち上げる
    - `ngrok`が生成したURL例
        - `https://4cb4c535.ngrok.io`
    - `Request URL`への入力例
        - `https://4cb4c535.ngrok.io/slack/events`
- `Request URL`へ入力後、「Verifing...」というメッセージが表示される
- 「Verfied!」というメッセージが表示されたら完了

:warning: `Request URL`の設定は、`ngrok`のセッションが変わる度に、更新する必要があります。

- その下の`Subscribe to bot events` > `Add Bot User Event`を選択
- `message.channels`と`message.im`を選択
- 画面右下の`Save Changes`を選択
- 画面上部に表示される`reinstall your app`を選択 > 次の画面で「許可」

## ボットとのチャット #1

- Slackの自分専用のチャネルに移動し、以下のメッセージを投稿
    ```
    goodbye
    ```
- `simple_bot`から以下の返信が来たら成功
    ```
    Hello @your-slack-name!
    ```
- `goodbye`以外のメッセージには反応しないことを確認

## ボットとのチャット #2

- Slackの左メニューの一番下にある「App」セクションの「＋」を選択
- 表示されるアプリ一覧から作成したボット（例：`Simple Bot`）を選択
- 追加されたボットを選択し、以下のメッセージを投稿
    ```
    goodbye
    ```
- `simple_bot`から以下の返信が来たら成功
    ```
    Hello @your-slack-name!
    ```

## チャットボットの終了

- VSCodeのターミナルで稼働している`goodbye-hello.py`を`Ctrl+C`で終了
- `Windows PowerShell`で稼働している`ngrok`を`Ctrl+C`で終了（2回押さないと終了しないかも）

## 次のステップ

- `goodbye-hello.py`をコピペして別ファイルを新規作成し、17行目以降を改良することで、より高度なチャットボットを開発する
- 下記参考URLを参照しながら、Slack APIが提供する機能を学習し、実装する

## 参考URL

- [Slack API 日本語](https://api.slack.com/lang/ja-jp)
- [Python Slack API](https://github.com/SlackAPI/python-slackclient)
- [Slack Events API adapter for Python](https://github.com/slackapi/python-slack-events-api)