import json


def load_conf():
    """
    载入配置文件
    :return:
    """
    f = open("conf.json", encoding='utf-8')
    setting = json.load(f)
    return setting

