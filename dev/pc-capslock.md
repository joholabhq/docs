# CapsLockキーをCtrlキーとして使う

## 参考URL

- https://ascii.jp/elem/000/000/927/927191/

## 所要時間

- 10分

## 手順１（`CapsLock`キーを`Ctrl`キーとして使う場合）

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
- `CapsLock`キーと`スペースキー`でIMEの切り替えができている（＝`CapsLock`キーを`Ctrl`キーとして使っている）ことを確認
- `Ctrl`キーと`スペースキー`でIMEの切り替えができている（＝`Ctrl`キーはそのまま機能する）ことを確認

## 手順２（`CapsLock`キーと`Ctrl`キーを入れ替えて使う場合）

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
- `CapsLock`キーと`スペースキー`でIMEの切り替えができている（＝`CapsLock`キーを`Ctrl`キーとして使っている）ことを確認
- `Ctrl`キーを押して、CapsLockがかかる（`CapsLock`キーに明かりがつく）ことを確認
