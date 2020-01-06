# VirtualBoxとVagrantのインストール

## 所要時間

- 15分

## 手順

### VirtualBoxのインストール

:warning: 2020/01/06時点で、VagrantはVirtualBox ver.6.0を必要としています。

- [VirtualBoxのダウンロードページ](https://www.virtualbox.org/wiki/Downloads)にいく
- ページ中段にある`VitualBox older builds`を選択、`VitualBox 6.0` > `Windows Hosts`を選択
- ダウンロード → 実行
  - すべて次へ
  - :warning: このデバイスソフトウェアをインストールしますか？：インストール

### Vagrantのインストール

- [Vagrantのダウンロードページ](https://www.vagrantup.com/downloads.html)にいき、`Windows 64-bit`を選択
- ダウンロード → 実行（すべて次へ）
- PCの再起動

### 環境変数の設定

- `Vagrant`はユーザ名が日本語だと動作しないので、以下の変更をおこなう
- `Windows Powershell (x86)`を :warning: `管理者モード`で起動し、以下のコマンドを実行
```
PS C:\WINDOWS\system32>cd C:\Users
PS C:\Users>dir
...
d-r---  2020/nn/nn  nn:nn Public
d-----  2020/nn/nn  nn:nn アカウント名
PS C:\Users>cmd
C:\Users>mklink /d sNNNNNNN アカウント名
sNNNNNNN <<===>> アカウント名のシンボリックリンクが作成されました
```
- `sNNNNNNN`は統一認証のユーザ名、`アカウント名`はWindowsのユーザ名
- 続いて以下のコマンドを実行
```
C:\Users>exit
PS C:\Users> [System.Environment]::SetEnvironmentVariable("VAGRANT_HOME", "C:\Users\sNNNNNNN", "User")
```
- PCの再起動


### Vagrantプラグインのインストール

- `Windows Powershell (x86)`を :warning: `管理者モード`で起動
- 端末で以下のコマンドを実行
```
PS C:\WINDOWS\system32> vagrant plugin install vagrant-vbguest
```
- 実行許可を求める表示が出たら、許可する

### Vagrantプラグインのアンインストール

:bulb: もし`vagrant-vbguest`をインストールした後に、`Vagrant failed to initialize at a very early stage`等のエラーメッセージがでるようなら、以下のコマンドを実行して、プラグインを削除する。

```
PS C:\WINDOWS\system32> vagrant plugin uninstall vagrant-vbguest
```


### 仮想マシンの作成

- [Ubuntu 18.04 LTSを使った仮想マシン作成](vm-ubuntu1804.md)
- [CentOS 7を使った仮想マシンの作成](vm-cnetos7.md)
