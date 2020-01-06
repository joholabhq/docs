# Ubuntu 18.04 LTSを使った仮想マシンの生成

## 所要時間

- 30分

## 手順

- [ユーザフォルダ内作業エリアの作成](pc-workspace.md)
- （1回目のみ）`Windows Powershell (x86)`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名>cd Workspace
PS C:\Users\アカウント名>cd Local
PS C:\Users\アカウント名>mkdir Vagrant
PS C:\Users\アカウント名>cd Vagrant
PS C:\Users\アカウント名>mkdir Ubuntu1804
PS C:\Users\アカウント名>cd Ubuntu1804
PS C:\Users\アカウント名>vagrant add box bento/ubuntu-18.04
```

- （2回目以降）`Windows Powershell (x86)`を起動
