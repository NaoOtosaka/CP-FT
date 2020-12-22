from libs.file import *
from libs.dir import *
from tools.check import *


def create_project(project_name, has_smoke_test, h5_compatibility, web_compatibility):
    # 控制台指令输出UTF-8代码页
    os.system('chcp 65001')
    # 检查输出目录
    print('======>>>>>检查输出根目录文件夹')
    check_output_dir()
    # 初始化项目文件夹
    print('======>>>>>初始化项目文件夹')
    project_path = create_project_dir(project_name)
    path = create_other_subdirectory_dir(project_path)
    # 载入用例模板
    print('======>>>>>载入基础用例模板')
    cp_case_temp_file(path[0], project_name)
    if has_smoke_test:
        print('======>>>>>载入冒烟用例模板')
        smoke_path = create_smoke_subdirectory_dir(project_path)
        cp_smoke_case_temp_file(smoke_path, project_name)
    if h5_compatibility:
        print('======>>>>>载入H5兼容性模板')
        cp_h5_compatibility_file(project_path, project_name)
    if web_compatibility:
        print('======>>>>>载入WEB兼容性模板')
        cp_web_compatibility_file(project_path, project_name)
    # 打开对应目录
    if open_dir(project_path):
        print("项目生成路径：" + project_path)
    else:
        print("路径异常")


def main(data_dict):
    """
    :type data_dict dict
    :param data_dict:
    :return:
    """
    # 文件初始化
    create_project(data_dict['项目名'], data_dict['冒烟测试'], data_dict['H5兼容性自测'], data_dict['WEB兼容性自测'])
