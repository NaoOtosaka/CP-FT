import json


def load_conf():
    f = open("conf.json", encoding='utf-8')
    setting = json.load(f)
    return setting

