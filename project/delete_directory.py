import os
import re
import shutil
import datetime


def delete_directory(dir_path, delete_flag=False, check_flag=False):
    dir_list = get_delete_dir_list(dir_path)
    for dir_path in dir_list:
        report_list = os.listdir(dir_path)
        for report in report_list:
            if not re.fullmatch('[0-9]{3}', report):
                if delete_flag:
                    if os.path.isfile(f'{dir_path}/{report}'):
                        os.remove(f'{dir_path}/{report}')
                    elif os.path.isdir(f'{dir_path}/{report}'):
                        shutil.rmtree(f'{dir_path}/{report}')
                    else:
                        print('ファイル形式がおかしいです')
                if check_flag:
                    print(f'{dir_path}/{report}')


def get_delete_dir_list(main_dir_path):
    dir_path_list = os.listdir(main_dir_path)

    delete_list = []

    for dir_path in dir_path_list:
        path = f'{main_dir_path}{dir_path}'
        create_time = get_create_date(path)

        if check_date(create_time):
            delete_list.append(path)

    return delete_list


def get_create_date(dir_path):
    '''
    ディレクトリ作成日取得
    :param dir_path: ディレクトリパス
    :return: ディレクトリ作成日
    '''
    create_time = os.path.getctime(dir_path)
    create_time = datetime.datetime.fromtimestamp(create_time)
    return datetime.date(create_time.year, create_time.month, create_time.day)


def check_date(create_date):
    now_date = datetime.date.today()
    half_year_date = now_date - datetime.timedelta(days=180)

    if half_year_date < create_date:
        return False
    else:
        return True