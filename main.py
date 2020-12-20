from libs.data import data_input
from libs.project import main as create_file
from tools.show import *


def setup():
    data = data_input()
    show_input_info(data)
    create_file(data)


if __name__ == '__main__':
    setup()