# CentOS 8 + Elasticsearch + Kibanaの仮想マシンの生成

:bulb: 仮想マシンは使いたい時に起動し、使い終わったら終了する習慣をつけましょう。

## 所要時間

- 30分

## 手順

### 仮想マシンの作成
- [VirtualBoxとVagrantのインストール](pc-virtualbox-vagrant.md)
- `Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名>cd C:\Home\sNNNNNNN\Workspace\Local\Vagrant
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant>mkdir CentOS7-EK; cd CentOS7-EK
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK>vagrant box add centos/8
...
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK>vagrant init centos/8
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK>code . # VSCodeの起動
```
- 以下はVSCode上で作業
  - 生成されている`Vagrantfile`の内容を[Vagrantfile.centos7.ek](vagrant/Vagrantfile.centos7.ek)で上書きする
  - `Vagrant_provision.sh`というファイルを新規作成し、[Vagrant_provision.sh.centos7.ek](vagrant/Vagrant_provision.sh.centos7.ek)をで上書きする

### 仮想マシンの起動

#### 方法１：VSCodeから起動（おすすめ）

- VSCodeで`C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK`フォルダを開く
- VSCodeの上部メニュー > ターミナル > 新しいターミナル`
- 以下のコマンドを実行
```
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK>vagrant up
```

#### 方法２：Windows PowerShellから起動

- 仮想マシンを起動したいだけならば、方法２でも十分
```
PS C:\Users\アカウント名> cd C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK>vagrant up
...
```

### 仮想マシン上のElasticsearchへの接続

- http://192.168.33.10:9200
- 以下のような出力が表示されたら、正常に動作しています
```
{
  "name" : "gK2xvEj",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "CsFaFfVPRBCUo0Y3ZpODsw",
  "version" : {
    "number" : "6.8.6",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "3d9f765",
    "build_date" : "2019-12-13T17:11:52.013738Z",
    "build_snapshot" : false,
    "lucene_version" : "7.7.2",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

### 仮想マシン上のKibanaへの接続

:bulb: `Kibana`はアクセスできるようになるまで、少し時間がかかる場合があります

- http://192.168.33.10:5601


### 仮想マシンとのファイル共有

- 仮想マシン内のファイルは仮想マシンを終了するとアクセスできなくなります。
- 仮想マシンでの作業後にホストマシンでアクセスしたいファイルやデータがある場合は、共有フォルダに保存しましょう。
- 共有フォルダの位置
  - 仮想マシン：`/vagrant`
  - ホストマシン：`C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK`

### 仮想マシンの終了

- 仮想マシンを起動した端末で以下のコマンドを実行
```
PS C:\Home\sNNNNNNN\Workspace\Local\Vagrant\CentOS7-EK>vagrant halt
```
