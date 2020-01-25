# Windows 10のインストール

:warning: 指導教員から指示があった場合のみ本手順の作業を行ってください。

## 参考URL

- http://lifekeynotes.com/2018/08/01/hot-to-solve-your-thinkpad-usb-boot-problems/
- [Windows 10用USBインストーラーの作成](pc-win10-installer-on-ubuntu.md)

## 所要時間

- 1時間

## 手順: Windows10のインストール

- インストール用USBディスクをPCに接続して、PCの電源を入れて、`Lenovo`のロゴが表示されたらすぐに`Enter`キーを押す
- 青い画面が表示されたら`F1`キーを押す
- BIOS設定画面が表示されたら、以下の設定をおこなう
  - Security > Secure Boot > `Enabled`をスペースキーを押して`Disabled`に変更 > `Enter` > `ESC` > `F10` > Yes
  - 再起動
- `Lenovo`のロゴが表示されたらすぐに`F12`キーを押す
- ブート選択画面が表示されたらUSBディスクを選択
- インストール画面が表示されたら、[PCの初期設定](pc-initial-setup.md)へ


### USBから起動できない場合

- BIOS設定画面が表示されたら、以下の追加設定をおこなう
  - Startup > UEFI/Legacy Boot > Both
  - UEFI/Legacy Boot Priority > Legacy First
  - `F10` > Yes
  

