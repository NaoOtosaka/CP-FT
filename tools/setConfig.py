import json


def load_conf():
    """
    载入配置文件
    :return:
    """
    f = open("conf.json", encoding='utf-8')
    setting = json.load(f)
    print(type(setting))
    return setting


def dump_conf(conf):
    """
    写入配置文件
    :return:
    """
    conf = json.dumps(conf, indent=4, ensure_ascii=False)
    f = open('conf.json', 'w', encoding='utf-8')
    try:
        f.write(conf)
        print("路径更新成功")
        return True
    except IOError:
        print("配置文件更新失败")
        return False