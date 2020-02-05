# Marpを使った発表スライドの作成

:bulb: VSCode内で作業をします

## Marpのインストール

- [VSCodeのインストール](../dev/pc-vscode.md)を参考に、Marp用拡張機能をインストール

## 作業用フォルダの作成

- [ファイルやデータの整理](files-and-data.md)を参考に、`Presentation`フォルダを作成
- `Presentation`フォルダの下に、発表会名のフォルダを作成（例：合同研究発表会20200324）
- [発表用Marpテンプレート](../templates/marp-lab)からファイルをコピーして、作成したフォルダに保存
- 以下のようなファイル構成になっていることを確認
  - `tsukuba-logo.png`のありかは指導教員に確認

### ファイル構成例

```
C:
  ├ Users
    ├ アカウント名
      ├ SynologyDrive
        ├ ...
        ├ MyFolders
          ├ ...
          ├ Presentation # 発表資料
           ├ 合同研究発表会20200324
             ├ presentation.md
             └ images
               └ tsukuba-logo.png 
```

## プレビューの表示

- `presentation.md`を選択
- 編集ペイン右上のプレビューアイコンをクリック

## 発表原稿の作成

- Marpの記法にしたがってスライドを作成していく
- :bulb: 全体的な方針としてシンプルなスライドを目指しましょう

### 画像について

- 画像は別のアプリで作成し、`images`フォルダの下に保存する
- スライドに挿入するには、`![](images/画像ファイル名.png)`と書く

### 表について

- 簡単な表はMarpの記法で作成
- 複雑な表はExcelなどで作成し、そのスクショを画像として挿入


### スライドの形の変更

- `presentation.md`を編集
```
size: 4:3
```
↓
```
size: 16:9
```

### 背景画像の変更

- 既存のスタイルに変化をつけたい場合は、タイトルスライドに背景画像を使いましょう
- 任意の背景画像をimagesフォルダに保存
- `presentation.md`を編集
```
<!-- _class: lead invert -->
# 発表題目
```
↓
```
<!-- _class: lead -->
![bg](images/自分の画像ファイル名.png)
# 発表題目
```
もしくは
```
<!-- _class: lead invert -->
![bg](images/自分の画像ファイル名.png)
# 発表題目
```

## PDFへの書き出し

- 編集画面ペイン右上のMarpアイコンを選択 > Export slide deck ... を選択
- 保存先を指定 > Export
- PDFが書き出されたことを確認

出力例：[presentation.pdf](../templates/marp-lab/presentation.pdf)

## Marpではできないこと

- 2段組みなどの複雑なレイアウト
- アニメーション

## 参考URL

- https://github.com/marp-team/marp-core
