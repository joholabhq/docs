# VirtualBoxとVagrantのインストール

## 所要時間

- 15分

## 手順

### フォルダの準備

- [第２作業エリアの作成](pc-workspace.md)
- 関連フォルダの作成
  - `Windows Powershell (x86)`を起動し、以下のコマンドを実行（エクスプローラーで作業しても良い）
  - `sNNNNNNN`は統一認証のユーザ名（半角英数）
```
PS C:\Users\アカウント名>cd C:\Home\sNNNNNNN
PS C:\Home\sNNNNNNN>mkdir .vagrant.d; mkdir .VirtualBox; mkdir "VirtualBox VMs"
PS C:\Home\sNNNNNNN>cd Workspace; cd Local
PS C:\Home\sNNNNNNN\Workspace\Local>mkdir Vagrant
```

### VirtualBoxのインストール

:information_source: 2020/01/06時点で、VagrantはVirtualBox ver.6.0を必要としています。

- [VirtualBoxのダウンロードページ](https://www.virtualbox.org/wiki/Downloads)にいく
- :warning: ページ中段にある`VitualBox older builds`を選択、`VitualBox 6.0` > `Windows Hosts`を選択
- ダウンロード → 実行
  - すべて次へ
  - :warning: このデバイスソフトウェアをインストールしますか？：インストール
- スタート > Oracle VM VirtualBoxで起動
- ファイル > 環境設定 > 一般 > デフォルトの仮想マシンフォルダー > ブルダウンメニュー > その他
- 「フォルダの準備」で作成した`C:\Home\sNNNNNNN\VirtualBox VMs`を選択 > OK
- アプリを終了

### Vagrantのインストール

- [Vagrantのダウンロードページ](https://www.vagrantup.com/downloads.html)にいき、`Windows 64-bit`を選択
- ダウンロード → 実行（すべて次へ）
- PCの再起動

### 環境変数の設定

- `Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> [System.Environment]::SetEnvironmentVariable("VAGRANT_HOME", "C:\Home\sNNNNNNN\.vagrant.d", "User")
PS C:\Users\アカウント名> [System.Environment]::SetEnvironmentVariable("VBOX_USER_HOME", "C:\Home\sNNNNNNN\.VirtualBox", "User")
PS C:\Users\アカウント名>exit
```
- PCの再起動


### Vagrantプラグインのインストール

- `Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> vagrant plugin install vagrant-vbguest
```
- 実行許可を求める表示が出たら、許可する

### （参考）Vagrantプラグインのアンインストール

- `vagrant-vbguest`の例

```
PS C:\Users\アカウント名> vagrant plugin uninstall vagrant-vbguest
```

---

### （参考）仮想マシンの作成

- [Ubuntu 18.04 LTSを使った仮想マシン作成](vm-ubuntu1804.md)
- [CentOS 7を使った仮想マシンの作成](vm-centos7.md)
