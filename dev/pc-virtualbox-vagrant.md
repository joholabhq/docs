# VirtualBoxとVagrantのインストール

## 所要時間

- 15分

## 手順

### VirtualBoxのインストール

:information_source: 2020/01/06時点で、VagrantはVirtualBox ver.6.0を必要としています。

- [VirtualBoxのダウンロードページ](https://www.virtualbox.org/wiki/Downloads)にいく
- :warning: ページ中段にある`VitualBox older builds`を選択、`VitualBox 6.0` > `Windows Hosts`を選択
- ダウンロード → 実行
  - すべて次へ
  - :warning: このデバイスソフトウェアをインストールしますか？：インストール

### Vagrantのインストール

- [Vagrantのダウンロードページ](https://www.vagrantup.com/downloads.html)にいき、`Windows 64-bit`を選択
- ダウンロード → 実行（すべて次へ）
- PCの再起動

### 環境変数の設定

- `Vagrant`のホームを日本語を含まない場所に設定する
- `Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名>cd C:\
PS C:\>mkdir Vagrant
PS C:\>cd Vagrant
PS C:\Vagrant>mkdir .vagrant.d
PS C:\Vagrant> [System.Environment]::SetEnvironmentVariable("VAGRANT_HOME", "C:\Vagrant\.vagrant.d", "User")
PS C:\Vagrant>exit
```
- PCの再起動


### Vagrantプラグインのインストール

- `Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> vagrant plugin install vagrant-vbguest
```
- 実行許可を求める表示が出たら、許可する

### Vagrantプラグインのアンインストール

- `vagrant-vbguest`の例

```
PS C:\Users\アカウント名> vagrant plugin uninstall vagrant-vbguest
```


### 仮想マシンの作成

- [Ubuntu 18.04 LTSを使った仮想マシン作成](vm-ubuntu1804.md)
- [CentOS 7を使った仮想マシンの作成](vm-cnetos7.md)
