from libs.file import *
from libs.dir import *
from tools.check import *


def create_project(project_name, has_smoke_test, h5_compatibility, web_compatibility):
    os.system('chcp 65001')
    check_output_dir()
    project_path = create_project_dir(project_name)
    path = create_other_subdirectory_dir(project_path)
    cp_case_temp_file(path[0], project_name)
    if has_smoke_test:
        smoke_path = create_smoke_subdirectory_dir(project_path)
        cp_smoke_case_temp_file(smoke_path, project_name)
    if h5_compatibility:
        cp_h5_compatibility_file(project_path, project_name)
    if web_compatibility:
        cp_web_compatibility_file(project_path, project_name)


def main(data_dict):
    """
    :type data_dict dict
    :param data_dict:
    :return:
    """
    create_project(data_dict['项目名'], data_dict['冒烟测试'], data_dict['H5兼容性自测'], data_dict['WEB兼容性自测'])