import config


def show_input_info(data_dict):
    """
    展示已有信息
    :type data_dict dict
    :param data_dict: 信息字典
    :return:
    """
    if data_dict:
        for k, v in data_dict.items():
            print(k + ':' + str(v))


def show_project_path():
    """
    展示当前项目目录生成路径
    :return:
    """
    if config.projectDir:
        print(config.projectDir)
        return config.projectDir
    else:
        return False
