import argparse
import project.delete_directory as delete_directory

parser = argparse.ArgumentParser(description='レポート削除ライブラリ')
parser.add_argument('--dir_path', help='監視パス', required=True)
parser.add_argument('--delete', help='削除フラグ', action='store_true')
parser.add_argument('--check', help='確認フラグ', action='store_true')
parser.add_argument('--delete_day', help='何日以前のデータを削除するか', default=180)

args = parser.parse_args()


def main():
    delete_directory.delete_directory(args.dir_path, args.delete, args.check)


if __name__ == '__main__':
    main()
