from libs.data import data_input
from libs.project import main as create_file
from tools.show import *
from tools.check import check_file


def setup():
    # 启动自检
    print('======>>>>>启动自检')
    if not check_file():
        input('回车以退出')
        return
    print('===================================')
    data = data_input()
    show_input_info(data)
    create_file(data)


if __name__ == '__main__':
    setup()