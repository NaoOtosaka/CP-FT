import tkinter
from tkinter import filedialog
from tools.check import *
from tools.setConfig import *


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
        os.startfile(path)
        return True
    else:
        return False


def get_project_dir_path():
    """
    自定义选择路径
    :return:
    """
    root = tkinter.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()

    return folder_path


def edit_project_path():
    """
    更新选择项目输出路径
    :return:
    """
    if input('是否需要重新定义输出路径？(y/n/回车跳过)') == 'y':
        project_path = get_project_dir_path()
        if project_path:
            conf = load_conf()
            conf['projectDir'] = project_path + '\\'
            if dump_conf(conf):
                return True
            else:
                return False