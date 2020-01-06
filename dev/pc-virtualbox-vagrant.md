# VirtualBoxとVagrantのインストール

## 所要時間

- 10分

## 手順

### VirtualBoxのインストール

- [VirtualBoxのダウンロードページ](https://www.virtualbox.org/wiki/Downloads)にいき、`Windows Hosts`を選択
- ダウンロード → 実行
  - すべて次へ
  - :warning: このデバイスソフトウェアをインストールしますか？：インストール

### Vagrantのインストール

- [Vagrantのダウンロードページ](https://www.vagrantup.com/downloads.html)にいき、`Windows 64-bit`を選択
- ダウンロード → 実行（すべて次へ）
- PCの再起動

### Vagrantプラグインのインストール

- `Windows Powershell (x86)`を起動
- 端末で以下のコマンドを実行
```
PS C:\Users\アカウント名> vagrant plugin install vagrant-vbguest
```
- 実行許可を求める表示が出たら、許可する

### 仮想マシンの作成

- [Ubuntu 18.04 LTSを使った仮想マシン作成](vm-ubuntu1804.md)
- [CentOS 7を使った仮想マシンの作成](vm-cnetos7.md)
