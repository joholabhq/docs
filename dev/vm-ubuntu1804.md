# Ubuntu 18.04 LTSを使った仮想マシンの生成

:bulb: 仮想マシンは使いたい時に起動し、使い終わったら終了する習慣をつけましょう。

## 所要時間

- 30分

## 手順

### 仮想マシンの作成
- [VirtualBoxとVagrantのインストール](pc-virtualbox-vagrant.md)
- `Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名>cd C:\Home\sNNNNNNN\Workspace\Local\Vagrant
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant>mkdir Ubuntu1804; cd Ubuntu1804
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>vagrant box add bento/ubuntu-18.04
...
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>vagrant init bento/ubuntu-18.04
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>code . # VSCodeの起動
```
- 以下はVSCode上で作業
  - 生成されている`Vagrantfile`の内容を[Vagrantfile.ubuntu1804](vagrant/Vagrantfile.ubuntu1804)で上書きする
  - `Vagrant_provision.sh`というファイルを新規作成し、[Vagrant_provision.sh.ubuntu1804](vagrant/Vagrant_provision.sh.ubuntu1804)で上書きする

### 仮想マシンの起動

#### 方法１：VSCodeから起動（おすすめ）

- VSCodeの上部メニュー > ファイル > フォルダを開く > `C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804`を選択
- VSCodeの上部メニュー > ターミナル > 新しいターミナル`
- 以下のコマンドを実行
```
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>vagrant up --provider=virtualbox
```

#### 方法２：Windows PowerShellから起動

- 仮想マシンを起動したいだけならば、方法２でも十分
```
PS C:\Users\アカウント名> cd C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>vagrant up --provider=virtualbox
...
```

### 仮想マシンへのSSH接続

#### 方法１：`Termius`（おすすめ）

- [Termiusをインストール](pc-termius.md)
- 新しいホストを作成
  - ホスト名：Ubuntu 18.04 LTS（例）
  - アドレス：192.168.33.10
  - ユーザ名：vagrant
  - パスワード：vagrant
- 接続

#### 方法２：`Windows Powershell (x86)`

- `Windows Powershell (x86)`アプリ、あるいは、`VSCode`内のターミナルから以下のコマンドを実行
```
PS C:\Users\アカウント名> cd C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>vagrant ssh
```

### 仮想マシンの終了

- 仮想マシンを起動した端末で以下のコマンドを実行
```
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\Ubuntu1804>vagrant halt
```
