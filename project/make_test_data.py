import os
import argparse
import datetime
import win32_setctime

parser = argparse.ArgumentParser(description='レポート削除ライブラリ')
parser.add_argument('--dir_path', help='監視ディレクトリパス', required=True)

args = parser.parse_args()

main_dir_path = args.dir_path
year = 2021
month = 1
day = 1
hour = 8
minute = 30
second = 0

if __name__ == '__main__':

    base_create_time = datetime.datetime(year, month, day, hour, minute, second)
    base_update_time = datetime.datetime(year, month, day, hour, minute, second)
    base_access_time = datetime.datetime(year, month, day, hour, minute, second)

    for i in range(365):
        make_dir_path = main_dir_path + str(i).zfill(16)
        os.makedirs(make_dir_path, exist_ok=True)

        create_time = base_create_time + datetime.timedelta(days=i)
        update_time = base_update_time + datetime.timedelta(days=i)
        access_time = base_access_time + datetime.timedelta(days=i)

        win32_setctime.setctime(make_dir_path, create_time.timestamp())
        os.utime(make_dir_path, (update_time.timestamp(), access_time.timestamp()))

        for report_id in range(30):
            report_path = f'{make_dir_path}/{str(report_id).zfill(3)}'
            os.makedirs(report_path, exist_ok=True)

        for time in range(16):
            create_time = create_time + datetime.timedelta(minutes=30)
            str_time = create_time.strftime('%Y%m%d%H%M%S')
            movie_path = f'{make_dir_path}/CAM-I-01_{str(str_time).zfill(3)}'
            os.makedirs(movie_path, exist_ok=True)

            file_path = f'{movie_path}.mp4'
            with open(file_path, 'w') as f:
                f.write('')
