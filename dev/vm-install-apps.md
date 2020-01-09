# 仮想マシンにアプリをインストールする方法

[Ubuntu 18.04 LTSを使った仮想マシンの作成](vm-ubuntu1804.md)や[CenOS 7を使った仮想マシンの作成](vm-centos8.md)で生成した仮想マシンの中身は、Linuxですので、それぞれのディストリビューションのやり方に沿ってアプリをインストールすることができます。

## 所要時間

- 任意

## 参考URL

- Server World https://www.server-world.info/
  - [Ubuntu 18.04 LTS](https://www.server-world.info/query?os=Ubuntu_18.04)
  - [CentOS 8](https://www.server-world.info/query?os=CentOS)
  
## 手順１：仮想マシンにSSH接続した後に、アプリをインストールする

- [Ubuntu 18.04 LTSを使った仮想マシンの作成](vm-ubuntu1804.md)や[CenOS 7を使った仮想マシンの作成](vm-centos8.md)を参考に、仮想マシンにSSH接続する。
- 参考URLのサイト等を参考に、インストールをおこなう。

## 手順２：`Vagrant_provision.sh`にインストールするアプリを記述する

- 仮想マシンが生成される（あるいは起動する）段階で一緒にアプリのインストールをしたい場合は、[Ubuntu 18.04 LTSを使った仮想マシンの作成](vm-ubuntu1804.md)や[CenOS 7を使った仮想マシンの作成](vm-centos8.md)からリンクされている`Vagrant_provision.sh`にインストールコマンドを追加する。
- Ubuntu 18.4 LTSの例（:bulb: アプリのインストールコマンドはディストリビューションによって異なるので注意が必要）

[Vagrant_provision.sh.ubuntu1804](vagrant/Vagrant_provision.sh.ubuntu1804)
```
# Update package
echo "============ PROVISIONING: Updating default packages ..."
sudo apt update -y
sudo apt upgrade -y

# Install dev tools
echo "============ PROVISIONING: Installing Development tools ..."
sudo apt install -y build-essential
```
↓
```
# Update package
echo "============ PROVISIONING: Updating default packages ..."
sudo apt update -y
sudo apt upgrade -y

# Install dev tools
echo "============ PROVISIONING: Installing Development tools ..."
sudo apt install -y build-essential

# Install additional apps
echo "============ PROVISIONING: Installing additional applications ..."
sudo apt install -y [アプリの名前]
```
