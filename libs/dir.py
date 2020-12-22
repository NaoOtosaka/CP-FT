import os
from tools.check import *


def create_project_dir(project_name):
    """
    创建项目文件夹
    :param project_name:
    :return:
    """
    if check_uniqueness(config.projectDir + project_name):
        print('存在同名项目文件夹，请处理后重新操作')
        return False
    else:
        os.mkdir(config.projectDir + project_name)
        return config.projectDir + project_name + '\\'


def create_smoke_subdirectory_dir(project_dir_path):
    """
    创建冒烟测试子目录
    :param project_dir_path:
    :return:
    """
    if project_dir_path:
        if not check_uniqueness(project_dir_path + config.smoke_dir_name):
            os.mkdir(project_dir_path + config.smoke_dir_name)
    return project_dir_path + config.smoke_dir_name + '\\'


def create_other_subdirectory_dir(project_dir_path):
    """
    创建其它子目录
    :param project_dir_path:
    :return:
    """
    if project_dir_path:
        # 创建原始用例文件夹
        if not check_uniqueness(project_dir_path + config.origin_case_dir_name):
            os.mkdir(project_dir_path + config.origin_case_dir_name)
        # 创建执行用例文件夹
        if not check_uniqueness(project_dir_path + config.execute_case_dir_name):
            os.mkdir(project_dir_path + config.execute_case_dir_name)

    return [
        project_dir_path + config.origin_case_dir_name + '\\',
        project_dir_path + config.execute_case_dir_name + '\\'
    ]


def open_dir(path):
    """
    打开对应文件夹
    :param path:
    :return:
    """
    if path:
        os.startfile(path=path)
        return True
    else:
        return False