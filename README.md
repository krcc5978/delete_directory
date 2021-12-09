# フォルダ監視
フォルダ内のフォルダやファイルで一定期間以上の物を削除する

## ディレクトリ構成
```
07_DeleteDirectory
├─ project
|  ├─ __init__.py
|  ├─ delete_directory.py
|  ├─ main.py
|  └─ make_test_data.py
|
├─ test(自動テスト用ディレクトリ)
|  ├─ __init__.py
|  ├─ conftest.py
|  ├─ main.py
|  └─ test_delete_derectory.py
|　
├─ README.md
└─ requirements.txt
```

## 環境構築（python）
pythonの仮想環境を作成し、仮想環境上で必要モジュールを取得してくる  
仮想環境を作る必要はないが仮想環境を作成しておくと他のバージョンなどを試す際に別の仮想環境を立てればよくなるため環境が汚れなくなる

仮想環境作成方法（venv）
```
【仮想環境用ディレクトリ作成】
mkdir [ディレクトリ名]
cd [ディレクトリ名]

【仮想環境作成】
python -m venv [modules]
# [modules]の部分は任意の文字列を入力してください

【仮想環境アクティベート】
[modules]\Scripts\activate

【必要モジュールインストール】
pip install -r requirements.txt
```

## .exe生成
main.pyのある階層でpyinstallerを実行しEXEファイルを生成する
```
pyinstaller main.py --onefile 
```
dist内にmain.exeが生成されます


## 実行方法
コマンドライン引数を用いて対象ディレクトリ、削除フラグなどを設定し実行すること
```
--dir_path [ディレクトリパス] (必須): 監視するディレクトリパス
--delete ： 削除実行
--check : 削除対象ファイル確認
--delete_day [日数] (デフォルト：180日): 今日から数えて指定した日数より前のレポートの動画データを削除対象にする
```

```
（例）
main.exe --dir_path [ディレクトリパス] --check --delete --delete_day 180
```

## 自動テストについて
testディレクトリの階層に行き下記コマンドを実行することでテストの実施可能
```
>pytest
```