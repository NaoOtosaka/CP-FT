import config
from libs.tools import *


def get_input_2_boolean(tip_msg):
    """
    返回输入结果的布尔类型判定
    :return:
    """
    msg = tip_msg + '（y/n）'
    has_smoke_test = input(msg)
    if has_smoke_test == 'y' or has_smoke_test == '':
        return True
    else:
        return False


def get_project_name():
    """
    获取项目名
    :return:
    """
    project_name = input('请输入需求名（回车结束）：')
    if project_name == "":
        project_name = config.default_project_name

    return project_name


def smoke_test_status():
    """
    判断是否包含冒烟测试
    :return:
    """
    return get_input_2_boolean('是否包含冒烟测试?')


def h5_compatibility_test_status():
    """
    是否包含H5兼容性测试
    :return:
    """
    return get_input_2_boolean('是否自测H5兼容性?')


def web_compatibility_test_status():
    """
    是否包含web兼容性测试
    :return:
    """
    return get_input_2_boolean('是否自测WEB兼容性?')


def data_validation():
    """
    用户确认数据
    :return:
    """
    return get_input_2_boolean('请确认数据无误')


def data_input():
    """
    数据获取逻辑
    :return:
    """
    temp = {}
    while not temp:
        project = get_project_name()
        has_smoke_test = smoke_test_status()
        h5_compatibility = h5_compatibility_test_status()
        web_compatibility = web_compatibility_test_status()
        temp = {
            '项目名': project,
            '冒烟测试': has_smoke_test,
            'H5兼容性自测': h5_compatibility,
            'WEB兼容性自测': web_compatibility
        }
        print("===================================")
        print("确认项目信息:")
        show_input_info(temp)
        print("===================================")
        if not data_validation():
            temp = {}
    return temp
