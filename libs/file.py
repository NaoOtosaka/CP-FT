from tools.check import *
from tools.copy import *


def cp_case_temp_file(origin_case_dir_name, project_name):
    """
    生成原始模板文件
    :param origin_case_dir_name:
    :param project_name:
    :return:
    """
    cp_file(config.tempDir + config.case_temp_file_name,
            origin_case_dir_name + project_name + config.case_file_name)


def cp_smoke_case_temp_file(smoke_case_dir_name, project_name):
    """
    生成原始模板文件
    :param smoke_case_dir_name:
    :param project_name:
    :return:
    """
    cp_file(config.tempDir + config.smoke_case_temp_file_name,
            smoke_case_dir_name + project_name + config.smoke_file_name)


def cp_h5_compatibility_file(project_path, project_name):
    """
    生成H5兼容性测试模板
    :param project_path:
    :param project_name:
    :return:
    """
    cp_file(config.tempDir + config.H5_compatibility_file_name,
            project_path + project_name + config.H5_file_name)


def cp_web_compatibility_file(project_path, project_name):
    """
    生成WEB兼容性测试模板
    :param project_path:
    :param project_name:
    :return:
    """
    cp_file(config.tempDir + config.web_compatibility_file_name,
            project_path + project_name + config.web_file_name)

