import os
import datetime
from project.delete_directory import get_delete_dir_list, get_create_date, check_date, delete_directory
from test.conftest import main_dir_path, make_dir_dict


def test_get_delete_dir_list(prepare_test):
    assert get_delete_dir_list(main_dir_path) == [main_dir_path + list(make_dir_dict.keys())[1]]


def test_get_date_1(prepare_test):
    str_time = '2021/12/09'
    tdatetime = datetime.datetime.strptime(str_time, '%Y/%m/%d')
    tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
    assert get_create_date(main_dir_path + list(make_dir_dict.keys())[0]) == tdate


def test_get_date_2(prepare_test):
    str_time = '2021/12/09'
    tdatetime = datetime.datetime.strptime(str_time, '%Y/%m/%d')
    tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
    assert get_create_date(main_dir_path + list(make_dir_dict.keys())[1]) != tdate


def test_delete_directory_1(prepare_test):
    flag = True
    delete_directory(main_dir_path)

    result_list = ['000', '001', '002', '003', '004', '00000000', '00000001']
    for result in result_list:
        if not result in os.listdir(main_dir_path + list(make_dir_dict.keys())[1]):
            flag = False
            break

    assert flag


def test_delete_directory_2(prepare_test):
    flag = True
    delete_directory(main_dir_path, delete_flag=False, check_flag=True)

    result_list = ['000', '001', '002', '003', '004', '00000000', '00000001']
    for result in result_list:
        if not result in os.listdir(main_dir_path + list(make_dir_dict.keys())[1]):
            flag = False
            break

    assert flag


def test_delete_directory_3(prepare_test):
    flag = True
    delete_directory(main_dir_path, delete_flag=True, check_flag=False)

    result_list = ['000', '001', '002', '003', '004']
    for result in result_list:
        if not result in os.listdir(main_dir_path + list(make_dir_dict.keys())[1]):
            flag = False
            break

    assert flag


def test_delete_directory_4(prepare_test):
    delete_directory(main_dir_path, delete_flag=True, check_flag=True)
    assert ['000', '001', '002', '003', '004'] == os.listdir(main_dir_path + list(make_dir_dict.keys())[1])


def test_check_date_1():
    now_date = datetime.date.today()
    half_year_date = now_date - datetime.timedelta(days=179)
    assert not check_date(half_year_date)


def test_check_date_2():
    now_date = datetime.date.today()
    half_year_date = now_date - datetime.timedelta(days=180)
    assert check_date(half_year_date)


def test_check_date_3():
    now_date = datetime.date.today()
    half_year_date = now_date - datetime.timedelta(days=181)
    assert check_date(half_year_date)
