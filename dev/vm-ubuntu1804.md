# Ubuntu 18.04 LTSを使った仮想マシンの生成

## 所要時間

- 30分

## 手順

### 仮想マシンの作成
- [ユーザフォルダ内作業エリアの作成](pc-workspace.md)
- （1回目のみ）`Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名>cd Workspace
PS C:\Users\アカウント名\Workspace>cd Local
PS C:\Users\アカウント名\Workspace\Local>mkdir Vagrant
PS C:\Users\アカウント名\Workspace\Local>cd Vagrant
PS C:\Users\アカウント名\Workspace\Local\Vagrant>mkdir Ubuntu1804
PS C:\Users\アカウント名\Workspace\Local\Vagrant>cd Ubuntu1804
PS C:\Users\アカウント名\Workspace\Local\Vagrant\Ubuntu1804>vagrant box add bento/ubuntu-18.04
...
PS C:\Users\アカウント名\Workspace\Local\Vagrant\Ubuntu1804>vagrant init bento/ubuntu-18.04
PS C:\Users\アカウント名\Workspace\Local\Vagrant\Ubuntu1804>code . # VSCodeの起動
```

- （2回目以降）`Windows Powershell (x86)`を起動


### 仮想マシンの起動

```
PS C:\Users\アカウント名\Workspace\Local\Vagrant\Ubuntu1804>vagrant up
...
```

### 仮想マシンへのSSH接続

- [Termiusをインストール](pc-termius.md)
- 新しいホストを作成
  - ホスト名：Ubuntu 18.04
  - アドレス：192.168.10.33
  - ユーザ名：vagrant
  - パスワード：vagrant
- 接続

### 仮想マシンの終了

- 起動した端末で以下のコマンドを実行
```
PS C:\Users\アカウント名\Workspace\Local\Vagrant\Ubuntu1804>vagrant halt
```
