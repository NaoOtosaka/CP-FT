import shutil


def cp_file(template_path, project_path):
    """
    拷贝文件
    :param project_path:
    :param template_path:
    :return:
    """
    shutil.copyfile(template_path, project_path)
    # os.system('copy' + project_path + ' ' + template_path)
