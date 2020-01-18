# Windows 10のインストール

:warning: 指導教員から指示があった場合のみ本手順の作業を行ってください。

Windows10のインストールとEnterprise版へのアップグレード

## 参考URL

- http://lifekeynotes.com/2018/08/01/hot-to-solve-your-thinkpad-usb-boot-problems/
- [Windows 10用USBインストーラーの作成](pc-win10-installer-on-ubuntu.md)

## 所要時間

- 手順1: 1時間
- 手順2: 1時間

## 手順1: Windows10のインストール

- インストール用USBディスクをPCに接続して、PCの電源を入れて、`Lenovo`のロゴが表示されたらすぐに`Enter`キーを押す
- 青い画面が表示されたら`F1`キーを押す
- BIOS設定画面が表示されたら、以下の設定をおこなう
  - Security > Secure Boot > Enabled をスペースキーを押して Disable > `F10` > Yes
  - 再起動
- `Lenovo`のロゴが表示されたらすぐに`F12`キーを押す
- ブート選択画面が表示されたらUSBディスクを選択
- インストール画面が表示されたら、[PCの初期設定](pc-initial-setup.md)の手順1を参考にインストールを行う
- デスクトップ画面が表示されたら、手順2に移る

### USBから起動できない場合

- BIOS設定画面が表示されたら、以下の追加設定をおこなう
  - Startup > UEFI/Legacy Boot > Both
  - UEFI/Legacy Boot Priority > Legacy First
  - `F10` > Yes
  
## 手順2: Enterprise版へのアップグレード

- 指導教員を呼ぶ
- [ソフトウェア配布管理システム](https://ds.cc.tsukuba.ac.jp/download/)のトップページにある「Windows 10へのアップグレードに関して」からリンクされているPDFファイルを開く
- PDF内の(zip 版)日本語版 64Bit 版のリンクを選択 > ダウンロード（要：指導教員）
- ダウンロードが完了したら、zipファイルを右クリック > ここに展開 > `setup.exe`を実行
- イメージの選択：Windows 10 Enterprise > 次へ
- インストール画面が表示されたら、[PCの初期設定](pc-initial-setup.md)の手順1を参考にインストールを行う
- インストールが完了したら、↑のPDFファイルに戻り、(4)以降のライセンス認証を行う（要：指導教員）
