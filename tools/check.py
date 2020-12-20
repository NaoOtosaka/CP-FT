import os
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


def check_file():
    """
    启动自检
    :return:
    """
    # 模板完整性检查
    template_list = ['base', 'smoke', 'H5', 'WEB']
    fail_list = []
    for temp in template_list:
        print('======>>>>>' + temp + ' template check')
        if check_template(temp):
            print('ok')
        else:
            print('fail')
            fail_list.append(temp)

    if fail_list:
        for temp in fail_list:
            print(temp + '模板丢失，请检查对应模板文件是否存在')
        return False
    else:
        return True
