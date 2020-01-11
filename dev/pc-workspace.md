# PC内作業エリアの作成

## 本作業の背景

- 研究室PCは[Office365のアカウント](https://github.com/joholabhq/docs/blob/ja/onboarding/getting-started.md)でログインすることを想定しています。
- これによりアカウント名が自動的に日本語になる場合があります。これはホームフォルダのパスに日本語が含まれることを意味します。
  - 現状では、Office365のアカウント名は変更できないようです
- インストールするプログラムによっては、ホームフォルダのパスに日本語が含まれていると正常に動作しないことがあります。
- したがって、日本語を含まない場所にもう一つのホームフォルダ（第２作業エリア）を作成し、必要に応じて使い分けます。

## 所要時間

- 10分

## 手順1：デフォルトの作業エリア（第１作業エリア）

- `Windows PowerShell (x86)`を起動し、以下のコマンドを実行（エクスプローラーで作業しても良い）
```
PS C:\Users\アカウント名> mkdir Workspace
PS C:\Users\アカウント名> cd Workspace
PS C:\Users\アカウント名> mkdir Local
```
- 結果
```
C:
  ├ Users
    ├ アカウント名
      ├ Workspace
        ├ Local
```

## 手順2: 第２作業エリア

- `Windows PowerShell (x86)`を起動し、以下のコマンドを実行（エクスプローラーで作業しても良い）
- `sNNNNNNN`は統一認証のユーザ名（半角英数）
```
PS C:\Users\アカウント名>cd C:\
PS C:\>mkdir Home; cd Home
PS C:\Home>mkdir sNNNNNNN; cd sNNNNNNN
PS C:\Home\sNNNNNNN>mkdir Workspace; cd Workspace
PS C:\Home\sNNNNNNN\Workspace>mkdir Local
```
- 結果
```
C:
  ├ Home
    ├ sNNNNNNN
      ├ Workspace
        ├ Local
```
