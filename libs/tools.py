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
