# CentOS 7 + Elasticsearch + Kibanaの仮想マシンの生成

:bulb: 仮想マシンは使いたい時に起動し、使い終わったら終了する習慣をつけましょう。

## 所要時間

- 30分

## 手順

### 仮想マシンの作成
- [CentOS 7を使った仮想マシンの生成](vm-centos7.md)の手順に従う
  - ただし、フォルダ名は`CentOS7-EK`に変える
- `Vagrantfile`と`Vagrant_provision-sh`は以下のファイルを使用する
  - [Vagrantfile.centos7.ek](vagrant/Vagrantfile.centos7.ek)
  - [Vagrant_provision.sh.centos7.ek](vagrant/Vagrant_provision.sh.centos7.ek)

### 仮想マシンの起動
- [CentOS 7を使った仮想マシンの生成](vm-centos7.md)の手順に従う
  - ただし、フォルダ名は`CentOS7-EK`に読み替える

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
- [CentOS 7を使った仮想マシンの生成](vm-centos7.md)の手順に従う
  - ただし、ホスト側のフォルダ名は`CentOS7-EK`に読み替える

### 仮想マシンの終了
- [CentOS 7を使った仮想マシンの生成](vm-centos7.md)の手順に従う
  - ただし、ホスト側のフォルダ名は`CentOS7-EK`に読み替える
