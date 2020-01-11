# Windows 10用USBインストーラーの作成

## 所要時間

- 1.5時間

## 手順

- データを全て削除しても良いUSBディスク（8G以上）をPCに接続する
- [Windows 10 のディスク イメージ (ISO ファイル) のダウンロード](https://www.microsoft.com/ja-jp/software-download/windows10ISO)にいく
  - エディションの選択：Windows10 > 確認
  - 製品の言語の選択：日本語 > 確認
  - Windows 10 日本語 64-bit ダウンロードを選択 > ダウンロード
- 端末（ターミナル）から以下のコマンドを実行
```
$ sudo add-apt-repository ppa:nilarimogard/webupd8
... [Enter]
$ sudo apt update
$ sudo apt install woeusb
```
- アプリ一覧から`WoeUSB`を起動
  - From a disk image: 先ほどダウンロードした`Win10...iso`ファイルを選択
  - File System: NTFS
  - Target Device: USBディスクを選択（例：`/dev/sdb`）
  - Install
  - エラー画面が出たら、デスクトップ画面からUSBディスクを右クリック > アンマウント > Install
- Windows 10のインストールが完了するまで待つ
