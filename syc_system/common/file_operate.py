import os
from datetime import datetime

from syc_system.settings.base import BAK_FILE_PATHS


def create_date_format():
    today = datetime.now()
    str_year = str(today.year)
    str_month = str(today.month) if today.month > 10 else '0' + str(today.month)
    str_day = str(today.day) if today.day > 10 else '0' + str(today.day)
    data_format = str_month + '.' + str_day
    return str_year, str_month, data_format


def create_dirs(dir_path):
    try:
        os.makedirs(dir_path)
    except FileExistsError:
        print('文件已存在')
    else:
        return


def create_customer_info_file(fr):
    str_year, str_month, date_format = create_date_format()
    dir_path = os.path.join(BAK_FILE_PATHS.get('BASIC_INFO_CUSTOMER_INFO'), str_year, str_month)
    create_dirs(dir_path)
    file_name = date_format + '.xlsx'
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'wb') as fw:
        for line in fr:
            fw.write(line)
    return file_path
