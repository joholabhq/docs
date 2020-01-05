# CapsLockキーをCtrlキーとして使う

## 参考URL

- https://ascii.jp/elem/000/000/927/927191/

## 所要時間

- 10分

## 手順１（`CapsLockキー`を`Ctrlキー`として使う場合）

- `Windowsキー`と`S`を同時に押して、検索画面を開く
- 検索画面に`regedit`と入力 → `レジストリエディタ`を選択
- 左パネルから`HKEY_LOCAL_MACHINE` > `SYSTEM` > `CurrentControlSet` > `Control` >`Keyboard Layout`を選択
- `編集` > `新規` > `バイナリ値`を選択
- 名前に`Scancode Map`と入力し、ダブルクリック
- 値のデータに、以下を入力

```
000000  00 00 00 00 00 00 00 00
000008  02 00 00 00 1D 00 3A 00
000010  00 00 00 00
```

- `OK`
- PCを再起動する
- `CapsLockキー`と`スペースキー`でIMEの切り替えができている（＝`CapsLockキー`を`Ctrlキー`として使っている）ことを確認
- `Ctrlキー`と`スペースキー`でIMEの切り替えができている（＝`Ctrlキー`はそのまま機能する）ことを確認

## 手順２（`CapsLockキー`と`Ctrlキー`を入れ替えて使う場合）

- `Windowsキー`と`S`を同時に押して、検索画面を開く
- 検索画面に`regedit`と入力 → `レジストリエディタ`を選択
- 左パネルから`HKEY_LOCAL_MACHINE` > `SYSTEM` > `CurrentControlSet` > `Control` >`Keyboard Layout`を選択
- `編集` > `新規` > `バイナリ値`を選択
- 名前に`Scancode Map`と入力し、ダブルクリック
- 値のデータに、以下を入力

```
000000  00 00 00 00 00 00 00 00
000008  03 00 00 00 1D 00 3A 00
000010  3A 00 1D 00 00 00 00 00
000018  
```

- `OK`
- PCを再起動する
- `CapsLockキー`と`スペースキー`でIMEの切り替えができている（＝`CapsLockキー`を`Ctrlキー`として使っている）ことを確認
- `Ctrolキー`を押して、CapsLockがかかる（`CapsLockキー`に明かりがつく）ことを確認
