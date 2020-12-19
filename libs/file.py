import os
import shutil
import config


def check_output_dir():
    """
    检测输出目录
    :return:
    """
    if not os.path.exists(config.projectDir):
        print('创建项目存储根目录')
        os.mkdir(config.projectDir)


def check_uniqueness(path):
    """
    检测目录唯一性
    :return:
    """
    if os.path.exists(path):
        return True
    else:
        return False


def check_template(template_type):
    """
    检测模板完整性
    :param template_type:
    :return:
    """
    if template_type == 'smoke':
        return os.path.exists(config.tempDir + config.smoke_case_temp_file_name)
    elif template_type == 'H5':
        return os.path.exists(config.tempDir + config.H5_compatibility_file_name)
    elif template_type == 'WEB':
        return os.path.exists(config.tempDir + config.web_compatibility_file_name)
    elif template_type == 'base':
        return os.path.exists(config.tempDir + config.case_temp_file_name)


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


def cp_file(template_path, project_path):
    """
    拷贝文件
    :param project_path:
    :param template_path:
    :return:
    """
    shutil.copyfile(template_path, project_path)
    # os.system('copy' + project_path + ' ' + template_path)


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