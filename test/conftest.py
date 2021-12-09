import os
import pytest
import datetime
import win32_setctime

main_dir_path = './share_folder/'
make_dir_dict = {'00000000': [datetime.datetime(2021, 12, 9, 0, 0, 0).timestamp(),
                              datetime.datetime(2021, 12, 9, 0, 0, 0).timestamp(),
                              datetime.datetime(2021, 12, 9, 0, 0, 0).timestamp()
                              ],
                 '00000001': [datetime.datetime(2021, 6, 12, 0, 0, 0).timestamp(),
                              datetime.datetime(2021, 12, 9, 0, 0, 0).timestamp(),
                              datetime.datetime(2021, 12, 9, 0, 0, 0).timestamp()
                              ]
                 }
report_data = ['000', '001', '002', '003', '004', '00000000', '00000001']
file_list = ['00000000.txt', '00000001.txt']


# @pytest.fixture(scope='function', autouse=True)
@pytest.fixture
def prepare_test():
    for report_id, timestamp_list in make_dir_dict.items():
        make_dir_path = main_dir_path + report_id
        os.makedirs(make_dir_path, exist_ok=True)
        win32_setctime.setctime(make_dir_path, timestamp_list[0])
        os.utime(make_dir_path, (timestamp_list[1], timestamp_list[2]))

        for report in report_data:
            report_path = f'{make_dir_path}/{report}'
            os.makedirs(report_path, exist_ok=True)

        for file in file_list:
            file_path = f'{make_dir_path}/{file}'
            with open(file_path, 'w') as f:
                f.write('')

