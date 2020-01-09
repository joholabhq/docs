# TeXLive

## 所要時間

- 2時間

## 手順

- [Installing TeX Live over the Internet](https://www.tug.org/texlive/acquire-netinstall.html)にいき、`install-tl.zip`をダウンロード
- TeXLiveのインストーラーは、パスに日本語があると正しく動作しないので、`C:\Home\sNNNNNNN\Downloads`というフォルダを作成し（[参考](pc-virtualbox-vagrant.md)）、ダウンロードしたZipファイルを保存
- Zipファイルを右クリック > ここに展開
- :warning: `Windows Powershell (x86)`を管理者権限で起動し、以下のコマンドを実行
```
PS C:\WINDOWS\system32>
PS C:\WINDOWS\system32>cd C:\Home\sNNNNNNN\Downloads\install-tl\install-tl-yyyymmdd # ← yyyymmddの部分は自分の環境に合わせる
PS C:\Home\sNNNNNNN\Downloads\install-tl\install-tl-yyyymmdd> install-tl-windows.bat
```
- TeX Liveインストーラーが起動したら、「インストール」を選択
- 4000近い数のパッケージがインストールされるまで待つ
