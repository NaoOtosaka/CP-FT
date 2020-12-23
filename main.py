from libs.data import data_input
from libs.project import main as create_file
from libs.dir import *
from tools.show import *
from tools.check import check_file


def setup():
    # 启动自检
    print('======>>>>>启动自检')
    if not check_file():
        input('回车以退出')
        return
    print('===================================')
    # 项目输出路径设置
    print('当前项目输出路径：')
    if not show_project_path():
        print('未定义项目输出路径')
    else:
        edit_project_path()
    print('===================================')
    # 信息输入

    data = data_input()
    # 信息复核
    show_input_info(data)
    # 文件初始化
    create_file(data)
    input('创建完成')


if __name__ == '__main__':
    setup()