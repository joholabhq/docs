# Windows 10用USBインストーラーの作成

:warning: 以下の手順は研究室PC用です。ハードディスクの構成次第ではパソコン内のデータが削除される可能性がありますので、個人PC等には実行しないでください。

## 所要時間

- 1.5時間

## 手順

- [Windows 10 のディスク イメージ (ISO ファイル) のダウンロード](https://www.microsoft.com/ja-jp/software-download/windows10ISO)にいく
  - エディションの選択：Windows10 > 確認
  - 製品の言語の選択：日本語 > 確認
  - Windows 10 日本語 64-bit ダウンロードを選択 > ダウンロード（ファイルを保存する）
- 端末（ターミナル）から以下のコマンドを実行
```
$ sudo add-apt-repository ppa:nilarimogard/webupd8
... [Enter]
$ sudo apt update
$ sudo apt install woeusb
```
- データを全て削除しても良いUSBディスク（8G以上）をPCに接続する
- USBディスクのアイコンがデスクトップに表示されたら、端末（ターミナル）から以下のコマンドを実行
  - `[Downloads/Win...iso]`の部分は自分の環境（ダウンロード先）を指定する
```
$ sudo umount /dev/sda1
$ sudo woeusb --tgt-fs NTFS -d [Downloads/Win10...iso] /dev/sda
```
- Windows 10のインストーラー作成が完了するまで待つ（1時間くらいかかる）
- 末尾に以下のようなエラーメッセージが表示されるが、作成は成功している
```
...
unresponsive during copying files.
/usr/bin/woeusb: 1676 行: echo: 書き込みエラー: 無効な引数です
The command "exit 0" failed with exit status "1", program is prematurely aborted
```

---

- （参考）[Windows 10のインストール](pc-win10.md)
