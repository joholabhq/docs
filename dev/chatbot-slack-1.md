# チャットボットの開発（Slack編）#1

## 作業時間

- 1時間

## 事前準備

- [Pythonのインストール](pc-python.md)
- [Slackのインストールと研究室ワークスペースへの参加](pc-slack.md)
- [grokのインストール](pc-ngrok.md)

## 新規アプリの作成

- [Slack Appマネージメント](https://api.slack.com/apps?new_app=1)で新規アプリを作成
  - App Name: Simple Bot
  - Development Slack Workspace: ISR Lab
  - `Create App`
- 基本情報の設定
  - `Basic Information`画面 > `Add features and functionality` > `Bots`を選択
  - `App Home`画面 > `Review Scopes to Add`を選択
  - `OAuth & Permissions`画面 > `Scopes` > `Bot Token Scopes` > `Add an OAuth Scope`を選択
  - 「chat:write」を選択

## アプリのワークスペースへの登録

- 作成したアプリ画面の左メニュー > `Install App`を選択
- 次の画面で「許可する」を選択

## 認証情報の取得方法

:bulb: チャットボット開発では主に二つの認証情報が必要になりますので、場所を覚えておきましょう。

### Signing Secret

- アプリ画面の左メニュー > `Basic Information`を選択
- `App Credentials` > `Signing Secret` > `Show`を選択

### Bot User OAuth Access Token

- アプリ画面の左メニュー > `OAuth & Permissions`を選択
- `OAuth Tokens & Redirect URLs` > `Tokens for Your Workspace` > `Bot User OAuth Access Token`

## アプリのチャネルへの追加

- Slackの自分専用チャネルにいく
- 上部リンクから「アプリを追加する」を選択
- 一覧から「Simple Bot」を選択

## Python Slack APIの取得

- [個人フォルダ](../research/files-and-data.md)の`Development`に「chatbot」というフォルダを作成
    - 以下このフォルダ内で作業することを想定
- VSCodeでchatbotフォルダを開く
- [requirements-1.txt](chatbot-slack/requirements-1.txt)というファイルを新規作成
- VSCodeでターミナルを開き、以下のコマンドを実行
```
PS C:\Users\アカウント名 ... chatbot> py -m pip install -r .\requirements-1.txt
```

## 接続テスト

- [hello-world.py](chatbot-slack/hello-world.py)を新規作成
    - 10行目付近の以下の行の`<your chatbot channel>`を、自分専用のチャネル名で置き換える
    ```
    my_channel = '<your chatbot channel>' #my-channel-name
    ```
- VSCodeのターミナルから以下のコマンドを実行（新規ターミナルにつき一度のみ）
    - `<Your Signing Secret>`と`<Your Bot User OAuth Access Token>`は、↑の認証情報からコピペする
```
PS C:\Users\アカウント名 ... chatbot> $env:SLACK_SIGNING_SECRET='<Your Signing Secret>'
PS C:\Users\アカウント名 ... chatbot> $env:SLACK_BOT_TOKEN='<Your Bot User OAuth Access Token>'
```

- VSCodeのターミナルから以下のコマンドを実行
```
PS C:\Users\アカウント名 ... chatbot> py hello-world.py
```
- Slackアプリの自分用チャネルに`Hello, world!'というメッセージが表示されたら接続成功


## 参考URL

- [Slack API 日本語](https://api.slack.com/lang/ja-jp)
- [Python Slack API](https://github.com/SlackAPI/python-slackclient)